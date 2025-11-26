import unittest
from unittest.mock import patch, Mock
from api_client import APIClient

class TestAPIClient(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        # Створюємо макет відповіді API-ендпоінта
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'MOCK TEST'}

        # Встановлюємо макет для функції get() з бібліотеки requests
        mock_get.return_value = mock_response

        # Тестуємо метод get_data() з класу APIClient
        api_client = APIClient(base_url="https://test-mock.com")
        result = api_client.get_data()

        # Перевіряємо результат
        assert result.status_code == 200
        self.assertEqual({'data': 'MOCK TEST'}, result.json())

    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        # Створюємо макет відповіді API-ендпоінта для
				# симуляції невдачі (status_code != 200)
        mock_response = Mock()
        mock_response.status_code = 404

        # Встановлюємо макет для функції get() з бібліотеки requests
        mock_get.return_value = mock_response

        # Тестуємо метод get_data() з класу APIClient при невдачі
        api_client = APIClient(base_url='https://api.example.com')
        result = api_client.get_data()

        # Перевіряємо, що результат - None при невдачі
        assert result.status_code != 200

if __name__ == '__main__':
    unittest.main()