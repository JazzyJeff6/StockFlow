def test_cadastrar_produto(client):
    dados = {
        "nome": "Teclado USB",
        "codigo": "TEC-001",
        "preco": "89.90",
    }

    resposta = client.post("/produtos", json=dados)

    assert resposta.status_code == 201

    produto = resposta.json()

    assert produto["id"] > 0
    assert produto["nome"] == "Teclado USB"
    assert produto["codigo"] == "TEC-001"
    assert produto["preco"] == "89.90"

    consulta = client.get(f"/produtos/{produto['id']}")

    assert consulta.status_code == 200
    assert consulta.json() == produto

def test_rejeitar_codigo_duplicado(client):
    dados = {
        "nome": "Teclado USB",
        "codigo": "TEC-001",
        "preco": "89.90",
    }

    primeira = client.post("/produtos", json=dados)
    assert primeira.status_code == 201

    segunda = client.post("/produtos", json=dados)
    assert segunda.status_code == 409

    consulta = client.get("/produtos")

    assert consulta.status_code == 200
    assert consulta.json() == [primeira.json()]

def test_rejeitar_preco_negativo(client):
    resposta = client.post(
        "/produtos",
        json={
            "nome": "Teclado USB",
            "codigo": "TEC-001",
            "preco": "-10.00",
        },
    )

    assert resposta.status_code == 422

    consulta = client.get("/produtos")

    assert consulta.status_code == 200
    assert consulta.json() == []

def test_consultar_produto_inexistente(client):
    resposta = client.get("/produtos/999")

    assert resposta.status_code == 404
    assert resposta.json() == {
        "detail": "Produto não encontrado."
    }
    