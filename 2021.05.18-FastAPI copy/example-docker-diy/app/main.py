from fastapi import FastAPI


app = FastAPI()


@app.get('/docker/')
def hello_docker():
    return 'Hello Docker - alt! 🐋'
