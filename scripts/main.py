from setup import app, db
from scripts.util.helper import getenv_bool
from scripts.routes.auth_routes import auth_routes
from scripts.routes.authz_routes import authz_routes
import os


if __name__ == '__main__':
    db.create_all()

    app.register_blueprint(auth_routes)
    app.register_blueprint(authz_routes)

    app.run(
        debug=getenv_bool('DEBUG_MODE'),
        host=os.getenv('APP_HOST'),
        port=os.getenv('APP_PORT')
    )
