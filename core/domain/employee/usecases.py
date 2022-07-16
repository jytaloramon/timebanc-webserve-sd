from typing import List
from core.commom.exceptions import Conflit, NotFoundError
from core.domain.employee.entities import Employee
from core.domain.employee.repositories import EmployeeRepository


class EmployeeUseCases:

    def __init__(self, repository: EmployeeRepository) -> None:

        self._repository = repository

    def get_all(self) -> List[Employee]:

        return self._repository.get_all()

    def get_by_Id(self, id: int) -> Employee:

        employee = self._repository.find_by_id(id)

        if employee is None:
            raise NotFoundError('Employee ID not exist.')

        return employee

    def create(self, name: str, personal_code: str, work_code: str, birth_date: str) -> Employee:

        if self._repository.find_by_work_code(work_code) is not None:
            raise Conflit('work_code already exists')

        if self._repository.find_by_personal_code(personal_code) is not None:
            raise Conflit('personal_code already exists')

        employee = Employee(name, personal_code, work_code, birth_date)

        return self._repository.create(employee)
