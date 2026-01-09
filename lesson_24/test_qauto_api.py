from lesson_24.base_qauto_api_client import BaseQAutoApiClient
from lesson_24.data_provider.sign_up_data import get_sign_up_data


class TestQAutoApi:

    api_client = BaseQAutoApiClient()

    def test_sign_up_and_sign_in_and_sign_out(self):
        test_user_data = get_sign_up_data()

        response_sign_up = self.api_client.sign_up(sign_up_data=test_user_data)

        assert response_sign_up.status_code == 201
        assert self.api_client.session.cookies.get_dict().get("sid") is not None
        user_id = response_sign_up.json().get("data").get("userId")

        response_sign_in = self.api_client.sign_in(email=test_user_data['email'], password=test_user_data['password'])

        assert response_sign_in.status_code == 200
        assert user_id == response_sign_in.json().get("data").get("userId")

        response_logout = self.api_client.log_out()

        assert response_logout.status_code == 200
        assert self.api_client.session.cookies.get_dict().get("sid") is None
