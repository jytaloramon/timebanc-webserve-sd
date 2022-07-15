from flask import Blueprint, request
from core.commom.repositoriesinstance import Repositories

from core.domain.employee.usecases import EmployeeUseCases

user_route = Blueprint('employee', __name__, url_prefix='/employee')

user_usecase = EmployeeUseCases(Repositories.employee_repository)


@user_route.route('/', methods=['GET', 'POST'])
def user_base():

    if request.method == 'GET':
        return {'data': list(map(lambda x: x.entity_dump(), user_usecase.getAll()))}

    if request.method == 'POST':
        data = request.get_json()

        return user_usecase.create(
            data['name'], data['personalcode'], data['workcode'], data['birthdate']).entity_dump()
