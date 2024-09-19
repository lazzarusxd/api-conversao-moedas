from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from services.conversor_moedas import conversor_moeda
from schemas.conversor_schemas import ConversorResponse, ConversorRequest
from .responses.conversor_responses import Response

router = APIRouter()


@router.post('/', response_model=ConversorResponse, responses={
    **Response.sucesso_response,
    **Response.erro_validacao_response,
    **Response.erro_validacao_response_422
})
async def post_conversao(body: ConversorRequest) -> JSONResponse:

    moeda_origem = body.moeda_origem
    moedas_conversao = body.moedas_conversao
    valor = body.valor

    resultado = {}

    for moeda in moedas_conversao:
        response = await conversor_moeda(
            moeda_origem=moeda_origem,
            moeda_conversao=moeda,
            valor=valor
        )

        resultado[moeda] = round(response, 2)

    return JSONResponse(resultado, status_code=status.HTTP_200_OK)
