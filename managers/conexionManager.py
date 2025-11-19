import psycopg
import os
from dotenv import load_dotenv

load_dotenv() 

class ConexionManager:
    def __init__(self):
        self.db_url = os.getenv('URLDATABASE')
        pass
    
    def get_connection(self):
        conn = psycopg.connect(self.db_url)
        return conn