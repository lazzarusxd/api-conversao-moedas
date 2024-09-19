from fastapi import FastAPI
from api.v1.api import router as router_v1
from api.v2.api import router as router_v2

app = FastAPI(title='API - Conversão de Moedas',
              description="API responsável pela conversão de moedas, ela realiza o cálculo de taxa cambial através da "
                          "API externa Alpha Vantage e retorna ao usuário o valor convertido."
                          "\n- V1: Na versão 1, o usuário deve inserir as informações no Query."
                          "\n\n- V2: Na versão 2, o usuário deve inserir as informações no Body.",
              version="1.1")

app.include_router(router_v1, prefix='/api/v1')
app.include_router(router_v2, prefix='/api/v2')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, log_level="debug", reload=True)
