from typing import List
from core.domain.employee.entities import Employee
from core.domain.employee.repositories import EmployeeRepository


class EmployeeUseCases:

    def __init__(self, repository: EmployeeRepository) -> None:

        self._repository = repository

    def getAll(self) -> List[Employee]:

        return self._repository.getAll()

    def getById(self, id: int) -> Employee:

        employee = self._repository.findById(id)

        if employee is None:
            # Throw not found exception
            pass

        return employee

    def create(self, name: str, personal_code: str, work_code: str, birth_date: str) -> Employee:

        employee = Employee(name, personal_code, work_code, birth_date)

        return self._repository.create(employee)
