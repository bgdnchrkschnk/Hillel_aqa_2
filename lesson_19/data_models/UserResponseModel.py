from pydantic import BaseModel

class UserResponseModel(BaseModel):
    id: int
    name: str
    email: str
    gender: str
    status: str




if __name__ == "__main__":
    test_data = {'id': 8306866, 'name': 'Michael Jimenez', 'email': 'plarsen@example.net', 'gender': 'male',
                 'status': 'active'}
    UserResponseModel.model_validate(test_data)