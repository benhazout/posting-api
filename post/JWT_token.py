from . import schemas
from datetime import datetime, timedelta
from jose import JWTError, jwt

# in order to generate SECRET_KEY
# bash: openssl rand -hex 32
SECRET_KEY = "fb194a5c5070d48e9f7a92ea1880af72163cb800213e68f9bdca18917a5c820b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('username')
        user_id: str = payload.get('user_id')
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username, user_id=user_id)
        return token_data
    except JWTError:
        raise credentials_exception
