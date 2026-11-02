from flask import jsonify
from flask_jwt_extended import create_access_token
from app.models import User


def register_user(data):
    name = str(data.get('name') or '').strip()
    email = str(data.get('email') or '').strip().lower()
    password = data.get('password')
    if not name:
        return None, 'Name is required'
    if not email:
        return None, 'Email is required'
    if not password or len(password) < 6:
        return None, 'Password must be at least 6 characters'
    if User.query.filter_by(email=email).first():
        return None, 'Email already registered'

    user = User(
        name=name,
        email=email,
        role=data.get('role') if data.get('role') in ('user', 'agent') else 'user',
        department=data.get('department', 'IT Support')
    )
    user.password = password
    from app import db
    db.session.add(user)
    db.session.commit()
    token = create_access_token(
        identity=str(user.id),
        additional_claims={'role': user.role, 'email': user.email},
    )
    return {'token': token, 'user': user.to_dict()}, None


def login_user(data):
    user = User.query.filter_by(email=str(data.get('email') or '').strip().lower()).first()
    if not user or not user.verify_password(data.get('password')):
        return None, 'Invalid email or password'
    token = create_access_token(
        identity=str(user.id),
        additional_claims={'role': user.role, 'email': user.email},
    )
    return {'token': token, 'user': user.to_dict()}, None
