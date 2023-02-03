from setup import app
from scripts.util.helper import getenv_bool
from scripts.routes.auth_routes import auth_routes
import os


def main():
    app.register_blueprint(auth_routes)

    app.run(
        debug=getenv_bool('DEBUG_MODE'),
        host=os.getenv('APP_HOST'),
        port=os.getenv('APP_PORT')
    )


if __name__ == '__main__':
    main()
