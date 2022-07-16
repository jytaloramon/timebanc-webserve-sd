from flask import Blueprint

from app.routes.employeerouter import employee_route
from app.routes.schedulerouter import schedule_router


api_routes = Blueprint('api', __name__, url_prefix='/api')
api_routes.register_blueprint(employee_route)
api_routes.register_blueprint(schedule_router)
