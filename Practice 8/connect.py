import psycopg2
import config

def get_connection():
    return psycopg2.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        dbname=config.db_name
    )