
from datetime import datetime
from typing import List, Tuple
from core.commom.exceptions import NotFoundError
from core.commom.repositoriesinstance import Repositories
from core.domain.schedule.entities import Schedule
from core.domain.schedule.repositories import ScheduleRepository
from core.domain.employee.entities import Employee


class ScheduleUseCases:

    def __init__(self, repository: ScheduleRepository) -> None:

        self._repository = repository

    def get_all(self) -> List[Schedule]:

        d = []
        for i in self._repository.get_all():
            s = Schedule(i._moment, i._event_type, i._employee_id)
            s._id = i._id
            s._employee_id = Repositories.employee_repository.find_by_id(
                s._employee_id).entity_dump()
            d.append(s)

        return d

    def get_by_Id(self, id: int) -> Schedule:

        schedule = self._repository.find_by_id(id)

        if schedule is None:
            raise NotFoundError('Schedule ID not exist.')

        return schedule

    def get_all_by_employee(self, id: int) -> Tuple[Employee, List[Schedule]]:

        d = []
        for i in self._repository.get_all_by_employee_id(id):
            s = Schedule(i._moment, i._event_type, i._employee_id)
            s._id = i._id
            d.append(s)

        return Repositories.employee_repository.find_by_id(id),  d

    def create(self, moment: str, event_type: int, employee_id: int) -> Schedule:

        employee = Repositories.employee_repository.find_by_id(employee_id)

        if employee is None:
            raise NotFoundError('Employee ID not exist.')

        moment_date = datetime.strptime(moment, '%Y-%m-%d %H:%M')

        schedule = Schedule(moment_date, event_type, employee_id)

        self._repository.create(schedule)

        new_schedule = Schedule(
            schedule._moment, schedule._event_type, schedule._employee_id)
        new_schedule._employee_id = employee.entity_dump()

        return new_schedule
