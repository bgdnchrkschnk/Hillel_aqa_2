import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self):
        url = f"{self.base_url}/data"
        response = requests.get(url)
        return response


# api_client = APIClient("https://test-mock.com")
#
# print(
#     api_client.get_data(),
# )