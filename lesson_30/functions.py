import logging

import allure


@allure.step("Calucate sum of several numbers {list_of_numbers}")
def sum_of_several_numbers(list_of_numbers: list) -> int:
    logging.info(f"Calculating sum of {list_of_numbers}")
    return sum(list_of_numbers)

@allure.step("Uppercase text {text}")
def upper_some_text(text: str) -> str:
    logging.info(f"Uppercasing text {text}")
    return text.upper()