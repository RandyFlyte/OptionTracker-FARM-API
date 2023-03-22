from fastapi import FastAPI
from fastapi.responses import JSONResponse
from getQuotes import getOptionQuote, getStockQuote
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3001",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/option/{optionSymbol}")
async def option_endpoint(optionSymbol: str):
    data = {"quote": getOptionQuote(optionSymbol)}
    return JSONResponse(content=data)


@app.get("/stock/{tickerSymbol}")
async def stock_endpoint(tickerSymbol: str):
    data = {"mark": getStockQuote(tickerSymbol)}
    return JSONResponse(content=data)