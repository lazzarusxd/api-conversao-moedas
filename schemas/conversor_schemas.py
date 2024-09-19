from typing import List, Dict
import re
from pydantic import BaseModel, Field, field_validator


class ConversorRequest(BaseModel):
    moeda_origem: str = Field(title='Moeda de origem',
                              description='Moeda a ser convertida.',
                              examples=["USD"])
    moedas_conversao: List[str] = Field(title='Moedas da conversão',
                                        description='Moedas as quais a moeda de origem será convertida.',
                                        examples= [["USD", "JPY"], ["BRL"]])
    valor: float = Field(gt=0,
                         title='Valor a ser convertido',
                         description='Valor da moeda de origem a ser convertida.',
                         examples=[210, 210.00])

    @field_validator('moeda_origem')
    def validator_moeda_origem(cls, valor):
        if not re.match('^[A-Z]{3}$', valor):
            raise ValueError("Valor inválido. Forneça uma moeda válida. Exemplos: 'USD', 'BRL', 'JPY'.")
        return valor

    @field_validator('moedas_conversao')
    def validator_moedas_conversao(cls, valor):
        for moeda in valor:
            if not re.match('^[A-Z]{3}$', moeda):
                raise ValueError("Valor inválido. Forneça uma List[moedas] válida. Exemplo: ['USD', 'BRL'].")
        return valor

    @field_validator('valor', mode="before")
    def validator_valor(cls, valor):
        valor = str(valor).replace(',', '.')
        try:
            valor = float(valor)
            if valor <= 0:
                raise ValueError('O valor deve ser maior que 0.')
            return valor
        except ValueError:
            raise ValueError('Valor inválido. Forneça um número válido (ex: 210.00 ou 210,00).')


class ConversorResponse(BaseModel):
    conversao: Dict[str, float] = Field(title='Resultados da Conversão',
                                        description='Dicionário com as moedas convertidas e seus valores.',
                                        examples=[{
                                            "USD": 210.00,
                                            "JPY": 5239.23
                                        }])
