from decorators import timer_v3
import sys

def dummy_function():
    return "result"

class MockWritable:
    # This can be any class that implements at least the write method (writable)
    def __init__(self):
        self.outputs = []

    def write(self, s: str):
        self.outputs.append(s)

def test_timer_v3_with_Writable():
    # Given 
    mock_output = MockWritable()

    # When
    result = timer_v3(dummy_function, output=mock_output)()
    
    # Then
    assert result == "result"
    assert len(mock_output.outputs) == 1
    assert "Execution time:" in mock_output.outputs[0] and "seconds" in mock_output.outputs[0]

def test_timer_v3_with_non_Writable(capsys):
    result = timer_v3(dummy_function, output="not writable")()
    
    captured = capsys.readouterr()
    assert result == "result"
    assert "Given output does not have a write method." in captured.out
    assert "Execution time:" in captured.out and "seconds" in captured.out

def test_timer_v3_with_mock_write(mocker):
    # Given
    mock_write = mocker.patch('sys.stdout.write')

    # When
    result = timer_v3(dummy_function, output=sys.stdout)()

    # Then
    mock_write.assert_called_once()
    assert result == "result"
    assert "Execution time:" in mock_write.call_args_list[0][0][0] and "seconds" in mock_write.call_args_list[0][0][0]
