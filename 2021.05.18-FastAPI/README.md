# Getting Started with FastAPI

## Tools
- [Python](https://www.python.org/) (currently using version: 3.9.3)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (shipped with Python as of 3.3)
- [Visual Studio Code](https://code.visualstudio.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
    - [Pydantic](https://pydantic-docs.helpmanual.io/)
    - [Starlette](https://www.starlette.io/)
- [Docker](https://www.docker.com/)

## Installation
```powershell
git clone https://github.com/IntelliTect-Samples/SpokanePythonUserGroup.git
cd .\SpokanePythonUserGroup\2021.05.18-FastAPI\
pip install -r requirements.txt
```

## Example 1 - Hello World
```powershell
uvicorn example1:app --reload
```

## Example 2 - Models
```powershell
uvicorn example2:app --reload
```
- [Swagger UI](http://127.0.0.1:8000/docs)
- [Redoc](http://127.0.0.1:8000/redoc)

## Example 3 - Validating
Run
```powershell
uvicorn example3.main:app --reload
```

Tests
```powershell
pytest ./example4/vehicle_test.py
```

## Example 4 - Dependency Injection
Run
```powershell
uvicorn example4.main:app --reload
```

Tests
```powershell
pytest ./example4/vehicle_service_test.py
pytest ./example4/main_test.py
```

## Example - Docker
```powershell
cd ./example-docker
docker-compose build
docker-compose up
```

## Example - Docker --reload
```powershell
cd ./example-docker-reload
docker-compose build
docker-compose up
```

## Example - Docker DIY
```powershell
cd ./example-docker-diy
docker-compose build
docker-compose up
```

## Example - Security
```powershell
uvicorn example-security.main:app --reload
```

## Example - Security - token
```powershell
uvicorn example-security-token.main:app --reload
```

## Example - Security - username + password
```powershell
uvicorn example-security-password.main:app --reload
```

## Example - Upload File
```powershell
uvicorn example-upload.main:app --reload
```