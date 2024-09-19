from fastapi import APIRouter
from .endpoints import conversor

router = APIRouter()

router.include_router(conversor.router, prefix='/conversor', tags=['Conversor V1'])
