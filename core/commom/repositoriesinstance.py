from core.domain.employee.entities import Employee
from core.domain.employee.repositories import EmployeeRepository
from core.domain.schedule.repositories import ScheduleRepository


class Repositories:

    employee_repository = EmployeeRepository()
    schedule_repository = ScheduleRepository()
