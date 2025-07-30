def to_uppercase(s):
    return s.upper()

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]
