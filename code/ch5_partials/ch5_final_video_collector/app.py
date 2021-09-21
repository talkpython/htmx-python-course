import sys

import flask
import jinja_partials

from services import video_service

app = flask.Flask("app")


def configure():
    print("Configuring Flask app:")

    register_template_ops()
    print("Registered template helpers")

    register_blueprints()
    print("Registered blueprints")

    setup_db()
    print("DB setup completed.")
    print("", flush=True)


def register_template_ops():
    jinja_partials.register_extensions(app)
    helpers = {
        'len': len,
        'isinstance': isinstance,
        'str': str,
        'type': type
    }
    app.jinja_env.globals.update(**helpers)


def register_blueprints():
    from views import home
    from views import videos
    from views import feed

    app.register_blueprint(home.blueprint)
    app.register_blueprint(videos.blueprint)
    app.register_blueprint(feed.blueprint)


def setup_db():
    video_service.load_data()


if __name__ == '__main__':
    configure()
    being_debugged = sys.gettrace() is not None
    app.run(debug=being_debugged)
else:
    configure()
