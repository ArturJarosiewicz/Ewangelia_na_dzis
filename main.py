import functions

URL = "https://opoka.org.pl/liturgia"

scrapped = functions.scrape(URL)
extracted = functions.extract(scrapped)
# print(extracted)

message = f"""\
Subject: Ewangelia na dziś
Pierwsze czytanie
{extracted['Pierwsze czytanie ksiega']}

{extracted['Pierwsze czytanie']}

-------------------------------------------------
Ewangelia
{extracted['Ewangelia ksiega']}

{extracted['Ewangelia']}
"""

functions.send_email(message)