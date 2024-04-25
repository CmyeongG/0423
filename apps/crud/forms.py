from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
# wtforms.validators : 유효성 검증 관련 모듈
# DataRequired : 값이 필수로 필요한 필드

class UserForm(FlaskForm):
  #사용자 폼의 username속성의 라벨과 검증을 설정
  username = StringField(
    '사용자명',
    validators=[
      DataRequired(message='사용자명은 필수입니다. '),
      Length(max=30, message='30문자 이내로 입력해주세요. '),

    ],
  )
  email = StringField(
    '메일주소',
    validators=[
      DataRequired(message='메일 주소는 필수입니다. '),
      Email(message='메일 주소의 형식으로 입력해 주세요. '),
    ],
  )
  password = PasswordField(
    '비밀번호',
    validators=[DataRequired(message='비밀번호는 필수입니다. ')]
  )
  #사용자폼 submit의 문구를 설정
  submit = SubmitField('신규 등록')