from logging import error
from fastapi import APIRouter
from requests import status_codes
from app.config.db import conn
from app.models.index import students
from app.schema.index import Student
from app.services.student import Student_service

route = APIRouter(
    prefix='/student',
    tags=['Student']
)
@route.get("/")
def list_student():
    try:
        return Student_service.list_student_service()
    except:
        return {"Ntg":"Present"}

@route.get("/{id}")
def get_by_studentid(id: int):
    if(len(Student_service.get_by_studentid_service(id))==0):
        return {"Error":"Enter the valid id"}
    return Student_service.get_by_studentid_service(id)

@route.post("/")
def add_student(student: Student):
    conn.execute(students.insert().values(
        id=student.id,
        student_name=student.student_name,
        student_email=student.student_email
    ))
    return conn.execute(students.select()).fetchall()

@route.put("/{id}")
def edit_student_id(id:int, student: Student):
    return Student_service.add_student_service(id,student)

@route.delete("/{id}")
def delete_student_id(id:int):
    try:
        return Student_service.delete_student_id_service(id)
    except(error):
        return {"msg":error}
