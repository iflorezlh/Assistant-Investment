import pyodbc

class SqlConnection:
    
    def __init__(self, database):
        self.server = '172.28.16.1'
        self.database = database
        self.username = 'ivan_florez_2'
        self.password = '6D6a2357.1152'
        self.connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};"
            f"DATABASE={self.database};UID={self.username};PWD={self.password};"
        )
        self.connection = None
        
    def connect(self):
        """Establece la conexión a la base de datos y la devuelve."""
        try:
            self.connection = pyodbc.connect(self.connection_string)
            print("Conexión establecida exitosamente.")
            return self.connection
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
            self.connection = None
