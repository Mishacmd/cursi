import psycopg2
import config


with psycopg2.connect(
    dbname=config.PGDATABASE,
    user=config.PGUSER,
    password=config.PGPASSWORD,
    host=config.PGHOST,
    port=5432,
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)