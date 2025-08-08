from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from db import Base
class StudentManager(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String(20), unique=True, index=True)  # added unique=True
    student_email = Column(String(50), unique=True)

class CourseManager(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True)
    course_code = Column(Integer, unique=True)
    course_name = Column(String(70))
    course_fees = Column(Integer)
    course_number_of_student = Column(Integer)


class StaffManager(Base):
    __tablename__ = 'staffs'
    staff_id = Column(Integer, primary_key=True)
    staff_name = Column(String(20))
    staff_email = Column(String(40))
    staff_designation = Column(String(40))
    staff_salary = Column(Integer)
    staff_mobile_no = Column(BigInteger)

class FeesManager(Base):
    __tablename__ = 'fees'
    student_id = Column(Integer, ForeignKey('students.student_id'), primary_key=True)
    student_name = Column(String(20))  # foreign key by name
    student_total_fees = Column(Integer)
    student_balance_fees = Column(Integer)

class AcademicManager(Base):
    __tablename__ = 'academic'
    academic_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.course_id'), nullable=False)
    academic_year = Column(String(20), nullable=True)  # e.g. "2024-25"
    grade = Column(String(10), nullable=True)  # e.g., "A", "B+", "Pass", "Fail"
    remarks = Column(String(150), nullable=True)  # (optional, comments)
    enrollment_date = Column(String(20), nullable=True)  # or Date column if using SQLAlchemy's Date
