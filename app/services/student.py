from app.models.index import students
from app.schema.index import Student
from app.config.db import conn

class Student_service():
    def list_student_service():
        return conn.execute(students.select()).fetchall()

    def get_by_studentid_service(id):
        return conn.execute(students.select().where(students.c.id == id)).fetchall()
    
    def add_student_service(id,student):
        conn.execute(students.update().values(
            student_name=student.name,
            student_email=student.email
            ).where(students.id == id))
        return conn.execute(students.select()).fetechall()

    def delete_student_id_service(id):
        conn.execute(students.delete().where(students.c.id == id))
        return "Student by "+ str(id) +" deleted"