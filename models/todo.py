from pydantic import BaseModel

class ToDo ( BaseModel) : 
    name : str 
    decription : str 
    complete : bool