### Quick start
1. `pip install poetry`  
2. `poetry install`  
3. `poetry update`

### Run project
`uvicorn app.main:app --reload`

### Build docker
`docker build -t hospital-registration . --file Dockerfile`

### For add models into alembic:  
1. go to /alembic/env.py
2. import models after 34 line
