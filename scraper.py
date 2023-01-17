import requests
from datetime import date
import pandas as pd

if __name__ == "__main__":
    file_name = 'FRB_H15.csv'
    start_date = '01/01/1954'
    end_date = date.today().strftime("%m/%d/%Y")
    url = 'https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=c5025f4bbbed155a6f17c587772ed69e&lastobs=&from='+start_date+'&to='+end_date+'&filetype=csv&label=omit&layout=seriescolumn'
    r = requests.get(url)
    if r.status_code == 200:
        with open(file_name,'w', encoding='utf-8') as file:
            file.write(r.content)
            df = pd.read_csv(file_name, skiprows=1)
            df.to_csv(file_name, index=False)
