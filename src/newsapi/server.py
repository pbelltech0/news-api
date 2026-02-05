from fastapi import FastAPI
from newsapi import NewsAPI
import os

API_KEY = os.getenv("NEWS_API_KEY", "")

app = FastAPI()
news_client = NewsAPI(API_KEY)
 
@app.get("/everything")
async def everything(query: str):
    response = await news_client.get_everything(query)
    return response.json()

@app.get("/top-headlines")
async def top_headlines(query: str):
    response = await news_client.get_top_headlines(query)
    return response.json()