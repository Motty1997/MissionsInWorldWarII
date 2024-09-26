from config.base import session_factory
from controllers.target_controller import target_blueprint
from models import Target, TargetType, City, Country, Location
from flask import Flask

def create_app():
    flask_app = Flask(__name__)
    return flask_app

if __name__ == '__main__':
    app = create_app()
    app.register_blueprint(target_blueprint, url_prefix="/api/target")
    app.run(debug=True)
