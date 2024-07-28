from pydantic import BaseModel
from mlx_lm import load, generate
import torch
import os


class ApiGemma2MlxRequest(BaseModel):
    text: str

model, tokenizer = load("mlx-community/gemma-2-9b-8bit")

def handle(request: ApiGemma2MlxRequest):
    text = request.text

    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    try:
        result_text = process_text(text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"out_text": result_text}

def process_text(text: str) -> str:
    response = generate(
        model,
        tokenizer,
        prompt=text,
        verbose=True,
        temp=0.4,
        repetition_penalty=2.0,
        max_tokens=200
    )
    return response