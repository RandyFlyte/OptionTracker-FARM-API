from fastapi import FastAPI
from fastapi.responses import JSONResponse
from getQuotes import getOptionQuote

app = FastAPI()

@app.get("/option/{optionS}")
async def option_endpoint(optionS: str):
    data = {"quote": getOptionQuote(optionS)}
    return JSONResponse(content=data)
