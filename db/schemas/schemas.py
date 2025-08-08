from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    student_name:str
    student_email:str

class FeesBase(BaseModel):
    student_id:int
    student_name:str
    student_total_fees :int
    student_balance_fees : int

class FeeUpdateRequest(BaseModel):
    student_id: int
    amount_paid: int
    new_total_fees: Optional[int] = None

class DeleteStudentBase(BaseModel):
    student_email:str

class DeleteStudentBase4(BaseModel):
    student_name:str

class DeleteStudentBase2(BaseModel):
    student_name:str

class DeleteStudentBase3(BaseModel):
    student_id:int

class CourseBase(BaseModel):
    course_code : int
    course_name : str
    course_fees : int
    course_number_of_student : int

class FeePayment(BaseModel):
    student_id: int
    #student_name: str
    amount_paid: int

class FeePayment2(BaseModel):
    #student_id: int
    student_name: str
    amount_paid: int

class StaffBase(BaseModel):
    staff_name : str
    staff_email : str
    staff_designation : str
    staff_salary : int
    staff_mobile_no : int

class UpdateCourse(BaseModel):
    course_code : int
    course_fees : int

class UpdateCourse2(BaseModel):
    course_code : int
    course_name : str

class UpdateCourse3(BaseModel):
    course_code : int
    course_number_of_student : int

class DeleteCourse(BaseModel):
    course_code:int

class DeleteCourse2(BaseModel):
    course_name:str

class StaffBase1(BaseModel):
    staff_id : int
    staff_email : str

class StaffBase2(BaseModel):
    staff_email : str
    staff_mobile_no : int

class StaffBase3(BaseModel):
    staff_name : str
    staff_mobile_no : int

class StaffBase4(BaseModel):
    staff_id : int
    staff_name : str
    staff_email : str
    staff_designation : str
    staff_salary : int
    staff_mobile_no : int

class DeleteStaff(BaseModel):
    staff_email : str

class DeleteStaff2(BaseModel):
    staff_name : str

class DeleteStaff3(BaseModel):
    staff_id : int

class AcademicBase(BaseModel):
    academic_id : int
    student_id : int
    course_id : int
    academic_year : str
    grade : str
    remarks : str
    enrollment_date : str

class DeleteAcademic(BaseModel):
    academic_year : str


class DeleteAcademic2(BaseModel):
    academic_id : int