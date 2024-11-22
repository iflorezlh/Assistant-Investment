from src.database.db_connection import SqlConnection
from src.database.alpha_vantage_API import AlphaAPI
import json
import pandas as pd

# Ruta al archivo JSON
path = r'/home/ivanfl/Assistant-Investment/config/api_keys.json'

# Leer el archivo JSON y cargarlo como un diccionario
with open(path, 'r') as file:
    credenciales = json.load(file)

# credenciales para la conexión
server = credenciales['bd_credentials']['server']
database = credenciales['bd_credentials']['database']
username = credenciales['bd_credentials']['username']
password = credenciales['bd_credentials']['password']

api_key = credenciales['alpha_vantage']['API_KEY']

def data_wrangling(df):
    df = df.replace({'None': 0}).fillna(0)  
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='raise')
            df[col] = df[col] / 1000  
            df[col] = df[col].astype(int)      
        except ValueError:
            pass
        except Exception as e:
            pass     
    return df

ticker = input("Write Stock Ticker: ").upper()

conn = SqlConnection(server, username, password, database)

with conn.connect() as cnx:
    cursor = cnx.cursor()
    cursor.execute("SELECT Ticker FROM Tickers_Companies WHERE Ticker = ?", (ticker,))
    row = cursor.fetchall()

    if row:
        print(f'The data for company with ticker {ticker} is in DB')
    else:
        print(f'Ticker {ticker} not found in DB, downloading financial data...')
        
        statements = ['INCOME_STATEMENT', 'BALANCE_SHEET', 'CASH_FLOW']
        for statement in statements:
            
            table_name = f'{statement.capitalize()}_{ticker.capitalize()}'
            
            alpha = AlphaAPI(statement, ticker, api_key)
            financial_statement = alpha.data_report()
            df = data_wrangling(financial_statement)
            print(df)

if __name__ == "__main__":
    ticker