from flask import Blueprint, request

schedule_router = Blueprint('schedule', __name__, url_prefix='/schedule')


@schedule_router.route('/', methods=['GET', 'POST'])
def schedule_base():

    if request.method == 'GET':
        return {'GDHFFD': 'FDFDF'}

    if request.method == 'POST':
        pass
