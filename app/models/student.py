from pydantic.utils import ClassAttribute
from sqlalchemy import Table, Column, String, Integer
from app.config.db import meta
from app.schema.student import BaseModel

students = Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('student_name',String(200)),
    Column('student_email',String(200))
)
