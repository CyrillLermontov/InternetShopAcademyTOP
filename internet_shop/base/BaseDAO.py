from sqlalchemy import insert, select, update, delete

from database import Base, session_maker


class BaseDAO:
    @classmethod
    def find_all(cls, model: Base) -> list:
        with session_maker() as session:
            query = select(model)
            result = session.execute(query)
            return [row for row in result.scalars()]

    @classmethod
    def find_by_id(cls, model: Base, model_id: int) -> list:
        with session_maker() as session:
            query = select(model).filter_by(id=model_id)
            result = session.execute(query)
            return result.fetchone()

    @classmethod
    def add(cls, model, data) -> list:
        with session_maker() as session:
            query = insert(model).values(**data)
            session.execute(query)
            session.commit()
            query = select(model).filter_by(**data)
            result = session.execute(query)
            return result.fetchone()[0]

    @classmethod
    def update(cls, model: Base, model_id: int, data) -> list:
        with session_maker() as session:
            query = update(model).where(model.id == model_id).values(**data)
            session.execute(query)
            session.commit()
            query = select(model).filter_by(id=model_id)
            result = session.execute(query)
            return result.fetchone()[0]

    @classmethod
    def delete(cls, model: Base, model_id: int):
        with session_maker() as session:
            query = delete(model).where(model.id == model_id)
            session.execute(query)
            session.commit()