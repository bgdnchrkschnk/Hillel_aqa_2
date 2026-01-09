from faker import Faker
fake = Faker()


def get_sign_up_data() -> dict:
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    data = {
        "name": fake.first_name(),
        "lastName": fake.last_name_female(),
        "email": fake.safe_email(),
        "password": password,
        "repeatPassword": password
    }
    return data