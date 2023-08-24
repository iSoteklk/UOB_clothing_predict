from fuzzywuzzy import process
from fastapi import APIRouter
from controllers.controller import predict_clothing

router = APIRouter()


@router.get("/predict/{text}/{color}/{gender}/{type}/{categories}")
# http://127.0.0.1:8000/predict/I%20want%20to%20go%20outing%20in%20the%20morning/black/male/casual/Watch,Shoes,Shirt,Trousers,sunglass
async def read_item(
    text: str,
    color: str,
    gender: str,
    type: str,
    categories: str
):
    situation = find_matching_situation(text)
    time = find_matching_time(text)
    categories = categories.split(',')
    print(f"{text}")
    print(f"{situation}, {color}, {time}, {gender},{type} {categories}")
    predictions = await predict_clothing(situation, color, time, gender, type, categories)
    return predictions


def find_matching_time(input_string):
    array_of_words = ["morning", "evening", "noon", "night"]

    input_string_lower = input_string.lower()

    best_match, similarity = process.extractOne(
        input_string_lower, array_of_words)

    if similarity >= 80:
        return best_match

    return ""


def find_matching_situation(input_string):
    array_of_words = ["party", "wedding", "work", "outing"]

    input_string_lower = input_string.lower()

    best_match, similarity = process.extractOne(
        input_string_lower, array_of_words)

    if similarity >= 80:
        return best_match

    return ""
