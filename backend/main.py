import fastapi


app = fastapi.FastAPI()


@app.get("/")
def home():
    return {"message": "this is the backend api for a website"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8001)
