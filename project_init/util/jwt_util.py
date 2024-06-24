import jwt
from jwt import exceptions
import datetime


def create_token(payload, jwt_salt):
    headers = {
        'type': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=60 * 60)
    result = jwt.encode(payload=payload, key=jwt_salt, algorithm='HS256', headers=headers).decode('utf-8')
    return result


def parse_payload(token):
    result = {'status': False, 'data': None, 'error': None}
    try:
        verified_payload = jwt.decode(token, JWT_SALT, True)
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = 'token非法'
    return result


if __name__ == '__main__':
    JWT_SALT = "12345678123456781234567812345678"
    result = create_token({'username': 'test'}, JWT_SALT)
    print(result)
    print(parse_payload(result))
