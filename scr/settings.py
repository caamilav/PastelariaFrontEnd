from dotenv import load_dotenv, find_dotenv
import os

# localiza o arquivo de .env
dotenv_file = find_dotenv()

# Carrega o arquivo .env
load_dotenv(dotenv_file)

# Configurações da APP
HOST  = os.getenv("HOST")
PORT  = os.getenv("PORT")
DEBUG = os.getenv("DEBUG")