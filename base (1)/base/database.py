from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session


# TODO: crie a classe Base herdando de DeclarativeBase.
class Base(DeclarativeBase):
    pass


# TODO: crie a engine apontando para sqlite:///biblioteca.db.

engine = create_engine("sqlite:///biblioteca.db")

def criar_banco():
    #  crie as tabelas usando Base.metadata.create_all(bind=engine).
    Base.metadata.create_all(bind=engine)
    pass


def nova_sessao():
    # TODO: devolva uma Session ligada à engine.
    return Session(engine)
    
