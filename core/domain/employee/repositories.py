from typing import List
from core.commom.repository import RepositoryBase
from core.domain.employee.entities import Employee


class EmployeeRepository(RepositoryBase):

    def __init__(self) -> None:
        super().__init__()

    def get_all(self) -> List[Employee]:
        return list(self._data.values())

    def find_by_id(self, id: int) -> Employee | None:
        return self._data.get(id)

    def find_by_work_code(self, work_code: str) -> Employee | None:
        employee_filtered = list(
            filter(lambda x: x._work_code == work_code, self._data.values())
        )

        return employee_filtered[0] if len(employee_filtered) > 0 else None

    def find_by_personal_code(self, personal_code: str) -> Employee | None:
        employee_filtered = list(
            filter(lambda x: x._personal_code ==
                   personal_code, self._data.values())
        )

        return employee_filtered[0] if len(employee_filtered) > 0 else None

    def create(self, emp: Employee) -> Employee:

        emp._id = self.get_v_auto_increment()
        self._data[emp._id] = emp

        return emp
