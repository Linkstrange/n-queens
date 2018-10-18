from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def __get_database_connection_data__():
    return 'postgresql://{0}:{1}@{2}/{3}'.format(
        'postgres',
        'root',
        'localhost:5432',
        'nQueens')


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
