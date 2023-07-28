# routes/route.py
from fastapi import APIRouter
from controllers.controller import predict_clothing

router = APIRouter()


@router.get("/predict/{situation}/{color}/{time}/{gender}/{categories}")
# http://127.0.0.1:8000/predict/wedding/white/morning/male/t-shirt,trouser,skirt,shirt,short
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
