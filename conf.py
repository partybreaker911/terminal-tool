import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.environ.get('TOKEN')
IRC_SERVER = os.environ.get('IRC_SERVER')
IRC_PORT = os.environ.get('IRC_PORT')
IRC_CHANNEL = os.environ.get('IRC_CHANNEL')
IRC_NICKNAME = os.environ.get('NICKNAME')
