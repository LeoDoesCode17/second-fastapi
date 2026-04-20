from app.repositories import tech_respository
from app.exceptions.tech_exceptions import CreateTechFailException, FetchAllTechFailException

def create_tech(data: dict):
    try:
        response =  tech_respository.create(data=data)

        if not response.data:
            raise Exception("Failed when create a tech: empty data field")
        
        return response.data[0]
    except Exception as e:
        raise e

def get_all_techs():
    try:
        response = tech_respository.get()

        if not response.data:
            raise Exception("Failed to get all techs: empty data field")
        
        return response.data
    except Exception as e:
        raise e

def update_tech(id: int, data: dict):
    try:
        response = tech_respository.update(id=id, data=data)
        if not response.data:
            raise Exception("Failed to update tech: empty data field")
        return response.data[0]
    except Exception as e:
        raise e
    
