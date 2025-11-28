import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)

class NeuralNetwork:
    def __init__(self, N_input, H_hidden, M_output):

        self.W1 = np.random.randn(H_hidden, N_input) * 0.01
        self.b1 = np.zeros((H_hidden, 1))

        self.W2 = np.random.randn(M_output, H_hidden) * 0.01

        self.b2 = np.zeros((M_output, 1))

        print("Sieć zainicjalizowana.")
        print(f"Wymiary W1: {self.W1.shape}")
        print(f"Wymiary W2: {self.W2.shape}")

    def forward(self, X):

        # Wzór: Z(1) = W(1)X + b(1)
        Z1 = np.dot(self.W1, X) + self.b1

        # Wzór: A(1) = sigma(Z(1))
        A1 = sigmoid(Z1)

        # Wzór: Z(2) = W(2)A(1) + b(2)
        Z2 = np.dot(self.W2, A1) + self.b2

        # Wzór: Y_hat = A(2) = sigma(Z(2))
        Y_hat = sigmoid(Z2)
        self.cache = {"X": X, "Z1": Z1, "A1": A1, "Z2": Z2, "Y_hat": Y_hat}

        return Y_hat

    def backward(self, Y):

        X = self.cache["X"]
        A1 = self.cache["A1"]
        Z1 = self.cache["Z1"]
        Y_hat = self.cache["Y_hat"]
        Z2 = self.cache["Z2"]

        # Wzór (teoria): delta_2 = (Y_hat - Y) * sigma'(Z2)
        # Używamy funkcji błędu MSE, więc dE/dY_hat = (Y_hat - Y)
        delta_2 = (Y_hat - Y) * sigmoid_derivative(Z2)

        #Obliczanie gradientów dla W2 i b2
        # Wzór (teoria): dE/dW2 = delta_2 * A1.T
        dW2 = np.dot(delta_2, A1.T)

        # Wzór (teoria): dE/db2 = delta_2
        db2 = delta_2

        delta_1 = np.dot(self.W2.T, delta_2) * sigmoid_derivative(Z1)

        # Obliczanie gradientów dla W1 i b1
        dW1 = np.dot(delta_1, X.T)

        db1 = delta_1

        gradients = {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}

        return gradients

    def update_weights(self, gradients, learning_rate):

        self.W1 = self.W1 - learning_rate * gradients["dW1"]
        self.b1 = self.b1 - learning_rate * gradients["db1"]
        self.W2 = self.W2 - learning_rate * gradients["dW2"]
        self.b2 = self.b2 - learning_rate * gradients["db2"]



#Zadanie 3 Uczenie XOR

X_data = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

Y_data = np.array([
    [0],
    [1],
    [1],
    [0]
])


nn = NeuralNetwork(N_input=2, H_hidden=4, M_output=1)

learning_rate = 0.1
epochs = 20000


for epoch in range(epochs):

    total_loss = 0


    for i in range(len(X_data)):


        x_sample = X_data[i].reshape(2, 1) # (N, 1)
        y_sample = Y_data[i].reshape(1, 1) # (M, 1)

        y_hat = nn.forward(x_sample)

        # Używamy MSE (Błąd Średniokwadratowy)
        loss = 0.5 * np.sum((y_hat - y_sample)**2)
        total_loss += loss

        gradients = nn.backward(y_sample)

        nn.update_weights(gradients, learning_rate)

    if (epoch + 1) % 1000 == 0:
        average_loss = total_loss / len(X_data)
        print(f"Epoka: {epoch + 1}/{epochs}, Średni Błąd (Wartość Kryterium): {average_loss:.6f}")

print("--- Uczenie zakończone ---")