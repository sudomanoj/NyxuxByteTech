class CustomError(Exception):
    def __init__(self):
        super.__init__()
        
    def id_exception(self, id):
        if id < 0:
            raise NegativeIdException("Print ID can't be a negative value!")
        
class NegativeIdException(Exception):
    pass