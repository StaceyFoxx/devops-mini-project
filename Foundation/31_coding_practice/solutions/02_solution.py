def valid_email(s):
    if s.count('@') != 1:
        return False

    parts = s.split('@')
    if not parts[0] or not parts[1]:
        return False

    return '.' in parts[1]

