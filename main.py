import functions
from datetime import datetime

URL = "https://opoka.org.pl/liturgia"

scrapped = functions.scrape(URL)
extracted = functions.extract(scrapped)
# print(extracted)

message = f"""\
Subject: Ewangelia na dzień {datetime.today().strftime("%d-%m")}
Pierwsze czytanie
{extracted['Pierwsze czytanie ksiega']}

{extracted['Pierwsze czytanie']}

-------------------------------------------------
Ewangelia
{extracted['Ewangelia ksiega']}

{extracted['Ewangelia']}
"""

functions.send_email(message)