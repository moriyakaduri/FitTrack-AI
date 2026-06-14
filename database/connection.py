import pyodbc

def get_db_connection():
    try:
        # הפרטים האמיתיים והמדויקים שלכן מתוך Somee!
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=FitTrackDB.mssql.somee.com;"
            "DATABASE=FitTrackDB;"
            "UID=moriyakaduri_SQLLogin_1;"
            "PWD=השתמש_בסיסמה_מלוח_הבקרה_הזה_*" # כאן תהיה הסיסמה שלכן
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"Error connecting to Somee cloud database: {e}")
        return None