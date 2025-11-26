# import unittest # bad practice
# from unittest import * # bad practice
from unittest import TestCase, main
from lesson_12.math_functions import add, subtract, CustomMathException, enter_danger_zone

class MathFunctionsTestSuite(TestCase):

    def test_add_is_correct(self):
        """
        Positive test of add function 1
        """
        a = 0
        b = 3
        result = add(a, b)
        # self.assertEqual(5, result, f"Custom message: a: {a}, b: {b} sum was expected to be 5 but got {result}")
        assert 5 == result, f"Custom message: a: {a}, b: {b} sum was expected to be 5 but got {result}"

    def test_add_is_correct_2(self):
        result = add(-2, -3)
        # self.assertEqual(-5, result)
        assert -5 == result

    def test_add_is_correct_3(self):
        result = add(-10, 10)
        # self.assertEqual(0, result)
        assert 0 == result

    def test_sub_is_correct(self):
        result = subtract(2, 3)
        # self.assertEqual(-1, result)
        assert -1 == result

    def test_sub_is_correct_2(self):
        result = subtract(-2, -3)
        # self.assertEqual(-5, result)
        assert 1 == result

    def test_sub_is_correct_3(self):
        result = subtract(-2, -2)
        # self.assertEqual(0, result)
        assert 0 == result

    def test_(self):
        assert 5 in [1,2,3,4,5] # self.AssertIn(a, b)
        assert bool([5])


    def test_add_custom_validation_error(self):
        with self.assertRaises(ArithmeticError):
            add("jnc", (2,4))


    def test_logger_danger_zone(self):
        with self.assertLogs(level="WARNING"):
            enter_danger_zone()



class OtherTest(TestCase):

    def test_user_is_registered_successfully(self, selenium_driver, db_client):
        """
        Test create user from browser registration page
        Verify user record is correctly saved in db users table.
        """
        test_user_data: dict = {"name": "Bohdan", "email": "nejknjkf@testmail.org"}
        selenium_driver.register_user(**test_user_data) # GUI user registration
        actual_db_result = db_client.get(f"SELECT * FROM users WHERE email='{test_user_data['name']}' AND username='{test_user_data['name']}'")
        # self.assertIsNotNone(db_result)
        # assert db_result is not None
        # assert bool(db_result)
        assert actual_db_result, f"User {test_user_data} was registered by registration form but not found in db users table."


    def test_negative_upper_func(self):
        """
        Test negative scenario of upper function
        """
        name = "Bohdan"
        # assert name.upper() == "Bohdan"
        # assert name.upper() is not None
        # assert name.upper().isalpha()
        assert name.upper() == "BOHDAN", f"It was expected name-{name} with ALL letters uppercase but got {name.upper()}"


if __name__ == '__main__': # якщо цей модуль буде імпортовато в інший файл, то main() не запуститься
    main(verbosity=2)


# self.assertNotEqual(a, b): Перевіряє, чи a не дорівнює b.  ->  assert a ! b
# self.assertTrue(expr): Перевіряє, чи вираз expr є True.
# self.assertFalse(expr): Перевіряє, чи вираз expr є хибним. ->
# self.assertFalse(is_invalid)
# self.assertIsNone(a): Перевіряє, чи a є None.
# self.assertIsNone(result)
# self.assertIsNotNone(a): Перевіряє, чи a не є None.
# self.assertIsNotNone(result)
# self.assertIn(a, b): Перевіряє, чи a входить в b.
# self.assertIn(item, container)
# self.assertNotIn(a, b): Перевіряє, чи a не входить в b.
# self.assertNotIn(item, container)