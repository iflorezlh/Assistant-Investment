import requests
import pandas as pd  # Modificación en la importación

class AlphaAPI:
    def __init__(self, statement, ticker, api_key):
        self.statement = statement
        self.ticker = ticker
        self.API_KEY = api_key
    
    def financial_statement(self):
        try:
            url = f'https://www.alphavantage.co/query?function={self.statement}&symbol={self.ticker}&apikey={self.API_KEY}'
            r = requests.get(url)
            data = r.json()
            print(f'Llamado al {self.statement} exitoso')
            return data
        except Exception as e:
            print(f'Error {e} llamando a la API')
            
    def data_report(self):
        try:
            data = self.financial_statement() 
            df = data['annualReports']  
            df = pd.json_normalize(df)
            return df
        except Exception as e:
            print(f'Error {e} procesando los datos')