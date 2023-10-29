from pydantic import BaseModel

#class Program(BaseModel):


class Programs(BaseModel):
    terminal: str
    browser: str
    browser_incognito: str
