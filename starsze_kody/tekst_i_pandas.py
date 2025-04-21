import pandas as pd


def hamming(Z1, Z2):
    if len(Z1) == len(Z2):
        count = 0
        for i in range(len(Z1)):
            if Z1[i] != Z2[i]:
                count += 1
        return count
    else:
        return print("Nie Wprowadzono ciągów o tej samej dlugosci")


def hamming2(Z1, Z2):
    if len(Z1) == len(Z2):
        count = 0
        for i in range(len(Z1)):
            if Z1[i] != Z2[i]:
                if Z2[i] in key_neighbors.get(Z1[i], ''):
                    count += 1
                else:
                    count += 2
        return count
    else:
        return "Nie Wprowadzono ciągów o tej samej dlugosci"


def podpunt3zada1(slowo):
    slowo = slowo.lower()
    count = 0
    for w in slownik:
        if slowo == w:
            print("Ok")
            count += 1
    if count == 0:
        podobne_slowa = []
        for w in slownik:
            if len(w) == len(slowo):
                dystans = hamming2(slowo, w)
                podobne_slowa.append((dystans, w))
        podobne_slowa.sort()
        najbardziejpodobneslowa = podobne_slowa[:3]
        return najbardziejpodobneslowa


def zliczanie_wystapienwtekscie(tekst):
    tekst = tekst.lower()
    df2['Liczba wystąpień (%)'] = 0
    for litera in tekst:
        if litera in df2['Letter'].values:
            df2.loc[df2['Letter'] == litera, 'Liczba wystąpień (%)'] += 1
    df2['Liczba wystąpień (%)'] *= (100/len(tekst))

    return df2


def zliczanie_wystapienwtekscie_spol_sam(df_new, tekst, df):
    tekst = tekst.lower()
    for litera in tekst:
        if litera in df['Letter'].values:
            for index, row in df.iterrows():
                if litera == row['Letter']:
                    if index in [0, 4, 8, 14, 20]:
                        df_new.loc[0, 'Liczba wystąpień (%)'] += 1
                    else:
                        df_new.loc[1, 'Liczba wystąpień (%)'] += 1
    df_new['Liczba wystąpień (%)'] *= (100/len(tekst))
    return df_new


def porownywanie_z_jezykami2(df2, df):

    df2['Podob(tekst-ang)(%)'] = (df2['Liczba wystąpień (%)'] - df['Ang(%)']).abs()
    df2['Podob(tekst-niem)(%)'] = (df2['Liczba wystąpień (%)'] - df['Niem(%)']).abs()
    df2['Podob(tekst-pol)(%)'] = (df2['Liczba wystąpień (%)'] - df['Pol(%)']).abs()

    a = df2['Podob(tekst-ang)(%)'].sum() / len(df2)
    b = df2['Podob(tekst-niem)(%)'].sum() / len(df2)
    c = df2['Podob(tekst-pol)(%)'].sum() / len(df2)

    lista = [("ang:", a), ("niem:", b), ("pol:", c)]
    sorted_lista = sorted(lista, key=lambda x: x[1])

    return sorted_lista[0], df2


def liczenie_dl_bez_przerw(slowo, slowo2):
    dl_ciagu_najd = 0
    for i in range(len(slowo)):
        for j in range(len(slowo2)):
            w = 0
            while j+w < len(slowo2) and i+w < len(slowo) and slowo2[j+w] == slowo[i+w]:
                w += 1
            if dl_ciagu_najd < w:
                dl_ciagu_najd = w
    return dl_ciagu_najd


def najdluzszy_wspolny_podciag(slowo1, slowo2):
    m = len(slowo1)
    n = len(slowo2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if slowo1[i - 1] == slowo2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]



#zad1
#1
print(hamming('1234', '1254'))

#2
key_neighbors = {
    'q': 'wa', 'w': 'qes', 'e': 'wsd', 'r': 'edf', 't': 'rfgh', 'y': 'tghj', 'u': 'yhjk', 'i': 'ujkl', 'o': 'iklp', 'p': 'ol',
    'a': 'qws', 's': 'qwed', 'd': 'wersf', 'f': 'ertgd', 'g': 'rtyfh', 'h': 'tyugj', 'j': 'uyhki', 'k': 'uijol', 'l': 'iopk',
    'z': 'asx', 'x': 'zsdc', 'c': 'xdfv', 'v': 'cfgb', 'b': 'vghn', 'n': 'bhjm', 'm': 'njk',
    'Q': 'WA', 'W': 'QES', 'E': 'WSD', 'R': 'EDF', 'T': 'RFVH', 'Y': 'TGHJ', 'U': 'YHJK', 'I': 'UJOL', 'O': 'IKLP', 'P': 'OL',
    'A': 'QWS', 'S': 'QWED', 'D': 'WERSF', 'F': 'ERTGD', 'G': 'RTYFH', 'H': 'TYUGJ', 'J': 'YHIK', 'K': 'UJOL', 'L': 'IOPK',
    'Z': 'ASX', 'X': 'ZSDC', 'C': 'XDFV', 'V': 'CFG', 'B': 'VGHN', 'N': 'BHMJ', 'M': 'NJK',
    '1': '2', '2': '13', '3': '24', '4': '35', '5': '46', '6': '57', '7': '68', '8': '79', '9': '80', '0': '9'
}

s1 = "mama"
s2 = "nawa"
print(hamming2(s1, s2))

#3
slownik = ["kot", "pies", "dom", "auto", "rower", "szkoła", "książka", "komputer", "telefon", "okno", "drzwi", "stół", "krzesło", "zegar", "obraz", "lampa", "kwiat",
           "woda", "jedzenie", "zupa", "chleb", "masło", "ser", "mleko", "kawa", "herbata", "cukier", "sól", "pieprz", "jajko", "mięso", "ryba", "warzywo", "owoc", "jabłko",
           "gruszka", "banan", "pomarańcza", "cytryna", "truskawka", "malina", "jeżyna", "borówka", "wiśnia", "czereśnia", "śliwka", "morela", "brzoskwinia", "winogrono", "arbuz",
           "melon", "pomidor", "ogórek", "sałata", "marchew", "ziemniak", "cebula", "czosnek", "papryka", "burak", "brokuł", "kalafior", "kapusta", "rzodkiewka", "groszek", "fasola",
           "soczewica", "kukurydza", "dynia", "cukinia", "bakłażan", "szpinak", "rukola", "seler", "por", "pietruszka", "koper", "bazylia", "oregano", "tymianek", "rozmaryn", "mięta",
           "majeranek", "lubczyk", "imbir", "kurkuma", "cynamon", "goździk", "wanilia", "gałka muszkatołowa", "pieczywo", "ciasto", "ciasteczko", "bułka", "rogal", "tort", "pizza"]

print(podpunt3zada1("basia"))



#zad2
print("\n")
print("\n")
#1
data = {
    "Letter": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "Ang(%)": [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074],
    "Niem(%)": [7.094, 1.886, 2.732, 5.076, 16.396, 1.656, 3.009, 4.577, 6.550, 0.268, 1.417, 3.437, 2.534, 9.776, 3.037, 0.670, 0.018, 7.003, 7.270, 6.154, 5.161, 0.846, 1.921, 0.034, 0.039, 1.134],
    "Pol(%)": [9.986, 1.482, 4.436 , 3.293, 9.052, 0.312, 1.377, 1.072, 8.286, 2.343, 3.411, 3.882, 2.911, 5.785, 8.413, 3.101, 0.003, 4.571, 4.946, 3.966, 2.347, 0.034, 4.549, 0.019, 3.857, 6.566]
}

df = pd.DataFrame(data)
a = df.sum()

#2
with open('C:/Users/Piotr Nowak/Desktop/Dokumenty_d0_zadania2_algort_Lista5.txt', 'r') as file:
    tekst_z_pliku = file.read()

data2 = {
    "Letter": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
}
df2 = pd.DataFrame(data2)

df2['Liczba wystąpień (%)'] = 0
df2['Podob(tekst-ang)(%)'] = 0
df2['Podob(tekst-niem)(%)'] = 0
df2['Podob(tekst-pol)(%)'] = 0

df2 = zliczanie_wystapienwtekscie(tekst_z_pliku)
najbardziej_podobny, zmod_df2 = porownywanie_z_jezykami2(df2, df)

pd.options.display.max_columns = 5
print(zmod_df2)
pd.options.display.max_columns = None
print("\nNajbardziej podobny język:", najbardziej_podobny)


#3
#tworzenie tabeli
data3 = {
    "Letter": ["samogloski", "spolgloski"],
}
sam_i_spol_tekst = pd.DataFrame(data3, columns=["samogloski", "spolgloski"], dtype='float64')
sam_i_spol_tekst["Ang(%)"] = 0
sam_i_spol_tekst["Niem(%)"] = 0
sam_i_spol_tekst["Pol(%)"] = 0

#dawanie wartosci
sam_i_spol_tekst.loc[0, 'Ang(%)'] = df.loc[[0, 4, 8, 14, 20], "Ang(%)"].sum()
sam_i_spol_tekst.loc[0, 'Niem(%)'] = df.loc[[0, 4, 8, 14, 20], "Niem(%)"].sum()
sam_i_spol_tekst.loc[0, 'Pol(%)'] = df.loc[[0, 4, 8, 14, 20], "Pol(%)"].sum()

df_domody = df
df_domody = df_domody.drop(index = 0)
df_domody = df_domody.drop(index = 4)
df_domody = df_domody.drop(index = 8)
df_domody = df_domody.drop(index = 14)
df_domody = df_domody.drop(index = 20)

sam_i_spol_tekst.loc[1, 'Ang(%)'] = df_domody["Ang(%)"].sum()
sam_i_spol_tekst.loc[1, 'Niem(%)'] = df_domody["Niem(%)"].sum()
sam_i_spol_tekst.loc[1, 'Pol(%)'] = df_domody["Pol(%)"].sum()

print("\n")
print(sam_i_spol_tekst)

#4
data4 = {
    "Letter": ["samogloski", "spolgloski"],
}
sam_i_spol_tekst_z_zew = pd.DataFrame(data4)
sam_i_spol_tekst_z_zew['Liczba wystąpień (%)'] = 0

print("\n")
sam_i_spol_tekst_z_zew = zliczanie_wystapienwtekscie_spol_sam(sam_i_spol_tekst_z_zew, tekst_z_pliku, df)
print(sam_i_spol_tekst_z_zew)

sam_i_spol_tekst_z_zew['Podob(tekst-ang)(%)'] = 0
sam_i_spol_tekst_z_zew['Podob(tekst-niem)(%)'] = 0
sam_i_spol_tekst_z_zew['Podob(tekst-pol)(%)'] = 0

najlepszy_jezyk, sam_i_spol_tekst_z_zew = porownywanie_z_jezykami2(sam_i_spol_tekst_z_zew, sam_i_spol_tekst)
print(f"\nNajlepiej dopasowany jezyk to: {najlepszy_jezyk}")
print(sam_i_spol_tekst_z_zew)


#zad3
#1
print("\n")
print("\n")
najwieksza_dl_podciagu = liczenie_dl_bez_przerw('konwalia', 'zawalina')
print(f"Największa dłufgośc podciągu to: {najwieksza_dl_podciagu}")
#2
slowo1 = "ApqBCrDsEF"
slowo2 = "tABuCvDEwxFyz"
print(f"Największa dłufgośc podciągu z przerwami to: {najdluzszy_wspolny_podciag(slowo1, slowo2)}")
#4?