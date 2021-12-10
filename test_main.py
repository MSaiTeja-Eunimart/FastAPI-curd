from app.config.db import conn
from app.services.student import Student_service
import requests

# def addition(a,b):
#     c=a+b
#     return c

# def test_addition():
#     assert addition(5,5)==10

# def test_main_status():
#     res = requests.get("http://127.0.0.1:8000/")
#     assert res.status_code == 200
   
# def test_main_json():
#     res = requests.get("http://127.0.0.1:8000/")
#     assert res.json() == {"world":"hi"}

# def test_post_content_type():
#     res = requests.post("http://127.0.0.1:8000/")
#     assert res.headers["Content-Type"] == "application/json"

# def test_get_student_name_1():
#     res = requests.get("http://127.0.0.1:8000/student/1")
#     assert res.status_code == 200
#     res_body = res.json()
#     assert res_body[0]["id"] == 2

# def test_get_student_name_2():
#     res = requests.get("http://127.0.0.1:8000/student/2")
#     assert res.status_code == 200
#     res_body = res.json()
#     assert res_body[0]["student_name"] == "M Sai Teja"

# def test_check_connection():
#     assert conn

# def test_retrieve_data():
#     res = Student_service.list_student_service()
#     print(res)
#     assert res[0]["id"] == 2

# def test_retrieve_data_1():
#     res = Student_service.list_student_service()
#     print(res)
#     assert res[0]["student_name"]=="M Sai Teja"

# def test_get_by_id():
#     data=1
#     res = Student_service.get_by_studentid_service(data)
#     assert res[0]["id"]==1

# def test_delete_by_id():
#     data = 1
#     flag = 0
#     # res = Student_service.delete_student_id_service(data)
#     result_res = Student_service.list_student_service()
#     for i in result_res:
#         if(i[0] == data):
#             flag = 1
#             break
#     assert flag == 0


# def test_insert_student():
#     res = requests.get("http://127.0.0.1:8000/student")
#     assert res.status_code == 200

def test_check_student():
    res = requests.get("http://127.0.0.1:8000/student/1")
    assert res.status_code == 200
    res_body = res.json()
    print(res_body[0]["id"])
    assert res_body[0]["student_name"] == "M Sai Teja"

# def test_check_student_1():
#     res = requests.get("http://127.0.0.1:8000/student/1")
#     assert res.status_code == 200
#     res_body = res.json()
#     x=res_body[0]["id"]
#     assert x == 2

# def test_delete_student():
#     res = requests.get("http://127.0.0.1:8000/student/1")
#     assert (res.status_code) == 200


