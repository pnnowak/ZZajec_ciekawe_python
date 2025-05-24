from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, confusion_matrix
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import cross_val_score


data = load_iris()
X = data.data
y = data.target

labelen = LabelEncoder()
stanscal = StandardScaler()

X = stanscal.fit_transform(X)
y = labelen.fit_transform(y)

# random_state=42 zawsze ten sam "losowy" podział
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, random_state=42)

# SVM
svm_model = SVC(probability=True)
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
y_pred_svm1 = svm_model.predict_proba(X_test)
scores = cross_val_score(svm_model, X, y, cv=10, scoring='accuracy')

# k-sasiadów
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_predknn = knn.predict(X_test)
y_predknn1 = knn.predict_proba(X_test)
scoresknn = cross_val_score(knn, X, y, cv=10, scoring='accuracy')

# drzewa decyzyjne
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred_dd = clf.predict(X_test)
y_pred_dd1 = clf.predict_proba(X_test)
scoresdd = cross_val_score(clf, X, y, cv=10, scoring='accuracy')

# Inicjalizacja i trenowanie modelu NBC
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)
y_pred_GNB = nb_classifier.predict(X_test)
y_pred_GNB1 = nb_classifier.predict_proba(X_test)
scoresgnb = cross_val_score(nb_classifier, X, y, cv=10, scoring='accuracy')

def obliczanie_rzeczy(y_pred, y_pred1):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='micro')
    recall = recall_score(y_test, y_pred, average='micro')
    # y_pred1 = y_pred.reshape(-1, 1)
    if y_pred1 is not False:
        roc_auc = roc_auc_score(y_test, y_pred1, multi_class='ovr')

    conf_matrix = confusion_matrix(y_test, y_pred)
    print("Dokładność:", accuracy)
    print("Precyzja:", precision)
    print("Czułość:", recall)
    if y_pred1 is not False:
        print("AUC:", roc_auc)
    print("Macierz pomyłek:")
    print(conf_matrix)

# wyniki

#drzewa
print("Svm")
obliczanie_rzeczy(y_pred_svm, y_pred_svm1)
print("Wyniki dla każdego folda:", scores)
print("Średnia dokładność crossval:", scores.mean())

print("\n")
print("Knn")
obliczanie_rzeczy(y_predknn, y_predknn1)
print("Wyniki dla każdego folda:", scoresknn)
print("Średnia dokładność crossval:", scoresknn.mean())

print("\n")
print("Gauss")
obliczanie_rzeczy(y_pred_GNB, y_pred_GNB1)
print("Wyniki dla każdego folda:", scoresgnb)
print("Średnia dokładność crossval:", scoresgnb.mean())

print("\n")
print("drzewa")
obliczanie_rzeczy(y_pred_dd, y_pred_dd1)
print("Wyniki dla każdego folda:", scoresdd)
print("Średnia dokładność crossval:", scoresdd.mean())
