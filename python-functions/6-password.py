def validate_password(password):
    is_password_valid = False

    # minimum length check
    if len(password) >= 8:
        is_password_valid = True
    else:
        return False

    # uppercase, lowercase digit and spaces check
    has_uppercase_letter = False
    has_lowercase_letter = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase_letter = True

        if char.islower():
            has_lowercase_letter = True

        try:
            int(char)
            has_digit = True
        except ValueError:
            pass

        if char == " ":
            return False

    if has_uppercase_letter and has_lowercase_letter and has_digit:
        is_password_valid = True
    else:
        return False

    return is_password_valid
