from environs import Env
from sqlalchemy import create_engine


def load_enve(path: str | None = None):
    env = Env()
    env.read_env(path)
    DB_USER = env('DB_USER')
    DB_PASS = env('DB_PASS')
    DB_HOST = env('DB_HOST')
    DB_PORT = env('DB_PORT')
    DB_NAME = env('DB_NAME')
    return DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


def get_datebase():
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME = load_enve()
    return f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
