from powerpulse_etl import decorators

def test_log_phase_decorator(caplog):
    @decorators.log_phase("Test Phase")
    def sample():
        return "OK"
    
    with caplog.at_level("INFO"):
        result = sample()

    assert result == "OK"
    assert "Test Phase started" in caplog.text
    assert "Test Phase completed" in caplog.text