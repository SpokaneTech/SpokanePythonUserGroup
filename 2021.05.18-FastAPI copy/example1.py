from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def hello_world():
    return 'Hello Spokane Python User Group! 🐍'


@app.get('/vehicles/')
def get_vehicle():
    return {
        'year': 2003,
        'make': 'Mitsubishi',
        'model': 'Montero Sport'
    }
