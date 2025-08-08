from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import StaffBase1,StaffBase3,StaffBase,StaffBase4
from app.logger import setup_logging
import logging

from db.services.Staff_Services import StaffServiceManager
from db.services.Student_Service import StudentServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()



@router.patch("/update_staff_email_by_id")
def patch_update_staff_email(staff:StaffBase1,db:Session=Depends(get_db)):
    logger.info("Request Received to update staff email")
    staff_info=StaffServiceManager.update_staff_email_by_staff_id(db,staff.staff_id,staff.staff_email)
    if staff_info:
        return_list = []
        for staff in staff_info:
            staff_data = {}
            staff_data['staff_id'] = staff.staff_id
            staff_data['staff_name'] = staff.staff_name
            staff_data['staff_email'] = staff.staff_email
            staff_data['staff_designation'] = staff.staff_designation
            staff_data['staff_salary'] = staff.staff_salary
            staff_data['staff_mobile_no'] = staff.staff_mobile_no

            return_list.append(staff_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500, detail="Error in updating Staff email by id")



@router.patch("/update_staff_name_by_mobile_number")
def patch_update_staff_email_by_number(staff:StaffBase3,db:Session=Depends(get_db)):
    logger.info("Request Received to update staff email")
    staff_info=StaffServiceManager.update_staff_name_by_mobile_number(db,staff.staff_mobile_no,staff.staff_name)
    if staff_info:
        return_list = []
        for staff in staff_info:
            staff_data = {}
            staff_data['staff_id'] = staff.staff_id
            staff_data['staff_name'] = staff.staff_name
            staff_data['staff_email'] = staff.staff_email
            staff_data['staff_designation'] = staff.staff_designation
            staff_data['staff_salary'] = staff.staff_salary
            staff_data['staff_mobile_no'] = staff.staff_mobile_no

            return_list.append(staff_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    raise HTTPException(status_code=500, detail="Error in updating Staff name")

@router.patch("/update_staff_detail_by_mobile_number")
def patch_update_student_details(staff:StaffBase,db:Session=Depends(get_db)):
    logger.info("Request Received to update staff details")
    staff_info = StaffServiceManager.update_staff_details_by_mobile_number(db, staff.staff_name, staff.staff_email,staff.staff_designation,staff.staff_salary,staff.staff_mobile_no)
    if staff_info:
        return_list = []
        for staff in staff_info:
            staff_data = {}
            staff_data['staff_id'] = staff.staff_id
            staff_data['staff_name'] = staff.staff_name
            staff_data['staff_email'] = staff.staff_email
            staff_data['staff_designation'] = staff.staff_designation
            staff_data['staff_salary'] = staff.staff_salary
            staff_data['staff_mobile_no'] = staff.staff_mobile_no

            return_list.append(staff_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    raise HTTPException(status_code=500, detail="Error in updating Staff name")


@router.patch("/update_staff_detail_by_staff_id")
def patch_update_student_details_by_id(staff:StaffBase4,db:Session=Depends(get_db)):
    logger.info("Request Received to update staff details")
    staff_info = StaffServiceManager.update_staff_details_by_staff_id(db, staff.staff_id, staff.staff_name, staff.staff_email, staff.staff_designation, staff.staff_salary, staff.staff_mobile_no)
    if staff_info:
        return_list = []
        for staff in staff_info:
            staff_data = {}
            staff_data['staff_id'] = staff.staff_id
            staff_data['staff_name'] = staff.staff_name
            staff_data['staff_email'] = staff.staff_email
            staff_data['staff_designation'] = staff.staff_designation
            staff_data['staff_salary'] = staff.staff_salary
            staff_data['staff_mobile_no'] = staff.staff_mobile_no

            return_list.append(staff_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    raise HTTPException(status_code=500, detail="Error in updating Staff details")

@router.patch("/update_staff_detail_by_email_id")
def patch_update_student_details(staff:StaffBase,db:Session=Depends(get_db)):
    logger.info("Request Received to update staff details")
    staff_info = StaffServiceManager.update_staff_details_by_staff_email(db, staff.staff_name, staff.staff_email,staff.staff_designation,staff.staff_salary,staff.staff_mobile_no)
    if staff_info:
        return_list = []
        for staff in staff_info:
            staff_data = {}
            staff_data['staff_id'] = staff.staff_id
            staff_data['staff_name'] = staff.staff_name
            staff_data['staff_email'] = staff.staff_email
            staff_data['staff_designation'] = staff.staff_designation
            staff_data['staff_salary'] = staff.staff_salary
            staff_data['staff_mobile_no'] = staff.staff_mobile_no

            return_list.append(staff_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    raise HTTPException(status_code=500, detail="Error in updating Staff name")
