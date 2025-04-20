import pandas as pd
import matplotlib.pyplot as plt

himalaye = pd.read_csv("himalaye.csv", encoding='utf-8')

print(himalaye.columns.tolist())
print(himalaye.dtypes)
print(len(himalaye.columns))

liczba_kolumn_z_nan = himalaye.isna().any().sum()
print("Kolumny zawierające NaN:", liczba_kolumn_z_nan)

kolumny_z_nan = himalaye.columns[himalaye.isna().any()].tolist()
print("Nazwy kolumn z NaN:", kolumny_z_nan)

kolumny_tylko_nan = himalaye.columns[himalaye.isna().all()]
print("Kolumny zawierające tylko NaN:", kolumny_tylko_nan.tolist())

kolumny_tylko_beznan = himalaye.columns[himalaye.notna().all()]
print(f"Kolumny niezawierające nan: {kolumny_tylko_beznan.tolist()}")
pd.set_option('display.max_columns', None)
print(himalaye.iloc[:, 0:9])
pd.reset_option('display.max_columns')

himal = pd.DataFrame()

himal[("Numer_wyprawy")] = himalaye["EXPID"]
himal["MEMBID"] = himalaye["MEMBID"]
himal["MYEAR"] = himalaye["MYEAR"]
himal[("FNAME")] = himalaye["FNAME"]
himal[("LNAME")] = himalaye["LNAME"]


print(himal.iloc[50:80, :])

czy_sa_duplikaty = himal[himal["Numer_wyprawy"] == "AMAD79301"]["MEMBID"].duplicated(keep=False).any()
print(czy_sa_duplikaty)

himal["MEMBID"] = (
    himal.groupby("Numer_wyprawy")["MEMBID"]
    .transform(lambda x: sorted(x.values))
)

print(himal)

liczba_nan_w_imionach = himal["FNAME"].isna().sum()
liczba_nan_w_nazwiskach = himal["LNAME"].isna().sum()
print(liczba_nan_w_imionach)
print(liczba_nan_w_nazwiskach)

duplikaty = himal.duplicated(subset=["FNAME", "LNAME"], keep='first')
ile_duplikatow = duplikaty.sum()

print(duplikaty)
print("duplikaty:", ile_duplikatow)

himal[["FNAME", "LNAME"]].fillna(" ")
himal[["FNAME", "LNAME"]] = himal[["FNAME", "LNAME"]].astype("string")

print(himal["FNAME"].dtypes)

himal.to_csv('himalgotowe.csv', index=False, encoding='utf-8')







