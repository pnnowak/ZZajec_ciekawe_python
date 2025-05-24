import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicHermiteSpline, interp1d, make_interp_spline, CubicSpline
from sklearn.impute import SimpleImputer


stocks = pd.read_csv("C:\\Users\\piotr\\Downloads\\stocks_data.csv", parse_dates=['Date'])
print(stocks.isnull().sum())

x = stocks['Date'].map(pd.Timestamp.toordinal)
y = stocks.drop(columns=['Date'])
dy_dx = []
for i, columny in enumerate(y.columns):
    dy_dx.append(np.gradient(y[columny], x))
print(dy_dx)


y_values = y['AAPL']
y_derivatives = dy_dx[0]
# Interpolacja kubiczna Hermite'a
x_interpolated = np.linspace(min(x), max(x), 100)
spline = CubicHermiteSpline(x, y_values, y_derivatives)
y_inter = spline(x_interpolated)

extrema_x = []
extrema_y = []
zero_crossings = np.where(np.diff(np.sign(y_derivatives)))[0]  # indeksy punktów zmiany znaku pochodnej

for i, enum in enumerate(zero_crossings-1):
    if 0 <= enum < len(x_interpolated):
        extrema_x.append(x_interpolated[enum])
        extrema_y.append(y_inter[enum])
    else:
        continue

plt.scatter(extrema_x, extrema_y, color='blue', label='Dane')
plt.plot(x_interpolated, y_inter, color='red', label='Interpolacja  kubiczna Hermite')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolacja kubiczna Hermite\'a danych')
plt.legend()
plt.show()


road = pd.read_csv("C:\\Users\\piotr\\Downloads\\road_traffic.csv", parse_dates=['Date'])
print(road.isnull().sum())
print(road.dtypes)

x1 = pd.to_datetime(road['Date'], format='%d/%m/%Y')
x1 = x1.map(pd.Timestamp.toordinal)

x1 = x1.astype(float)  # upewniamy się, że można dodać ułamek
offsets = {}

for i in range(len(x1)):
    val = x1[i]
    if val in offsets:
        offsets[val] += 1
    else:
        offsets[val] = 0
    x1[i] += offsets[val] * 0.01  # dodajemy unikalny offset


print(x1)
y = road['Car']

x_train= x1[0:9000]
y_train = road['Car'][0:9000]
print(len(road))

linear_interp = interp1d(x_train, y_train, kind='linear', fill_value='extrapolate')
poly_interp = interp1d(x_train, y_train, kind='cubic', fill_value='extrapolate')
split = CubicSpline(x_train, y_train)

y_cubic = split(x1[9000:len(x1)-1])
y_linear = linear_interp(x1[9000:len(x1)-1])
y_poly = poly_interp(x1[9000:len(x1)-1])

x_predict = x1[9000:len(x1)-1]

print(y[0])
plt.figure(figsize=(14, 6))
# plt.plot(x1, y, 'o', label='Dane z czujnika (z brakami)')
plt.plot(x_predict, y_linear, '-', label='Interpolacja liniowa')
plt.plot(x_predict, y_poly, '--', label='Interpolacja kubiczna (wielomian)')
plt.plot(x_predict, y_cubic, '-.', label='Interpolacja Hermite’a (PCHIP)')
plt.title('Prognozowanie ruchu ulicznego z wykorzystaniem interpolacji')
plt.xlabel('Time')
plt.ylabel('Liczba pojazdów')
plt.legend()
plt.grid(True)
plt.show()

