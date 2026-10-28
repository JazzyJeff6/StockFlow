from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class ProdutoCriar(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nome: str = Field(min_length=1, max_length=100)
    codigo: str = Field(min_length=1, max_length=30)
    preco: Decimal = Field(
        gt=0,
        max_digits=10,
        decimal_places=2,
        allow_inf_nan=False,
    )

class ProdutoResposta(ProdutoCriar):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
    )