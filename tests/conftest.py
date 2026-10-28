import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import main
from database import Base, get_db


@pytest.fixture
def client(tmp_path, monkeypatch):
    arquivo = tmp_path / "teste.db"

    engine_teste = create_engine(
        f"sqlite:///{arquivo}",
        connect_args={"check_same_thread": False},
    )

    SessaoTeste = sessionmaker(bind=engine_teste)
    Base.metadata.create_all(bind=engine_teste)

    def get_db_teste():
        db = SessaoTeste()

        try:
            yield db
        finally:
            db.close()

    monkeypatch.setattr(main, "engine", engine_teste)
    main.app.dependency_overrides[get_db] = get_db_teste

    try:
        with TestClient(main.app) as cliente:
            yield cliente
    finally:
        main.app.dependency_overrides.clear()
        engine_teste.dispose()