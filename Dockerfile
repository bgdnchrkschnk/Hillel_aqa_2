FROM python:latest

WORKDIR /app

COPY test_docker_database_conn.py .

RUN pip install pytest psycopg2-binary

CMD ["pytest", "-k", "test_docker_db_connection_dockercompose"]