import allure

import pytest
import faker
fake = faker.Faker()

from lesson_30.functions import sum_of_several_numbers, upper_some_text

@allure.suite("30 lesson")
@allure.epic("Lesson 30")
@allure.feature("30 lesson operations")
@allure.story("30 lesson math tests")
class Test30Lesson:

    @allure.title("Test sum of several numbers {input_data}")
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.parametrize("input_data, expected_output", [
        ([1, 2, 3], 6),
        ([-1, 0, 1], 0),
        ([10, 20, 30], 60)
    ])
    def test_sum_ref(self, input_data, expected_output):
        """Test description of sum"""
        actual_result = sum_of_several_numbers(input_data)
        with allure.step(f"Comparing actual result {actual_result} with expected {expected_output}"):
            assert actual_result == expected_output
        allure.attach(attachment_type=allure.attachment_type.TEXT, name="attached text", body=fake.text())

    @allure.title("Testing uppercase for string {input_string}")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("input_string, expected_output", [
        ("hello", "HELLO"),
        ("world", "WORLD")
    ])
    def test_uppercase(self, input_string, expected_output):
        """Test description of uppercase"""
        actual_result = upper_some_text(input_string)
        with allure.step(f"Comparing actual result {actual_result} with expected {expected_output}"):
            assert actual_result == expected_output
        allure.attach(attachment_type=allure.attachment_type.TEXT, name="attached text",body=fake.text())

    @allure.title("Testing failed assertion")
    @allure.description("Test description of failed assertion")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_failed(self):
        with allure.step("Asserting false"):
            assert False


    @allure.title("Testing yellow error")
    @allure.description("Test description of yellow error")
    @allure.issue(url="https://jira.com/BO-187", name="BO-187 bug link")
    @allure.link(url="https://jira.com/BO-187", name="BO-187 bug link")
    def test_yellow_error(self):
        with allure.step("Asserting division not 0"):
            assert 1 / 0
        allure.attach(attachment_type=allure.attachment_type.TEXT, name="attached text", body=fake.text())
