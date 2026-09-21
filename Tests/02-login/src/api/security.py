import jwt

from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()

SECRET_KEY = "change-this-later"
ALGORITHM = "HS256"


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return password_hash.verify(
        plain_password,
        hashed_password
    )


def hash_password(password: str) -> str:

    return password_hash.hash(password)


def create_access_token(username: str) -> str:

    payload = {
        "sub": username
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token