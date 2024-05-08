from decorators import timer_v3
class MockWritable:
    # This can be any class that implements at least the write method (writable)
    def __init__(self):
        self.outputs = []

    def write(self, s: str):
        self.outputs.append(s)

def test_timer_v3_with_Writable():
    mock_output = MockWritable()

    @timer_v3(output=mock_output)
    def dummy_function():
        return "result"

    result = dummy_function()
    
    assert result == "result"
    assert len(mock_output.outputs) == 1
    assert "Execution time:" in mock_output.outputs[0] and "seconds" in mock_output.outputs[0]

def test_timer_v3_with_non_Writable(capsys):
    @timer_v3(output="not writable")
    def dummy_function():
        return "result"

    result = dummy_function()
    
    captured = capsys.readouterr()
    assert result == "result"
    assert "Given output does not have a write method." in captured.out
    import pdb; pdb.set_trace()
    assert "Execution time:" in captured.out and "seconds" in captured.out
