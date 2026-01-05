import os

from sqlalchemy import Column, Integer, String, ForeignKey
from lesson_23.declarative_base import Base
from sqlalchemy.orm import relationship

from lesson_23.sqlalchemy_client import SqlAlchemyClient
from dotenv import load_dotenv
load_dotenv()


# Визначення моделей даних (таблиць) за допомогою класів
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department", back_populates="employees")


if __name__ == '__main__':
    db_url = os.getenv("DB_URL")

    client = SqlAlchemyClient(db_url=db_url)
    client.create_table(table_model=Employee)
    client.create_table(table_model=Department)

    it_department = Department(name="IT")
    hr_department = Department(name="HR")
    client.session.add_all([it_department, hr_department])
    client.session.commit()

    john = Employee(name="John", department_id=it_department.id)
    alice = Employee(name="Alice", department_id=hr_department.id)
    client.session.add_all([john, alice])


    client.session.commit()


    client.close_connection()
