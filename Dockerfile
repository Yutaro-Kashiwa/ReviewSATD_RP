FROM python:3.9-slim-buster

ENV WORK_DIR /work
WORKDIR ${WORK_DIR}

RUN pip install -U \
        setuptools \
        pip && \
    pip install pipenv
RUN apt update -y
RUN apt-get install tk -y
COPY ./src ${WORK_DIR}/src
COPY ./conf ${WORK_DIR}/conf
COPY ./inputs ${WORK_DIR}/inputs
COPY ./requirements.txt ${WORK_DIR}/requirements.txt


#RUN pipenv install --system
RUN pip install -r requirements.txt
WORKDIR ${WORK_DIR}/src

ENTRYPOINT ["python", "-m", "exe.all"]