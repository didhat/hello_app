import os
from typing import Final

import dotenv

dotenv.load_dotenv()

secret_name: Final = os.environ.get("SECRET_NAME", default="dan")


def get_secret_name():
    return secret_name
