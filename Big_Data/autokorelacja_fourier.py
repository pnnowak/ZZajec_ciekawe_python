import numpy as np
import matplotlib.pyplot as plt
# from scipy.signal import find_peaks
# from statsmodels.tsa.stattools import acf
# from statsmodels.robust import mad
# from sklearn.decomposition import PCA
import pandas as pd
import time


stocks = pd.read_csv("C:\\Users\\piotr\\Downloads\\DJIA_ClosingValues_1896-10-07-2025-03-28.csv")
print(stocks.head())
print(stocks.dtypes)

print(stocks.isna().sum())
stocks['Date'] = pd.to_datetime(stocks['Date'])

plt.plot(stocks['Date'], stocks['DJIA'])
plt.show()

ean = np.mean(stocks['DJIA'])
median = np.median(stocks['DJIA'])
std_dev = np.std(stocks['DJIA'])
min_val = np.min(stocks['DJIA'])
max_val = np.max(stocks['DJIA'])
print("srednia:", ean, " med:",median, " std_dev:",min_val, " max_val:", max_val)

#2
quantiles = stocks['DJIA'].quantile([0.25, 0.5, 0.75])

stocks['diff'] = stocks['DJIA'].diff()
stocks['diff'].plot(title='Różnicowanie pierwszego rzędu')
plt.show()

# result = seasonal_decompose(stocks['DJIA'], model='additive', period=30)  # np. miesiąc
# result.plot()
# plt.show()

# Średnia krocząca
stocks['rolling_mean'] = stocks['DJIA'].rolling(window=7).mean()  # okno 7-dniowe
stocks[['DJIA', 'rolling_mean']].plot(title='Średnia 7-dniowa')
plt.show()

# Inne cechy:
# stocks['mad'] = stocks['DJIA'].mad()  # Mediana absolutnego odchylenia
# stocks['zscore'] = (stocks['DJIA'] - mean_val) / std_val  # Z-score (normalizacja)
# stocks['return'] = stocks['DJIA'].pct_change()  # Zmiana procentowa


# Autokorelacja
def autocorr(x, lag=1):
    return np.corrcoef(x[:-lag], x[lag:])[0, 1]

lags = np.arange(1, 101)
autocorr_vals = [autocorr(stocks['DJIA'].dropna(), lag) for lag in lags]

plt.plot(lags, autocorr_vals)
plt.title('Autokorelacja')
plt.show()


# Transformata Fouriera (FFT)
def fourier_transform(signal):
    fft_vals = np.fft.fft(signal)
    fft_freq = np.fft.fftfreq(len(signal))
    return fft_vals, fft_freq

fft_vals, fft_freq = fourier_transform(stocks['DJIA'].dropna())
plt.plot(fft_freq, np.abs(fft_vals))
plt.title('Spektrum Fouriera')
plt.show()


start_time = time.time()
stocks['rolling_mean'] = stocks['DJIA'].rolling(window=7).mean()
print(f"Pandas metoda (średnia krocząca): {time.time() - start_time:.4f} sekundy")

# Pomiar czasu dla NumPy metod
start_time = time.time()
fft_vals, fft_freq = fourier_transform(stocks['DJIA'].dropna())
print(f"NumPy metoda (FFT): {time.time() - start_time:.4f} sekundy")