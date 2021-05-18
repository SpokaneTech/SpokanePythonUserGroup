from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def hello_docker():
    return 'Hello Docker! 🐋'
