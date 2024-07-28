from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.llm import api_gemma2_mlx

router = APIRouter()

@router.post("/llm/gemma2_mlx")
async def llm_gemma2_mlx(request: api_gemma2_mlx.ApiGemma2MlxRequest):
    return api_gemma2_mlx.handle(request)