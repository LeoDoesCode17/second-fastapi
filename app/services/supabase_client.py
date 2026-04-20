# app/services/supabase_client.py
from app.core import config

from supabase import create_client, Client

supabase: Client = create_client(
    config.DATABASE_URL,
    config.DATABASE_KEY
)