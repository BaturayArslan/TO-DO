from dataclasses import dataclass


@dataclass
class GetUserRequest:
    username: str
    password: str
  