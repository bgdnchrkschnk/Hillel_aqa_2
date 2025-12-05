from lesson_14.logging_function import log_event, get_last_log

class TestLogEvent:

    def test_log_event_success_status(self):
        test_username = None
        test_status = None
        test_data = {"username": test_username, "status": test_status}
        # log_event(username=test_username, status=test_status)
        log_event(**test_data)
        # last_log: str = get_last_log("logs.log")
        #
        expected_level = "INFO"
        expected_username = test_username
        expected_status = test_status

        actual_level = ...
        actual_username = ...
        actual_status = ...

        assert expected_level == actual_level, f"Level logging is incorrect. Expected: {expected_level}, Actual: {actual_level}"
        assert expected_username == actual_username, f"Username is incorrect. Expected: {expected_username}, Actual: {actual_username}"
        assert expected_status == actual_status, f"Status is incorrect. Expected: {expected_status}, Actual: {actual_status}"



    def test_log_event_error_status(self):
        ...

    def test_log_event_else_status(self):
        ...