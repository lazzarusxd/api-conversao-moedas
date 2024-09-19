class Response:
    sucesso_response = {
        200: {
            "description": "Conversão bem-sucedida, retorna os resultados das moedas convertidas.",
            "content": {
                "application/json": {
                    "example": {
                        "resultado": {
                            "EUR": 210.00,
                            "JPY": 23100.00
                        }
                    }
                }
            }
        }
    }

    erro_validacao_response = {
        400: {
            "description": "Erro de validação. Ocorre quando os parâmetros não atendem aos requisitos esperados.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["query", "moeda_origem"],
                                "msg": "Valor inválido. Forneça uma moeda válida no formato 'USD', 'BRL', etc.",
                                "type": "value_error"
                            },
                            {
                                "loc": ["query", "valor"],
                                "msg": "Valor inválido. Forneça um número válido maior que 0.",
                                "type": "value_error"
                            }
                        ]
                    }
                }
            }
        }
    }

    erro_validacao_response_422 = {
        422: {
            "description": "Erro de validação, detalhes sobre o erro serão retornados.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["query", "moeda_origem"],
                                "msg": "Valor inválido. Forneça uma moeda válida.",
                                "type": "value_error"
                            }
                        ]
                    }
                }
            }
        }
    }
