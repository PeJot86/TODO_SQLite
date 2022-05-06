import sqlite3

class TodosSQLite:
        
    def __init__(self, db_file):
        self.db_file = db_file
    
    
    def create_connection(self):
        conn = sqlite3.connect('database.db')
        return conn
        
    
    def create_table(self):
        try:
            with self.create_connection() as conn:
                conn.execute('''
                    CREATE TABLE todos (
                        todos_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
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


    def show_all(self, table):
        with self.create_connection() as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table}")
            rows = cur.fetchall()
            return rows

        
    def show_where(self, table, **query):
        with self.create_connection() as conn:
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
    
    
    def add_todos(self, data):
        sql = '''INSERT OR IGNORE INTO todos(todos_id, title, description, status)
                    VALUES(?,?,?,?)'''
        with self.create_connection() as conn:
            cur = conn.cursor()
            cur.execute(sql, (data))
            conn.commit()
            return cur.lastrowid    


    def delete_all(self, table):
        with self.create_connection() as conn:
            sql = f'DELETE FROM {table}'
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            return print("Deleted")    


    def delete_where(self, table, **kwargs):
            qs = []
            values = tuple()
            for k, v in kwargs.items():
                qs.append(f"{k}=?")
                values += (v,)
            q = " AND ".join(qs)
            with self.create_connection() as conn:
                sql = f'DELETE FROM {table} WHERE {q}'
                cur = conn.cursor()
                cur.execute(sql, values)
                conn.commit()
                print("Deleted")

    
    def update_todo(self, table, todos_id, **kwargs):
        with self.create_connection() as conn:
            parameters = [f"{k} = ?" for k in kwargs]
            parameters = ", ".join(parameters)
            values = tuple(v for v in kwargs.values())
            values += (todos_id, )

            sql = f''' UPDATE {table}
                        SET {parameters}
                        WHERE todos_id = ?'''
            try:
                cur = conn.cursor()
                cur.execute(sql, values)
                conn.commit()
                print("OK")
            except sqlite3.OperationalError as e:
                print(e)

  
todos = TodosSQLite("database.db")