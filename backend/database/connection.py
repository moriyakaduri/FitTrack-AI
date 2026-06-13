import pyodbc

# הגדרות התחברות בסיסיות ל-SQL Server מקומי
# בהמשך תוכלו להחליף את זה בפרטי הענן של Somee לפי דרישות המרצה
SERVER = 'localhost\\SQLEXPRESS'
DATABASE = 'FitTrackDB'

def get_db_connection():
    try:
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={SERVER};"
            f"DATABASE={DATABASE};"
            f"Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None