import logging

import allure
import requests

_log = logging.getLogger('Main')
log_format = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

base_url = 'http://127.0.0.1:7070'
test_content_data = {'cars': ['Audi, VW', 'Toyota']}
test_content_data_2 = {'bikes': ['Honda', 'Suzuki']}


class TestFlaskContent:

    @allure.title("Test content adding")
    def test_add_content(self):
        """Test content adding, flask server should return 200 status code"""
        _log.info('Checking content adding...')
        with allure.step(f'Adding content..'):
            response_data = requests.post(f'{base_url}/content', json=test_content_data)
        with allure.step("Test checks"):
            assert response_data.status_code == 200, "Content was not created"
            assert response_data.json().get('message') == 'Content created successfully!'

    @allure.title("Test content adding")
    def test_get_content(self):
        """Test content getting, flask server should return 200 status code and content in response"""
        _log.info('Getting content...')
        with allure.step(f'Getting content..'):
            response_get = requests.get(f'{base_url}/content')
        with allure.step("Test checks"):
            assert response_get.status_code == 200, "Unable to get content"
            server_content = response_get.json().get('content')
            assert test_content_data in server_content

    @allure.title("Test content modifying")
    def test_modify_content(self):
        """Test content modifying, flask server should return 200 status code"""
        _log.info('Modifying content...')
        response = requests.put(f'{base_url}/content/0', json=test_content_data_2)
        assert response.status_code == 200, "Unable modify content"
        assert response.json().get('message') == 'Content updated successfully!'

    @allure.title("Test content deleting")
    def test_deleting_content(self):
        """Test content deleting, flask server should return 200 status code"""
        _log.info('Deleting content...')
        response = requests.delete(f'{base_url}/content/0')
        assert response.status_code == 200, "Unable delete content"
        assert response.json().get('message') == 'Content deleted successfully!'