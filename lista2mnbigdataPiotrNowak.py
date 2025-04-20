import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zadanie 2
arr = np.arange(1, 11)
max_val = np.max(arr)
min_val = np.min(arr)
mean_val = np.mean(arr)
std_val = np.std(arr)


# Zadanie 3
arr_2d = np.arange(1, 13).reshape(3, 4)
element = arr_2d[1, 2]
sup_tablica = arr_2d[:2, -2:]

# Zadanie 4
arr_1 = np.arange(10)
arr_1 = arr_1.reshape(2, 5)
arr_1 = arr_1.T
print(arr_1)

# Zadanie 5
arr15 = np.array([[1, 2, 3], [4, 5, 6]])
arr25 = np.array([[1, 7, 3], [8, 5, 6]])
sum_arrays = arr15 + arr25
scaled_arr = arr15 * 2


# Zadanie 6
grid = np.arange(9).reshape(3, 3)
row_addition = np.array([1, 2, 3])
row_additionmesh, row_additionmesh1 = np.meshgrid(row_addition, row_addition)
grid_with_addition = grid + row_additionmesh
print(grid_with_addition)
grid_with_addition = grid + row_addition
print(grid_with_addition)
column_scaling = np.array([1, 2, 3]).reshape(3, 1)
grid_scaled = grid * column_scaling

# # Zadanie 7
rand_array = np.random.rand(100)
sum_rand = np.sum(rand_array)
mean_rand = np.mean(rand_array)
std_rand = np.std(rand_array)
cum_sum = np.cumsum(rand_array)
cum_prod = np.cumprod(rand_array)

# Zadanie 8
rand_int_array = np.random.randint(1, 100, size=10)
sorted_array = np.sort(rand_int_array)
search_value = 50
search_index = np.searchsorted(sorted_array, search_value)


# Zadanie 9
sp500 = pd.read_csv("sp500_stock.csv", sep="\s+", index_col=0)
print(sp500.head())
dimensions = sp500.shape
first_rows = sp500.head()
print(dimensions)

sp500["Low"] = pd.to_numeric(sp500["Low"], errors="coerce")
sp500["Volume"] = pd.to_numeric(sp500["Volume"], errors="coerce")
sp500["Close"] = pd.to_numeric(sp500["Close"], errors="coerce")
sp500["High"] = pd.to_numeric(sp500["High"], errors="coerce")
sp500["Open"] = pd.to_numeric(sp500["Open"], errors="coerce")

print(sp500.dtypes)  # Sprawdzenie typów kolumn

# Zadanie 10 Wybór i filtrowanie danych
selected_columns = sp500[['High', 'Low']]
filtered_df = selected_columns[sp500['High'] > 4000]
selected_rows = sp500.iloc[:5]

# Zadanie 11 Oczyszczanie danych
sp500 = sp500.drop_duplicates()
sp500 = sp500.dropna()

sp500["Date"] = sp500.index
sp500["Date"] = sp500["Date"].iloc[2:]
sp500["Date"] = pd.to_datetime(sp500["Date"], format="%Y-%m-%d")
sp500["Year"] = sp500["Date"].dt.year

# Zadanie 12
print(sp500[["Close", "Volume", "High", "Low", "Open"]].describe())

grouped = sp500.groupby("Year").agg(
    {"Close": ["sum", "mean", "count"],
     "Volume": ["sum", "mean"],
    }
)
print(grouped)

# Zadanie 13 Transformacja danych
sp500["Month"] = sp500["Date"].dt.month
sp500["Datestr"] = sp500["Date"].dt.strftime("%Y-%m-%d")
sp500["Datestrrok"] = sp500["Datestr"].str.split("-").str[0]
print(sp500["Datestrrok"])

# Zadanie 14 Wizualizacja danych
plt.figure()
sp500['Close'].plot(kind='bar', title="Wartości w kolumnie Close")
plt.show()
sp500['Close'].plot(title="Wartości w kolumnie Close")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

#zadanie 15
sp500_inne = sp500.copy()
sp500_inne["Suma"] = sp500_inne["Close"].cumsum()
print(sp500_inne)
result = pd.concat([sp500_inne, sp500])
print(result)

sp500long = sp500.melt(id_vars=["Date"], var_name="kolumny", value_name="Wartosc")
sp500long= sp500long[2:]
sp500wide = sp500long.pivot_table(index="Date", columns="kolumny", values="Wartosc", aggfunc="first")
print(sp500wide)
moving_average = sp500['Close'].rolling(window=30).mean()

# Zadanie 16: Wykres liniowy
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)")

ax.set_xlabel('X')
ax.set_ylabel('SINX')
ax.set_title('Sine Wave Plot')
ax.legend()
# plt.show()

# # Zadanie 17: Wykres punktowy
x = np.random.randint(0, 100, 50)
y = np.random.randint(0, 100, 50)
sizes = np.random.randint(10, 100, 100)

fig, ax = plt.subplots()
plt.scatter(x, y, c='r', sizes= sizes, label="Punkty")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scatter Plot')
ax.legend()
# plt.show()

# Zadanie 18: Wykres słupkowy
categories = ['A', 'B', 'C', 'D']
values = [10, 3, 1, 4]
plt.figure()
plt.bar(categories, values, color=['red', 'blue', 'green', 'purple'])
plt.title("Wykres słupkowy")
plt.xlabel("Litery")
plt.ylabel("Ilosc_liter_w_tekscie")
#plt.show()

# # Zadanie 19: Histogram losowanie danych z rozkladu normalnego sr=0 odch = 1
data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=20, color='blue', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Wartości")
plt.ylabel("Częstotliwość")

# Zadanie 20
sizes = [20, 30, 25, 25]
labels = ['A', 'B', 'C', 'D']
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['red', 'blue', 'green', 'purple'])
plt.title("Wykres kołowy")
#plt.show()

#zadanie 21
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
# Creating subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 8))

axes[0, 0].plot(x, y1, color='blue')
axes[0, 0].set_title('Sin(x)')

axes[1, 0].plot(x, y2, color='red')
axes[1, 0].set_title('Cos(x)')

axes[0, 1].scatter(x, y1, color='purple')
axes[0, 1].set_title('Sin(x)')

axes[1, 1].scatter(x, y2, color='black')
axes[1, 1].set_title('Cos(x)')

plt.tight_layout()
plt.show()

# Zadanie 22
# korzystam już z wcześniej zaladowanego zbioru danych sp500
print(sp500.info())
print(sp500.describe())

sp500["Daily Change"] = sp500["Close"] - sp500["Open"]  # Obliczenie dziennych zmian
colors = ["red" if v < 0 else "green" for v in sp500["Daily Change"].cumsum()]
sp500["Daily Change"].cumsum().plot(kind="bar", stacked=True, figsize=(12, 6), color=colors)
plt.locator_params(axis='x', nbins=20)
plt.xlabel("Data", fontsize=12)
plt.xticks(rotation=45, fontsize=8)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.title("Skumulowane zmiany dzienne S&P 500")
plt.xlabel("Dni")
plt.ylabel("Zmiana ceny")
plt.show()

#3d
colors = np.random.rand(len(sp500["Daily Change"]))
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(projection='3d')
ax1.scatter(sp500["Daily Change"], sp500["Volume"], sp500["Close"], c=colors, alpha=0.5)

ax1.set_ylim(min(sp500["Volume"]), max(sp500["Volume"]))
ax1.set_xlabel('Daily Change')
ax1.set_ylabel('Volume')
ax1.set_zlabel('Close')
plt.show()
