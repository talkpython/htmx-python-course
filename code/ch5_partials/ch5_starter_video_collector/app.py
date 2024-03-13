import sys

import flask

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

    # Python 3.12 has a new way to determine this,
    # see https://github.com/talkpython/htmx-python-course/issues/8#issuecomment-1990894657
    being_debugged = sys.gettrace() is not None
    being_debugged = being_debugged or sys.monitoring.get_tool(sys.monitoring.DEBUGGER_ID) is not None

    app.run(debug=being_debugged)
else:
    configure()
