def check_security_level(access_level):
    if not isinstance(access_level, str):
        raise ValueError("Access level must be a string")
    return f"Security level: {access_level.upper()}"


print(check_security_level("high"))  