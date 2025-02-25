import secrets

from jinja2.ext import Extension


# taken from Django
# https://github.com/django/django/blob/main/django/core/managemet/utils.py

RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    """
    Return a securely generated random string.

    The bit length of the returned value can be calculated with the formula:
        log_2(len(allowed_chars)^length)

    For example, with default `allowed_chars` (26+26+10), this gives:
      * length: 12, bit length =~ 71 bits
      * length: 22, bit length =~ 131 bits
    """
    return "".join(secrets.choice(allowed_chars) for i in range(length))

def random_secret_key(length=50):
    """
    Return a 50 character random string usable as a SECRET_KEY setting value.
    """
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return random_string(length, chars)


class DjangoExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["random_string"] = random_string
        environment.filters["random_secret_key"] = random_secret_key
