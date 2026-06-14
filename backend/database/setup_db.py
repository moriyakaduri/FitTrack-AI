import pyodbc

# הגדרות התחברות לשרת המקומי שלכן
SERVER = 'localhost\\SQLEXPRESS'

def setup_database():
    try:
        # 1. התחברות ראשונית לשרת כדי ליצור את הדאטה-בייס
        conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};Trusted_Connection=yes;"
        conn = pyodbc.connect(conn_str, autocommit=True)
        cursor = conn.cursor()
        
        print("Creating Database 'FitTrackDB'...")
        # ננסה ליצור את הדאטה-בייס (אם הוא כבר קיים, זה פשוט ימשיך)
        try:
            cursor.execute("CREATE DATABASE FitTrackDB")
        except Exception:
            print("Database already exists or verified.")
        
        cursor.close()
        conn.close()

        # 2. התחברות ישירות לדאטה-בייס החדש כדי לבנות את הטבלאות
        conn_str_db = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE=FitTrackDB;Trusted_Connection=yes;"
        conn = pyodbc.connect(conn_str_db)
        cursor = conn.cursor()

        print("Creating tables inside FitTrackDB...")

        # יצירת טבלת משתמשים
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Users' AND xtype='U')
            CREATE TABLE Users (
                UserID INT IDENTITY(1,1) PRIMARY KEY,
                Username NVARCHAR(50) NOT NULL UNIQUE,
                PasswordHash NVARCHAR(255) NOT NULL,
                WeightStatus NVARCHAR(50) DEFAULT 'On Track'
            )
        """)

        # יצירת טבלת ארוחות
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Meals' AND xtype='U')
            CREATE TABLE Meals (
                MealID INT IDENTITY(1,1) PRIMARY KEY,
                UserID INT FOREIGN KEY REFERENCES Users(UserID),
                MealName NVARCHAR(100) NOT NULL,
                Calories INT NOT NULL,
                ProteinG INT NOT NULL,
                LogDate DATETIME DEFAULT GETDATE()
            )
        """)

        # יצירת טבלת אימונים
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Workouts' AND xtype='U')
            CREATE TABLE Workouts (
                WorkoutID INT IDENTITY(1,1) PRIMARY KEY,
                UserID INT FOREIGN KEY REFERENCES Users(UserID),
                WorkoutType NVARCHAR(100) NOT NULL,
                DurationMinutes INT NOT NULL,
                CaloriesBurned INT NOT NULL,
                LogDate DATETIME DEFAULT GETDATE()
            )
        """)

        conn.commit()
        print("🚀 Success! All tables created successfully inside SQL Server.")
        
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"🛑 Error setup database: {e}")

if __name__ == "__main__":
    setup_database()