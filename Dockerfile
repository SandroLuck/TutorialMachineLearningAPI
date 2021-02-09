# Some container that is already suitable for unicover
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR '/app/app'
COPY ./requirements.txt ./
# install dependencies, we could also use the conda env, but it is more minimal
# we could probably find an image including this
RUN pip install --no-cache-dir -r requirements.txt
COPY ./test.py ./
COPY ./main.py ./
COPY ./model_weights/clf.bin ./model_weights/clf.bin
# do tests, usually better to do befor building container, e.g. travis, circelci
RUN python -m test