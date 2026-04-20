# app/services/image_service.py
from app.repositories import image_repository

def create_image(data: dict):
    try:
        create_response = image_repository.create(data=data)
        if not create_response.data:
            raise Exception("CREATE: Failed to create a new image row")
        return create_response.data[0]
    except Exception as e:
        raise e
    
def get_all_images():
    try:
        get_response = image_repository.get()
        if not get_response.data:
            raise Exception("GET: Failed to get all images")
        return get_response.data
    except Exception as e:
        raise e