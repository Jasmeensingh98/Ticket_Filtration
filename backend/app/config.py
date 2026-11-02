import os
from dotenv import load_dotenv

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
load_dotenv(os.path.join(root_dir, '.env'))
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


def get_config():
    database_url = os.getenv('DATABASE_URL', 'sqlite:///helpdesk.db')
    if database_url.startswith('postgresql://'):
        database_url = database_url.replace('postgresql://', 'postgresql+psycopg2://', 1)
    cors_origins = [
        origin.strip()
        for origin in os.getenv('CORS_ORIGINS', '*').split(',')
        if origin.strip()
    ]
    return {
        'SQLALCHEMY_DATABASE_URI': database_url,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'JWT_SECRET_KEY': os.getenv('JWT_SECRET', 'demo-secret-key'),
        'JWT_ALGORITHM': 'HS256',
        'DEMO_MODE': os.getenv('DEMO_MODE', 'true').lower() == 'true',
        'SECRET_KEY': os.getenv('SECRET_KEY', 'demo-secret-key'),
        'CORS_ORIGINS': cors_origins,
        'MAX_CONTENT_LENGTH': int(os.getenv('MAX_CONTENT_LENGTH', 12 * 1024 * 1024)),
    }
