FROM python:3.11-slim

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt --no-cache-dir
COPY ./reposipoint-backend /app

ENTRYPOINT [ "python" ]
CMD ["/app/main.py"]
EXPOSE 80
