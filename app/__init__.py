from flask import Flask
from app.routes.routes import api_routes

app = Flask('apiflask')

app.register_blueprint(api_routes)
