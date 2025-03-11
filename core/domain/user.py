# core/domain/user.py
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str
