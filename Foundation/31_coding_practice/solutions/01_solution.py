def validate_password(s):
    special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~"

    # Check if it contains the word "password"
    if "password" in s.lower():
        return "false"

    # Check password length
    if not (8 <= len(s) <= 30):
        return "false"

    # Check for at least one uppercase letter
    if not any(c.isupper() for c in s):
        return "false"

    # Check for at least one digit
    if not any(c.isdigit() for c in s):
        return "false"

    # Check for at least one special character
    if not any(c in special_chars for c in s):
        return "false"

    # If all checks passed
    return "true"
