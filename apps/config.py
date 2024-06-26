from pathlib import Path

basedir = Path(__file__).parent.parent

# BaseConfig 클래스 작성하기
class BaseConfig:
  SECRET_KEY = 'qpdltmzhsvlrmcfg'
  WTF_CSRF_SECRET_KEY = 'dlrjtdmsdhktejvjzwtf'

#BaseConfig 클래스를 상속하여 LocalConfig 클래스를 작성하기
class LocalConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'localsqlite'}"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True

#BaseConfig 클래스를 상속하여 TestingConfig 클래스를 작성하기
class TestingConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'localsqlite'}"
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  WTF_CSRF_ENABLED = False

#config 사전에 매핑한다
config = {
  'testing': TestingConfig,
  'local' : LocalConfig,
}
