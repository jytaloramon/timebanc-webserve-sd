from typing import Any, Dict, List, Tuple
from core.commom.repository import RepositoryBase
from core.domain.employee.entities import Employee


class EmployeeRepository(RepositoryBase):

    def __init__(self, dbfile_name: str) -> None:
        super().__init__(dbfile_name)

    def _deserializable(self, data: dict[str, Any]) -> Any:

        employee = Employee(
            data['name'], data['personal_code'], data['work_code'], data['birth_date'])
        employee._id = data['id']

        return employee

    def _serializable_to_save(self, data: Any) -> Tuple[int, Dict[str, any]]:

        return (data._id, data.entity_dump())

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
        self.set_new_data(emp._id, emp)

        return emp
