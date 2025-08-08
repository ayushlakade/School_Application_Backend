from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.logger import setup_logging
import logging
from db.services.Student_Service import StudentServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.get("/get_all_students")
def get_all_students(db:Session=Depends(get_db)):
    logger.info("Request Received to get all students info")
    student_info=StudentServiceManager.display_all_student_details(db)
    return_list=[]

    for student in student_info:
        student_data = {}
        student_data['student_id']=student.student_id
        student_data['student_name']=student.student_name
        student_data['student_email']=student.student_email
        return_list.append(student_data)


    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_students_by_name/{student_name}")
def get_students_by_id(student_name:str,db:Session=Depends(get_db)):
    logger.info("Request Received to get student by name : {0}".format(student_name))
    student_info=StudentServiceManager.display_student_details_by_name(db,student_name)

    return_list = []

    student_data = {}
    student_data['student_id'] = student_info.student_id
    student_data['student_name'] = student_info.student_name
    student_data['student_email'] = student_info.student_email
    return_list.append(student_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_students_by_id/{student_id}")
def get_students_by_id(student_id:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get student by id : {0}".format(student_id))
    student_info=StudentServiceManager.display_student_details_by_id(db,student_id)

    return_list = []
    student_data = {}
    student_data['student_id'] = student_info.student_id
    student_data['student_name'] = student_info.student_name
    student_data['student_email'] = student_info.student_email
    return_list.append(student_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )