from flask import Blueprint, request
from app.routes.statuscode import StatusCode
from core.commom.exceptions import NotFoundError
from core.commom.repositoriesinstance import Repositories

from core.domain.schedule.usecases import ScheduleUseCases

schedule_router = Blueprint('schedule', __name__, url_prefix='/schedule')

schedule_use_case = ScheduleUseCases(Repositories.schedule_repository)


@schedule_router.route('/', methods=['GET', 'POST'])
def schedule_base():

    if request.method == 'GET':
        return {'schedules': list(map(lambda x: x.entity_dump(), schedule_use_case.get_all()))}

    if request.method == 'POST':
        data = request.get_json()

        try:
            return schedule_use_case.create(
                data['moment'], data['event_type'], data['employee_id']
            ).entity_dump(), StatusCode.OK.value
        except NotFoundError as e:
            return {'msg': e.args[0]}, StatusCode.NOTFOUND.value
