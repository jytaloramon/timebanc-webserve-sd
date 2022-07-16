from core.domain.employee.repositories import EmployeeRepository
from core.domain.schedule.repositories import ScheduleRepository


class Repositories:

    employee_repository = EmployeeRepository('./db/employee.json')
    schedule_repository = ScheduleRepository('./db/schedule.json')
