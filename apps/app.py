from pathlib import Path # 경로 처리를 위한 기본 라이브러리
from flask import Flask 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
from flask_login import LoginManager

db = SQLAlchemy()
csrf = CSRFProtect()

login_manger = LoginManager()
login_manger.login_view = 'auth.signup'
login_manger.login_message = ''


def create_app(config_key):

    app = Flask(__name__)

    app.config.from_object(config[config_key])

    app.config.from_mapping(
        SECRET_KEY="sksms12qkqh34dpdy",
        SQLALCHEMY_DATABASE_URI=
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KET = 'dianwlrp2ajrdjeiemld1'
    )

    db.init_app(app)
    csrf.init_app(app)

    Migrate(app, db)

    login_manger.init_app(app)

    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix="/auth")


    return app