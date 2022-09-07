from ast import Try
import psycopg


class UserConnection():
    conn = None

    def __init__(self):  # inciando a conexão
        try:
            self.conn = psycopg.connect(
                "dbname=api_crud user=postgres password=12345 host=localhost port=5432")
        except psycopg.OperationalError as e:
            print(e)
            self.conn.close()

    def read_all(self):  # Ler arquivos
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "user"
            """)
            return data.fetchall()  # busca todas as linhas da tabela.

    def read_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "user" WHERE id = %s
            """, (id,))

            return data.fetchone()  # busca uma linha da tabela.

    def write(self, data):  # adicionar valores
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "user"(name, phone) VALUES(%(name)s, %(phone)s)
            """, data)
            self.conn.commit()  # confirmação de envio ao banco de dados

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "user" SET name = %(name)s, phone = %(phone)s WHERE id = %(id)s
            """, data)
            self.conn.commit()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "user" WHERE id = %s
            """, (id,))
        self.conn.commit()

    def __def__(self):  # destrutor
        self.conn.close()
