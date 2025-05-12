import os
from dotenv import load_dotenv

load_dotenv()


class Credential:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")