from fastapi import APIRouter, status, HTTPException, Query
from fastapi.responses import JSONResponse
from services.conversor_moedas import conversor_moeda
from schemas.conversor_schemas import ConversorResponse
from .responses.conversor_responses import Response

router = APIRouter()


@router.get('/', response_model=ConversorResponse, responses={
    **Response.sucesso_response,
    **Response.erro_validacao_response,
    **Response.erro_validacao_response_422
})
async def get_conversao(
        moeda_origem: str = Query(title='Moeda de origem',
                                  description='Moeda a ser convertida.',
                                  max_length=3,
                                  min_length=3,
                                  regex='^[A-Z]{3}$'),
        moedas_conversao: str = Query(title='Moeda da conversão',
                                      description='Moedas as quais a moeda de origem será convertida.',
                                      max_length=50,
                                      regex='^[A-Z]{3}(,[A-Z]{3})*$'),
        valor: str = Query(title='Valor a ser convertido',
                           description='Valor da moeda de origem a ser convertida.')) -> JSONResponse:
    try:
        valor = float(valor.replace(',', '.'))
        if valor <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='O valor informado deve ser maior que 0.')
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Valor inválido. Forneça um número válido maior que 0. (ex: 210.00 / 210,00 / 210).')

    moedas_conversao = moedas_conversao.split(',')
    resultado = {}

    for moeda in moedas_conversao:
        response = await conversor_moeda(
            moeda_origem=moeda_origem,
            moeda_conversao=moeda,
            valor=valor
        )

        resultado[moeda] = round(response, 2)

    return JSONResponse(resultado, status_code=status.HTTP_200_OK)
