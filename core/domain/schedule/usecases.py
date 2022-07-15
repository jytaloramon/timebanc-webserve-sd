
from datetime import datetime
from typing import List
from core.domain.schedule.entities import Schedule
from core.domain.schedule.repositories import ScheduleRepository
from core.domain.employee.entities import Employee


class ScheduleUseCases:

    def __init__(self, repository: ScheduleRepository) -> None:

        self._repository = repository

    def getAll(self) -> List[Schedule]:

        return self._repository.getAll()

    def getById(self, id: int) -> Schedule:

        schedule = self._repository.findById(id)

        if schedule is None:
            # Throw not found exception
            pass

        return schedule

    def create(self, moment: str, event_type: int, employee_id: int) -> Schedule:

        employee = Employee()
        employee._id = employee_id

        moment_date = datetime.strptime(moment)

        employee = Schedule(moment_date, event_type, employee)

        return self._repository.create(employee)
