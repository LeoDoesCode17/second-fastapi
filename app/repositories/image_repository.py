from app.services.supabase_client import supabase
TABLE_NAME = 'images'

def create(data: dict):
    response = supabase.table(TABLE_NAME).insert(data).execute()
    return response

def get():
    response = supabase.table(TABLE_NAME).select("*").execute()
    return response

def update(id: int, data: dict):
    response = supabase.table(TABLE_NAME).update(data).eq('id', id).execute()
    return response 