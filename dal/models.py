from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship

Base = declarative_base()


class Solution(Base):
    __tablename__ = 'solutions'

    solution_id = Column(BigInteger, primary_key=True, autoincrement=True)
    board_size = Column(SmallInteger)
    solution_ordinal = Column(Integer)
    board_hash = Column(BigInteger, unique=True)
    placements = relationship('Placement')

    def __repr__(self):
        return f'''<solution(solution_id={self.solution_id},
                    board_size={self.board_size},
                    solution_ordinal={self.solution_ordinal},
                    board_hash={self.board_hash})>'''


class Placement(Base):
    __tablename__ = 'placements'

    placement_id = Column(BigInteger, primary_key=True, autoincrement=True)
    solution_id = Column(BigInteger, ForeignKey('solutions.solution_id'))
    row = Column(SmallInteger)
    column = Column(SmallInteger)

    def __repr__(self):
        return f'''<placement(placement_id={self.placement_id},
                    solution_id={self.solution_id},
                    row={self.row},
                    column={self.column})>'''
