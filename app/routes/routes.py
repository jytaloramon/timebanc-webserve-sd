from flask import Blueprint

from app.routes.userrouter import user_route
from app.routes.schedulerouter import schedule_router


api_routes = Blueprint('api', __name__, url_prefix='/api')
api_routes.register_blueprint(user_route)
api_routes.register_blueprint(schedule_router)

