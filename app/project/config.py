import os
from dotenv import load_dotenv


load_dotenv()

REDIS_HOST = os.getenv('HOST')
REDIS_PORT = os.environ.get('PORT')
REDIS_USERNAME = os.environ.get('USERNAME')
REDIS_PASSWORD = os.environ.get('PASSWORD')

AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
AWS_ENDPOINT_URL = os.getenv('AWS_ENDPOINT_URL')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_PUBLIC_URL = os.getenv('AWS_PUBLIC_URL')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

AMQP_HOST=os.getenv('AMQP_HOST')
AMQP_PORT=int(os.getenv('AMQP_PORT'))
AMQP_VIRTUAL_HOST=os.getenv('AMQP_VIRTUAL_HOST')
AMQP_USERNAME=os.getenv('AMQP_USERNAME')
AMQP_PASSWORD=os.getenv('AMQP_PASSWORD')

PGHOST=os.getenv('PGHOST')
PGDATABASE=os.getenv('PGDATABASE')
PGUSER=os.getenv('PGUSER')
PGPASSWORD=os.getenv('PGPASSWORD')