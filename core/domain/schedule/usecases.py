
from datetime import datetime
from typing import List
from core.commom.exceptions import NotFoundError
from core.commom.repositoriesinstance import Repositories
from core.domain.schedule.entities import Schedule
from core.domain.schedule.repositories import ScheduleRepository
from core.domain.employee.entities import Employee


class ScheduleUseCases:

    def __init__(self, repository: ScheduleRepository) -> None:

        self._repository = repository

    def get_all(self) -> List[Schedule]:

        return self._repository.get_all()

    def get_by_Id(self, id: int) -> Schedule:

        schedule = self._repository.find_by_id(id)

        if schedule is None:
            # Throw not found exception
            pass

        return schedule

    def create(self, moment: str, event_type: int, employee_id: int) -> Schedule:

        employee = Repositories.employee_repository.find_by_id(employee_id)

        if employee is None:
            raise NotFoundError('Employee ID not exist.')

        moment_date = datetime.strptime(moment, '%Y-%m-%d %H:%M')

        employee = Schedule(moment_date, event_type, employee_id)

        return self._repository.create(employee)
