from dotenv import load_dotenv
from os import getenv

load_dotenv()

DATABASE_URL = getenv('SUPABASE_URL')
DATABASE_KEY = getenv('SUPABASE_KEY')
DATABASE_JWT_KEY = getenv('SUPABASE_JWT_KEY')
