import pyodbc

def get_db_connection():
    try:
        # תמלאו כאן את הפרטים המדויקים שקיבלתן מסומי על המסך
        conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=הסרבר_שמופיע_לכן_בסומי;"
            "DATABASE=FitTrackDB;"
            "UID=שם_המשתמש_שמופיע_לכן;"
            "PWD=הסיסמה_שמופיע_לכן;"
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"Error connecting to Somee cloud database: {e}")
        return None