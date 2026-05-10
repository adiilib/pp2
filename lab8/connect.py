import psycopg2
from config import params

def get_conn():
    return psycopg2.connect(**params)
