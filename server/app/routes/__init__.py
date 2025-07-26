# registration of all routes will be done down here

# models routes
# from .auth_routes import auth_blue_print
from .umuganda_routes import umuganda_blue_print
from .user_routes import user_blue_print
from .attendance_routes import attendance_blue_print
from .fine_routes import fine_blue_print
from .payment_routes import payment_blue_print

# main UI
from .main_routes import home_blue_print
from .main_routes import app_blue_print

# dashboard
from .dashboard_routes import dashboard_blue_print

# testing routes
from .test_env import env_variables_blue_print # testing  the env variables
from .debug import debug_blue_print # testing  the db data
from .test_home import test_home_blue_print # testing  the UI 

def register_routes(app):

    # for models
    # app.register_blueprint(auth_blue_print, url_prefix='/auth') # this created confusion hence removed
    app.register_blueprint(umuganda_blue_print, url_prefix='/umuganda')
    app.register_blueprint(attendance_blue_print, url_prefix='/attendance')
    app.register_blueprint(user_blue_print, url_prefix='/user')
    app.register_blueprint(fine_blue_print, url_prefix='/fine')
    app.register_blueprint(payment_blue_print, url_prefix='/payment')

    # for app
    app.register_blueprint(home_blue_print)
    app.register_blueprint(app_blue_print, url_prefix='/app')

    # for dashboards
    app.register_blueprint(dashboard_blue_print, url_prefix='/dashboard')
    
    # for testing
    app.register_blueprint(env_variables_blue_print)
    app.register_blueprint(debug_blue_print)
    app.register_blueprint(test_home_blue_print)
