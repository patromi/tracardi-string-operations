from pydantic import BaseModel


class Configuration(BaseModel):
    operation: str
    string: str



