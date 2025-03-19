from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hello world aass"


@app.get("/topic")
def f():
    return "strasan"