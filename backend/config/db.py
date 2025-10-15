from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session, create_engine
from fastapi import FastAPI, Depends
from typing import Annotated

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

# ✅ Permitir acceso desde múltiples hilos
engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False},
    echo=False
)

with engine.connect() as conn:
    conn.exec_driver_sql("PRAGMA journal_mode=WAL;")

def get_session():
    # ✅ Asegura que cada sesión se cierre correctamente
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # ✅ Crear tablas y activar WAL
    SQLModel.metadata.create_all(engine)
    with engine.connect() as conn:
        conn.exec_driver_sql("PRAGMA journal_mode=WAL;")
    yield