from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser


def __get_database_connection_data__():
    config = ConfigParser()
    config.read('config.ini')
    user = config['DEFAULT']['DATABASE_USER']
    password = config['DEFAULT']['DATABASE_PASS']
    host = config['DEFAULT']['DATABASE_HOST']
    name = config['DEFAULT']['DATABASE_NAME']

    return 'postgresql://{0}:{1}@{2}/{3}'.format(
        user,
        password,
        host,
        name)


class NQueensDataAccess:
    def __init__(self):
        connection_string = __get_database_connection_data__()
        engine = create_engine(connection_string)
        session = sessionmaker(bind=engine)
        self.__session__ = session()

    def save_solution(self, solution):
        self.__session__.add(solution)
        self.__session__.commit()
        return solution.solution_id

    def finish_session(self):
        self.__session__.close()

    def rollback(self):
        self.__session__.rollback()
