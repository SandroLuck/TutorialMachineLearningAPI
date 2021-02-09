# General
This is the repository associated with the youtube tutorial at: TODO:
It is very simplistic and is meant as a guideline for implementing a Machine Learning API and not necessarily a good Machine Learning algorithm.
I put particular emphasis on making this tutorial as short as possible.

## To run:
### Locally
I recommend using docker below, but also works like this:
`pip install -r requirements.txt`
`cd TO/PATH`
`uvicorn main:app --reload`

### Using Docker
cd to the folder: `cd PATH/TO/MlApiTutorial`
run docker: `docker-compose up --build`

### Find Solution at
recommended: go in browser to http://localhost/docs (Assuming your docker hosts there else check `docker ps` it's on port 80)
you can test the API directly with GUI http://localhost/docs
or sent to http://localhost/will_survive

## For dev purposes
tests: `python -m main`
run server: `uvicorn main:app --reload`

## Troubleshoot
find IP: `docker ps`

## Files
'main.py' holds the API-related code. We put all in one file to make project simpler.
'test.py' has one test case to validate classifier is roughly working.
'Dockerfile' configures the server and installs dependencies. I used the Uvicorn/FastApi
'docker-compose.yml' not really needed. Simplifies execution on your side. I put restart: always incase you test edge cases (I did not handle them). 
'make_model.py' builds and selects a model. I did not validate them much since this is more of an API tutorial.

## Test
I implemented a test to integrate it.
In practice running them in Travis, Circelci before pulling from GitHub would be better.

## Deploy to a cloud
Check docker related deployment possibilities of your favorite cloud provider

## Data From
Kaggle: https://www.kaggle.com/c/titanic-dataset/data
