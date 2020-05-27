import os

from flask import Flask
from flaskr.background.routes import background
from flaskr.links.routes import links
from flaskr.logo.routes import logo

def app_factory(test_config=None):
    """
    create and configure the app
    :param test_config: param for application test configuration
    :return: object
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Blueprints
    app.register_blueprint(background)
    app.register_blueprint(links)
    app.register_blueprint(logo)


    @app.route('/api')
    def hello():
        return 'Opa! Me achou!'

    return app