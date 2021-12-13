# import schedule
# import time
from app.services.student import Student_service

import threading
def schedule_db():
    print(Student_service.list_student_service())
    t= threading.Timer(5,schedule_db).start()

# def schedule_db1():
#     print(Student_service.root())
#     t1= threading.Timer(1,schedule_db1).start()