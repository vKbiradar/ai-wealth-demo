from dataclasses import dataclass


@dataclass(frozen=True)
class AdminCredentials:
    username: str
    password: str


ADMIN_CREDENTIALS = AdminCredentials(username="admin", password="admin123")


def authenticate_admin(username: str, password: str) -> bool:
    return (
        username.strip().lower() == ADMIN_CREDENTIALS.username.lower()
        and password == ADMIN_CREDENTIALS.password
    )
