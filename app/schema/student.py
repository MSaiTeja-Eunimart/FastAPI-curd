from pydantic import BaseModel

class Student(BaseModel):
    id:int
    student_name:str
    student_email:str