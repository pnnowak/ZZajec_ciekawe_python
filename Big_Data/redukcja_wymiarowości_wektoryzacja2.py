import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, NMF
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


#1
def zadanie1():
    mental_health = pd.read_csv("C:\\Users\\piotr\\OneDrive\\Pulpit\\students_mental_health_survey.csv")

    print(mental_health.columns)
    X_doroboty = pd.DataFrame()
    X_doroboty["Stress"] = mental_health["Stress_Level"]
    X_doroboty["Depression_score"] = mental_health["Depression_Score"]
    X_doroboty["Anxiety_score"] = mental_health["Anxiety_Score"]
    X_doroboty["CGPA"] = mental_health["CGPA"].fillna(0)


    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_doroboty)

    # 3. Redukcja wymiarowości do 2D
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    plt.figure(figsize=(10, 7))
    plt.scatter(X_pca[:, 0], X_pca[:, 1])
    plt.xlabel('PCA 1')
    plt.ylabel('PCA 2')
    plt.title('Redukcja wymiarowości danych psychologicznych za pomocą PCA')
    plt.grid(True)
    plt.show()

    # t-SNE
    tsne = TSNE(n_components=2)
    X_embedded1 = tsne.fit_transform(X_scaled)

    plt.scatter(X_embedded1[:, 0], X_embedded1[:, 1])
    plt.title('Wizualizacja danych przy użyciu t-SNE')
    plt.xlabel('Wymiar 1')
    plt.ylabel('Wymiar 2')
    plt.show()

    # # Tworzenie obiektu NMF
    nmf_model = NMF(n_components=3)
    nmf_model.fit(X_doroboty)
    # Pobranie macierzy bazowych i wagowych
    W = nmf_model.transform(X_doroboty)
    H = nmf_model.components_

    # Wyświetlenie macierzy bazowych i wagowych
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(W, cmap='viridis', aspect='auto')
    plt.title('Macierz bazowa (W)')
    plt.xlabel('Składowe')
    plt.ylabel('Próbki')
    plt.subplot(1, 2, 2)
    plt.imshow(H, cmap='viridis', aspect='auto')
    plt.title('Macierz wagowa (H)')
    plt.xlabel('Cechy')
    plt.ylabel('Składowe')
    plt.tight_layout()
    plt.show()



