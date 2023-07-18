# routes/route.py
from fastapi import APIRouter
from controllers.controller import predict_clothing

router = APIRouter()


@router.get("/predict/{situation}/{color}/{time}/{gender}/{categories}")
async def read_item(
    situation: str,
    color: str,
    time: str,
    gender: str,
    categories: str
):
    categories = categories.split(',')
    predictions = await predict_clothing(situation, color, time, gender, categories)
    return predictions
