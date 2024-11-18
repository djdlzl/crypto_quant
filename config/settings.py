from dotenv import load_dotenv
import os

load_dotenv()

# Upbit API 설정
UPBIT_ACCESS_KEY = os.environ.get('AccessKey')
UPBIT_SECRET_KEY = os.environ.get('SecretKey')
UPBIT_SERVER_URL = os.environ.get('Base_URL')