import jwt
from django.conf import settings
from datetime import datetime, timedelta

def generate_token(user_id, email):
    # Set expiration time to 2 minutes from now
    exp = datetime.utcnow() + timedelta(minutes=2)
    # Create payload with expiration
    payload = {
        'id': user_id,
        'email': email,
        'exp': exp
    }
    # Encode token
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')
    return token
