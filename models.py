import sqlite3

class TodosSQLite:
        
    def create_connection(self):
            conn = sqlite3.connect('database.db')
            return conn
        
    
    def create_table(self):
        try:
            conn = self.create_connection()
            conn.execute('''
                CREATE TABLE todos (
                    todos_id INTEGER PRIMARY KEY NOT NULL,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    status TEXT NOT NULL
                );
            ''')
            conn.commit()
            print("Todos table created")
        except:
            print("Todos table already exist")
        finally:
            conn.close()
        
    
    def show_all(self, conn, table):
            conn = self.create_connection()
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table}")
            rows = cur.fetchall()
            return rows

        
    def show_where(self, conn, table, **query):
            conn = self.create_connection()
            cur = conn.cursor()
            qs = []
            values = ()
            for k, v in query.items():
                qs.append(f"{k}=?")
                values += (v,)
            q = " AND ".join(qs)
            cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
            rows = cur.fetchall()
            return rows
        
    
    def add_todos(self, conn, task):
        sql = '''INSERT INTO todos(todos_id, title, description, status)
                    VALUES(?,?,?,?)'''
        conn = self.create_connection()
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        cur.close()
        return cur.lastrowid
        


todos = TodosSQLite()