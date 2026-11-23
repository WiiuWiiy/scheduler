import os
from dotenv import load_dotenv

load_dotenv()
DEV_ID = int(os.getenv("id"))
TOKEN = os.getenv("key")


def getid() -> int:
	return DEV_ID


def gettoken() -> str:
	info = TOKEN
	return info
