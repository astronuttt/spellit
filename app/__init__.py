from flask import Flask
from config import config




def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
