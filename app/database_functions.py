import sqlite3
 
def SQLite_connection():
    try:
        conn = sqlite3.connect('discount_codes.db')
        print("Database connection is established successfully!")
        return conn
    except sqlite3.Error: print(sqlite3.Error)
         
def create_table(conn, table_name, columns):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS '''+table_name+''' '''+columns+'''''')
    conn.commit()

def insert_into_db(conn, brand, code):
    cur = conn.cursor()
    cur.execute("INSERT INTO brand_codes (brand, code) VALUES (\'"+brand+"\',\'"+code+"\')")
    conn.commit()

def get_code_from_db(conn, brand):
    cur = conn.cursor()
    selected_codes = cur.execute("SELECT * FROM brand_codes WHERE brand = \'"+brand+"\' ORDER BY RANDOM() LIMIT 1").fetchone()
    conn.commit()
    return selected_codes