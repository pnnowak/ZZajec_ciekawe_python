class Perceptron:

    def __init__(self, wagi, prog):
        self.w = wagi
        self.theta = prog
        self.liczba_wejsc = len(wagi)
        print(f"Stworzono perceptron z wagą w1={self.w}, dlu wag: {self.liczba_wejsc} i progiem theta={self.theta}")

    def obliczanie_s(self, x):
        if self.liczba_wejsc != len(x):
            print("Błąd")
            raise ValueError(f"Zła liczba wejść! Oczekiwano {self.liczba_wejsc}, a otrzymano {len(x)}")
        s = 0
        for i in range(self.liczba_wejsc):
            s += self.w[i] * x[i]
        return s

    # unipolarny perceptron
    def przewiduj_uni(self, x):
        wy = self.obliczanie_s(x)
        if wy >= self.theta:
            return 1
        else:
            return 0

    # bipolarny perceptron
    def przewiduj_bi(self, x):
        wy = self.obliczanie_s(x)
        if wy >= self.theta:
            return 1
        else:
            return -1

    def trenuj_uni(self, X_uczace, D_oczekiwane, alpha, max_epok):
        print(f"Parametry: alpha={alpha}, max_epok={max_epok}")
        print(f"Stan początkowy: wagi={self.w}, prog={self.theta}")

        for epoka in range(max_epok):

            calkowity_blad_epoki = 0

            for (x, d) in zip(X_uczace, D_oczekiwane):
                print("\n")
                print("Iteracja")
                y = self.przewiduj_uni(x)
                e = d - y
                print(f"x: {x} d: {d}")
                print(f"wagi: {self.w}")
                print(f"próg: {self.theta}")
                print(f"y: {y}")
                print(f"e: {e}")
                print("\n")

                if e != 0:
                    calkowity_blad_epoki += 1

                    # Korekta wag (wzór: w_nowe = w_stare + alpha * e * x) liczba wejsc = 2
                    for i in range(self.liczba_wejsc):
                        self.w[i] = self.w[i] + alpha * e * x[i]

                    # Korekta progu (wzór: theta_nowe = theta_stare - alpha * e)
                    self.theta = self.theta - alpha * e

            # chat
            print(f"Epoka {epoka+1:03d} | Błędy: {calkowity_blad_epoki:02d} | Wagi: {[round(w, 2) for w in self.w]} | Prog: {round(self.theta, 2)}")

            if calkowity_blad_epoki == 0:
                print("--- Trening zakończony sukcesem (brak błędów) ---")
                return

        print("--- Trening zakończony (osiągnięto limit epok) ---")


#zadanie1
#1D Perceptron
peruni1 = Perceptron([0.5],0.2)
print(peruni1.przewiduj_uni([1]))

peruni1 = Perceptron([0.5],0.6)
print(peruni1.przewiduj_bi([1]))

#2D Perceptron
peruni1 = Perceptron([0.5, 0.5],0.8)
print(peruni1.przewiduj_uni([1, 0]))

peruni1 = Perceptron([0.5, 0.5],0.6)
print(peruni1.przewiduj_bi([1, 0]))

#zad2
print("\n")

def perceptron_i_wyswietlanie_wynikow(X_uczace, D_oczekiwane, alpha, max_epok, perce_1):

    perce_1.trenuj_uni(X_uczace, D_oczekiwane, alpha, max_epok)

    # chat
    print("\n Testowanie po nauce")
    for i, x in enumerate(X_uczace):
        y = perce_1.przewiduj_uni(x)
        print(f"We: {x} -> Wy: {y} (Oczekiwano: {D_oczekiwane[i]})")
    return "Koniec"


print("zadanie2")

print("\n")
X_uczace = [[0, 0], [0, 1], [1, 0], [1, 1]]
D_oczekiwane = [0,0,0,1]

X_uczace_OR = [[0, 0], [0, 1], [1, 0], [1, 1]]
D_oczekiwane_OR = [0, 1, 1, 1]

X_uczace_NOT = [[0], [1]]
D_oczekiwane_NOT = [1, 0]

X_uczace_XOR = [[0, 0], [0, 1], [1, 0], [1, 1]]
D_oczekiwane_XOR = [0, 1, 1, 0]

perce_1 = Perceptron([0.0, 0.0],0.0)
perce_2 = Perceptron([0.0, 0.0],0.0)
perce_3 = Perceptron([0.0],0.0)
perce_4 = Perceptron([0.0, 0.0],0.0)

alpha = 0.1
max_epok = 10
max_epok_XOR = 20

#wyniki
print("\n")
print("AND")
perceptron_i_wyswietlanie_wynikow(X_uczace, D_oczekiwane, alpha, max_epok, perce_1)
print("\n")
print("OR")
perceptron_i_wyswietlanie_wynikow(X_uczace_OR, D_oczekiwane_OR, alpha, max_epok, perce_2)
print("\n")
print("NOT")
perceptron_i_wyswietlanie_wynikow(X_uczace_NOT, D_oczekiwane_NOT, alpha, max_epok, perce_3)
print("\n")
print("XOR")
perceptron_i_wyswietlanie_wynikow(X_uczace_XOR, D_oczekiwane_XOR, alpha, max_epok_XOR, perce_4)
print("XOR: Nie da się narysować jednej prostej linii, która oddzieliłaby punkty (0,1) i (1,0) od (0,0) i (1,1).")