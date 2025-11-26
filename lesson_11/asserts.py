
expected_result = 1
actual_result = 2


# assert expected_result == actual_result, f"{expected_result} is not equal to {actual_result}"

condition = expected_result == actual_result

if bool(condition) is False:
    raise AssertionError(f"{expected_result} is not equal to {actual_result}")