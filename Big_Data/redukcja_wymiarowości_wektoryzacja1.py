import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, load_digits, load_wine, fetch_20newsgroups
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA, LatentDirichletAllocation
from sklearn.manifold import TSNE
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


data = load_breast_cancer()
X = data.data
y = data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Redukcja wymiarowości do 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)


plt.figure(figsize=(10, 7))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='coolwarm', edgecolor='k', s=60)
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('Redukcja wymiarowości danych Breast Cancer za pomocą PCA')
plt.colorbar(label='Klasa (0 = złośliwy, 1 = łagodny)')
plt.grid(True)
plt.show()

#2
litery = load_digits()
X1 = data.data
y1 = data.target


tsne = TSNE(n_components=2)
X_embedded1 = tsne.fit_transform(X1)

plt.scatter(X_embedded1[:, 0], X_embedded1[:, 1])
plt.title('Wizualizacja danych przy użyciu t-SNE')
plt.xlabel('Wymiar 1')
plt.ylabel('Wymiar 2')
plt.show()

#4
datax = load_wine()
Xy = datax.data
y = datax.target

U,s,VT = np.linalg.svd(Xy)
k = 2

rocent = sum(s[:k])/sum(s)
print(rocent)
#kolo 98 rocent czyli więcej niż 95
# Zredukowane dane
reduced_data = np.dot(U[:, :k], np.diag(s[:k]))

plt.scatter(reduced_data[:, 0], reduced_data[:, 1])
plt.title('Wizualizacja danych przy użyciu SVD')
plt.xlabel('Wymiar 1')
plt.ylabel('Wymiar 2')
plt.show()


newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
documents = newsgroups.data[:1000]  # ograniczamy liczbę dokumentów dla szybkości

# 2. Zamień tekst na wektory (z angielskimi stopwords)
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
X = vectorizer.fit_transform(documents)

lda = LatentDirichletAllocation(n_components=3, random_state=42)
lda_output = lda.fit_transform(X)

# 4. ile dokumentów przypisano do każdego tematu
topic_distribution = pd.DataFrame(lda_output, columns=[f"Topic {i}" for i in range(1, 11)])
dominant_topic = topic_distribution.idxmax(axis=1)

plt.figure(figsize=(10, 6))
dominant_topic.value_counts().sort_index().plot(kind='bar')
plt.title("Document count per dominant topic (LDA)")
plt.xlabel("Topic")
plt.ylabel("Number of Documents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




