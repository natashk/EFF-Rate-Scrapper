import requests
from datetime import date

if __name__ == "__main__":
    start_date = '01/01/1954'
    end_date = date.today().strftime("%m/%d/%Y")
    url = 'https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=c5025f4bbbed155a6f17c587772ed69e&lastobs=&from='+start_date+'&to='+end_date+'&filetype=csv&label=omit&layout=seriescolumn'
    r = requests.get(url)
    if r.status_code == 200:
        file = open('FRB_H15.csv','wb')
        file.write(r.content)
        file.close
