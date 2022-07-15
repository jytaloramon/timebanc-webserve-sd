from typing import List
from core.commom.repository import RepositoryBase
from core.domain.employee.entities import Employee


class EmployeeRepository(RepositoryBase):

    def __init__(self) -> None:
        super().__init__()

    def getAll(self) -> List[Employee]:

        return list(self._data.values())

    def findById(self, id: int) -> Employee | None:

        return self._data.get(id)

    def create(self, emp: Employee) -> Employee:

        emp._id = self.get_v_auto_increment()
        self._data[emp._id] = emp

        return emp
