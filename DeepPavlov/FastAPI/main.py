import asyncio
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
counter_model = 0
lock = asyncio.Lock()


class Model(BaseModel):
    method: str
    text: str


@app.post("/model")
async def model(request: Model):
    global counter_model
    async with lock:
        counter_model += 1
    result = 'Not found'
    request_dict = request.dict()
    if request_dict['method'] == 'lower':
        result = request_dict['text'].lower()
    elif request_dict['method'] == 'upper':
        result = request_dict['text'].upper()
    elif request_dict['method'] == 'swapcase':
        result = request_dict['text'].swapcase()
    return result


@app.get("/stat")
def stat():
    global counter_model
    return counter_model


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
