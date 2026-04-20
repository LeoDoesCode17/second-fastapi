from app.exceptions.base import AppException

class DuplicateTechSlugException(AppException):
    pass

class CreateTechFailException(AppException):
    pass

class FetchAllTechFailException(AppException):
    pass

class UpdateTechFailException(AppException):
    pass