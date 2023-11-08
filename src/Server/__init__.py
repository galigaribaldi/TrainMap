from flask import Flask

###Routes configurations
app = Flask(__name__)
#app.config.from_object('configuration.DevelopmentConfig')

####Register Endpoints
from src.Server.endpoints.view import endP1
app.register_blueprint(endP1)
