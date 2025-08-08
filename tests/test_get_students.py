import sys
import os
from http.client import responses

from fastapi.testclient import TestClient
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)


def test_get_all_students():
    response=client.get("/student/get_all_students")
    assert  response.status_code == 200
    data=response.json()
    assert "message" in data

def test_get_students_by_name():
    response = client.get("/student/get_students_by_name/Ayush Lakade")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_get_students_by_id():
    response = client.get("student/get_students_by_id/1")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_insert_student():
    response = client.post("student/insert_student_record",json={
    "student_name":"Ayush sharma2",
    "student_email":"ayushsharma6229@gmail.com"
})
    assert response.status_code == 201
    data = response.json()
    assert "message" in data

def test_patch_update_student_record():
    response = client.patch("student/update_student_email_id_by_name",json={
        "student_name": "Ayush lakade",
        "student_email": "ayushlakade7@gmail.com"

    })
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

# def test_patch_update_student_record_by_id():
#     response = client.patch("student/update_student_name_by_email_id",json={
#         "student_name": "omkar dattakumar umbarkar",
#         "student_email": "oumbarkar77@gmail.com"
#
#     })
#     assert response.status_code == 200
#     data = response.json()
#     assert "message" in data