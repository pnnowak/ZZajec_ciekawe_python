import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, interp1d
from sklearn.impute import SimpleImputer

# 3 i 2
# Generowanie dat i temperatur
dates = pd.date_range(start='2023-01-01', periods=30)
temperatures = np.random.normal(loc=10, scale=5, size=30)

# Dodanie kilku brakujących wartości
temperatures[5] = np.nan
temperatures[12] = np.nan
temperatures[20] = np.nan

df = pd.DataFrame({
    'date': dates,
    'temperature': temperatures
})

df.to_csv('weather_data.csv', index=False)

df = pd.read_csv('weather_data.csv', parse_dates=['date'])

# Sprawdź brakujące wartości
print(df.isnull().sum())

plt.plot(df['date'], df['temperature'], marker='o')
plt.title("Temperatura z brakami")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
print(len(df['temperature']))

imputer = SimpleImputer(strategy='mean')
x = df['date'].dropna().map(pd.Timestamp.toordinal)
y = df['temperature'].dropna()
temperatury = pd.DataFrame({
    'x': x,
    'y': y
})

temperaturygotowe = pd.DataFrame(imputer.fit_transform(temperatury), columns=temperatury.columns)

# Budujemy funkcję B-spline
spl = make_interp_spline(temperaturygotowe['x'], temperaturygotowe['y'])

# Punkty do prognozowania (np. co 1 dzień)
x_new = df['date'].map(pd.Timestamp.toordinal)
y_new = spl(x_new)

# Dodajemy do DataFrame
df['interpolated_temp'] = y_new

# Wizualizacja
plt.plot(df['date'], df['temperature'], 'o', label='oryginalne')
plt.plot(df['date'], df['interpolated_temp'], '-', label='interpolacja B-sklejana')
plt.title("Interpolacja B-sklejana temperatury")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#4

# Daty: 1 miesiąc (30 dni)
days = pd.date_range(start="2023-01-01", periods=30)

# Zużycie energii w sektorze domowym i przemysłowym
home_usage = np.random.normal(loc=120, scale=10, size=30)
industry_usage = np.random.normal(loc=500, scale=50, size=30)

# Dodaj brakujące wartości
home_usage[10] = np.nan
industry_usage[20] = np.nan

df_energy = pd.DataFrame({
    "date": days,
    "home": home_usage,
    "industry": industry_usage
})

df_energy.to_csv("energy_data.csv", index=False)

df = pd.read_csv("energy_data.csv", parse_dates=["date"])
x = df["date"].map(pd.Timestamp.toordinal)

# Interpolacja dla sektora domowego
home_clean = df["home"].dropna()
x_home = df["date"][df["home"].notnull()].map(pd.Timestamp.toordinal)
poly_home = interp1d(x_home, home_clean, kind='quadratic', fill_value="extrapolate")

# Wypełnianie braków
df["home_interp"] = poly_home(x)

# Wykres
plt.plot(df["date"], df["home"], 'o', label="oryginalne")
plt.plot(df["date"], df["home_interp"], '-', label="interpolacja (wielomian)")
plt.title("Zużycie energii - sektor domowy")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

