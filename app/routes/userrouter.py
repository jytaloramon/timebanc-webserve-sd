from flask import Blueprint, request
from app.routes.statuscode import StatusCode
from core.commom.exceptions import Conflit, NotFoundError
from core.commom.repositoriesinstance import Repositories

from core.domain.employee.usecases import EmployeeUseCases

user_route = Blueprint('employee', __name__, url_prefix='/employee')

user_use_case = EmployeeUseCases(Repositories.employee_repository)


@user_route.route('/', methods=['GET', 'POST'])
def user_base():

    if request.method == 'GET':
        return {'employees': list(map(lambda x: x.entity_dump(), user_use_case.get_all()))}

    if request.method == 'POST':
        data = request.get_json()

        try:
            return user_use_case.create(
                data['name'], data['personal_code'], data['work_code'], data['birth_date']
            ).entity_dump()
        except Conflit as e:
            return {'msg': e.args[0]}, StatusCode.CONFLIT.value


@user_route.route('/<int:id>', methods=['GET'])
def user_base_id(id: int):

    if request.method == 'GET':

        try:
            return user_use_case.get_by_Id(id).entity_dump()
        except NotFoundError as e:
            return {'msg': e.args[0]}, StatusCode.NOTFOUND.value
