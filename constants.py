from dotenv import load_dotenv
import os
load_dotenv()



SERVER_URL = 'localhost'
PORT = 8000
ENV = 'development'  # Options: 'development', 'production', 'testing'
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')