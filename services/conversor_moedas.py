from os import getenv
import aiohttp
from fastapi import HTTPException, status

ALPHAVANTAGE_APIKEY = getenv('ALPHAVANTAGE_APIKEY')


async def conversor_moeda(moeda_origem: str, moeda_conversao: str, valor: float):
    url= (f'https://www.alphavantage.co/query?'
          f'function=CURRENCY_EXCHANGE_RATE&'
          f'from_currency={moeda_origem}&'
          f'to_currency={moeda_conversao}&'
          f'apikey={ALPHAVANTAGE_APIKEY}')

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    if 'Realtime Currency Exchange Rate' not in data:
        if 'Information' in data:
            raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                                detail="Limite de requisições atingido. Tente novamente mais tarde.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Erro no response. Verifique se o formato está correto ou se a moeda existe. Ex: 'USD'.")

    taxa_cambio = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    return valor * taxa_cambio
