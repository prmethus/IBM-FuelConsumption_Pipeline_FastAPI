FROM python:3.8

WORKDIR ml_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY *.py ./

COPY Pipeline ./Pipeline

COPY Data ./Data

CMD ["python", "./api.py"]
