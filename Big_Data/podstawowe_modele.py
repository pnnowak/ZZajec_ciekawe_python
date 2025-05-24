import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score


# 1. Regresja liniowa - ceny mieszkań
apart = pd.read_csv('appartments.csv')
X_housing = apart.drop(columns=['price'])
y_housing = apart['price']
X_train, X_test, y_train, y_test = train_test_split(X_housing, y_housing, test_size=0.2, random_state=42)
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
print("Regresja Liniowa: MSE:", mean_squared_error(y_test, y_pred), "R2:", r2_score(y_test, y_pred))
plt.scatter(y_test, y_pred)
plt.xlabel("Rzeczywiste ceny")
plt.ylabel("Przewidywane ceny")
plt.title("Regresja Liniowa - ceny mieszkań")
plt.show()

# # 2. Regresja wielomianowa - temperatura vs miesiące
temenerg = pd.read_csv("C:\\Users\\Piotr\\Downloads\\temperature_and_energy_consumption.csv")

temenerg['time_n'] = pd.to_datetime(temenerg['time_n'], format="%Y-%m-%d")
temenerg['Mouth'] = temenerg['time_n'].dt.month

X_temp = temenerg[['Mouth']]
y_temp = temenerg['temperature']

X_train, X_test, y_train, y_test = train_test_split(X_temp, y_temp, test_size=0.2, random_state=42)
poly = PolynomialFeatures(degree=3)
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)
poly_reg = LinearRegression()
poly_reg.fit(X_poly_train, y_train)
y_pred = poly_reg.predict(X_poly_test)
print("Regresja Wielomianowa: MSE:", mean_squared_error(y_test, y_pred), "R2:", r2_score(y_test, y_pred))
plt.scatter(X_test, y_test, color='blue')
plt.scatter(X_test, y_pred, color='red')
plt.xlabel("Miesiąc")
plt.ylabel("Temperatura")
plt.title("Regresja Wielomianowa")
plt.show()

#3. Regresja grzbietowa i Lasso - zużycie energii vs temperatura
energy_data = pd.read_csv("C:\\Users\\Piotr\\Downloads\\temperature_and_energy_consumption.csv")

X_energy = energy_data[['temperature']]
y_energy = energy_data['energy_consumption']

def trenowanie_modeli(alpha1, alpha2):
    X_train, X_test, y_train, y_test = train_test_split(X_energy, y_energy, test_size=0.2, random_state=42)
    ridge = Ridge(alpha=alpha1)
    ridge.fit(X_train, y_train)
    y_pred_ridge = ridge.predict(X_test)

    lasso = Lasso(alpha=alpha2)
    lasso.fit(X_train, y_train)
    y_pred_lasso = lasso.predict(X_test)

    return y_pred_ridge, y_pred_lasso, X_test, y_test

for i, enum in enumerate([10, 1, 40000, 0.5, 4, 0.001]):
    pred1ridge, pred1lasso, X_test_mew, y_test_new = trenowanie_modeli(enum, enum)
    print("Regresja Grzbietowa: MSE:", mean_squared_error(y_test_new, pred1ridge), "R2:", r2_score(y_test_new, pred1ridge))
    print("Regresja Lasso: MSE:", mean_squared_error(y_test_new, pred1lasso), "R2:", r2_score(y_test_new, pred1lasso))
    #10 najlepsze


y_pred_ridge, y_pred_lasso, X_test, y_test = trenowanie_modeli(10, 10)
plt.scatter(X_test, y_test, color='blue', label="Rzeczywiste")
plt.scatter(X_test, y_pred_ridge, color='red', label="Grzbietowa")
plt.plot(X_test, y_pred_lasso, color='green', label="Lasso")
plt.xlabel("Temperatura")
plt.ylabel("Zużycie energii")
plt.title("Regresja Grzbietowa vs Lasso")
plt.legend()
plt.show()

X_train2, X_test2, y_train2, y_test2 = train_test_split(X_energy, y_energy, test_size=0.2, random_state=42)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_train2, y_train2)
y_pred1 = lin_reg2.predict(X_test2)
print("\n")
print("Regresja liniowa: MSE:", mean_squared_error(y_test2, y_pred1), "R2:", r2_score(y_test2, y_pred1))


# 4. Regresja SVR - czas przeżycia pacjentów
patients_data = pd.read_csv("C:\\Users\\piotr\\Downloads\\dane_medyczne.csv")
X_patients = patients_data.drop(columns=['czas_przezycia'])
y_patients = patients_data['czas_przezycia']
X_train, X_test, y_train, y_test = train_test_split(X_patients, y_patients, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

for i, enum in enumerate([5, 1, 9, 0.5, 0.001]):
    svr = SVR(kernel='linear', C=enum)
    svr.fit(X_train_scaled, y_train)
    y_pred_svr = svr.predict(X_test_scaled)
    print("Regresja SVR linear: MSE:", mean_squared_error(y_test, y_pred_svr), "R2:", r2_score(y_test, y_pred_svr))

    svr = SVR(kernel='rbf', C=enum)
    svr.fit(X_train_scaled, y_train)
    y_pred_svr = svr.predict(X_test_scaled)
    print("Regresja SVR rbf: MSE:", mean_squared_error(y_test, y_pred_svr), "R2:", r2_score(y_test, y_pred_svr))

    svr = SVR(kernel='poly', C=enum, degree=3)
    svr.fit(X_train_scaled, y_train)
    y_pred_svr = svr.predict(X_test_scaled)
    print("Regresja SVR poly: MSE:", mean_squared_error(y_test, y_pred_svr), "R2:", r2_score(y_test, y_pred_svr))
    print("\n")
    #nailepsze wyniki liniowy i rbf dla dwóch pierwszych


svr = SVR(kernel='linear', C=1)
svr.fit(X_train_scaled, y_train)
y_pred_svr1 = svr.predict(X_test_scaled)
print("Regresja SVR linear: MSE:", mean_squared_error(y_test, y_pred_svr1), "R2:", r2_score(y_test, y_pred_svr1))

svr = SVR(kernel='rbf', C=1)
svr.fit(X_train_scaled, y_train)
y_pred_svr = svr.predict(X_test_scaled)
print("Regresja SVR rbf: MSE:", mean_squared_error(y_test, y_pred_svr), "R2:", r2_score(y_test, y_pred_svr))

plt.scatter(y_test, y_pred_svr1, label="linear")
plt.scatter(y_test, y_pred_svr, label="rbf")
plt.xlabel("Rzeczywisty czas przeżycia")
plt.ylabel("Przewidywany czas przeżycia")
plt.title("Regresja SVR")
plt.show()
