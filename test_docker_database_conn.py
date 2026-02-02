import time

import psycopg2

class TestDockerDB:

    def test_docker_db_connection_dockercompose(self):
        time.sleep(5)
        conn = psycopg2.connect(
            dbname="test_db",
            user="test_user",
            password="test_password",
            host="db",
            port="5432"
        )
        assert conn