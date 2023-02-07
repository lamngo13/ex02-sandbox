from fastapi import FastAPI
#import FastAPI from

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}