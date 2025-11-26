class AccessDeniedAgeError(Exception):
    ...

age = 17

if age < 18:
    raise AccessDeniedAgeError(f"Reason: age - {age}")
else:
    print("You are welcome!")