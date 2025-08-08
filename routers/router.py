from fastapi import APIRouter


from routers.staff import post_staffs,get_staffs,update_staffs,delete_staffs
from routers.student import get_students,post_students,update_students,delete_students
from routers.fees import get_fees,post_fees,update_fees,delete_fees
from routers.course import get_courses,post_courses,update_courses,delete_courses
from routers.academic import get_academics,post_academics,update_academics,delete_academics


api_router=APIRouter()
api_router.include_router(get_students.router,prefix="/student",tags=["Student"])
api_router.include_router(post_students.router,prefix="/student",tags=["Student"])
api_router.include_router(update_students.router,prefix="/student",tags=["Student"])
api_router.include_router(delete_students.router,prefix="/student",tags=["Student"])
api_router.include_router(get_staffs.router,prefix="/staff",tags=["Staff"])
api_router.include_router(post_staffs.router,prefix="/staff",tags=["Staff"])
api_router.include_router(update_staffs.router,prefix="/staff",tags=["Staff"])
api_router.include_router(delete_staffs.router,prefix="/staff",tags=["Staff"])
api_router.include_router(get_fees.router,prefix="/fees",tags=["Fees"])
api_router.include_router(post_fees.router,prefix="/fees",tags=["Fees"])
api_router.include_router(update_fees.router,prefix="/fees",tags=["Fees"])
api_router.include_router(delete_fees.router,prefix="/fees",tags=["Fees"])
api_router.include_router(get_courses.router,prefix="/course",tags=["Course"])
api_router.include_router(post_courses.router,prefix="/course",tags=["Course"])
api_router.include_router(update_courses.router,prefix="/course",tags=["Course"])
api_router.include_router(delete_courses.router,prefix="/course",tags=["Course"])
api_router.include_router(get_academics.router,prefix="/academic",tags=["Academic"])
api_router.include_router(post_academics.router,prefix="/academic",tags=["Academic"])
api_router.include_router(update_academics.router,prefix="/academic",tags=["Academic"])
api_router.include_router(delete_academics.router,prefix="/academic",tags=["Academic"])