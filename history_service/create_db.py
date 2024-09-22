import sqlite3

def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Exception as e:
        print(e)
    return conn

def execute_query(conn, sql, params):
    """Execute an SQL query."""
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"Error executing query: {e}")

# Create the database file
db_file = "calculator.db"

# Create a connection to the database
conn = create_connection(db_file)

# Create a table to store calculation history
create_table_sql = """
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operator TEXT NOT NULL,
    num1 REAL NOT NULL,
    num2 REAL NOT NULL,
    result REAL NOT NULL
);
"""

execute_query(conn, create_table_sql, ())

# ... (rest of your calculator code)

# Insert a new calculation into the history table
insert_sql = "INSERT INTO history (operator, num1, num2, result) VALUES (?, ?, ?, ?)"
execute_query(conn, insert_sql, ("+", 2, 3, 5))
conn.close()
