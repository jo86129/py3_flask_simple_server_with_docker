FROM python:3.9-slim

WORKDIR /app

COPY BackendServer/ BackendServer/
COPY Other/ BackendServer/Other/

WORKDIR /app/BackendServer
RUN pip install -r requirements.txt
RUN mkdir /home/log

CMD ["python", "main.py"]