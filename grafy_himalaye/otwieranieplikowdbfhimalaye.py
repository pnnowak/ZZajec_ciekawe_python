from dbfread import DBF
import pandas as pd

# Otwieranie pliku DBF
table = DBF("members.DBF")
df = pd.DataFrame(iter(table))
#
# print(df.head())
# df.to_csv('himalaye.csv', index=False, encoding='utf-8')