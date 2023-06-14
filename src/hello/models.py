import dataclasses as dt


@dt.dataclass
class SecretAnswer:
    secret: str
    name: str

    def to_user(self):
        return {
            "text": f"You secret user, this is your secret code {self.secret} for something interesting"
        }


@dt.dataclass
class BasicHello:
    name: str

    def to_user(self):
        return {"text": f"Hello user with name - {self.name}"}
