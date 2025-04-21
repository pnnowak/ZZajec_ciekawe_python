import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure
import scipy.integrate as si


def eulera_dla_Lotki_Volterry(x, y, dt, n):
    for i in range(n-1):
        dx = (a - b * y[i]) * x[i]
        dy = (c * x[i] - d) * y[i]
        x[i+1] = x[i] + dt*dx
        y[i+1] = y[i] + dt * dy
    return x, y

def eulera_dla_układu_lorenza(x, y, z, dt, n):
    for i in range(n-1):

        dx = (y[i] - x[i]) * sigma
        dy = (rho-z[i])*x[i] - y[i]
        dz =  x[i] * y[i] - beta * z[i]

        x[i+1] = x[i] + dt * dx
        y[i+1] = y[i] + dt * dy
        z[i+1] = z[i] + dt * dz

    return x, y, z

def do_odeinta_LV(xy, t):
    x, y = xy
    dx = (a - b * y) * x
    dy = (c * x - d) * y
    return [dx, dy]

def do_odeinta_UK(xyz,t):
    x, y, z = xyz
    dx = (y - x) * sigma
    dy = (rho - z) * x - y
    dz = x * y - beta * z

    return [dx, dy, dz]

def rysowanie_wykresow(x, y):
    plt.plot(t, y)
    plt.plot(t, x)
    plt.xlabel('Czas')
    plt.ylabel('Liczba populacji')
    plt.legend(['Populacja ofiar', 'Polulacja drapieżników'], fontsize='small')
    plt.show()


def rysowanie_wykresowxy(x, y):
    plt.plot(x, y)

    plt.xlabel('X')
    plt.ylabel('Y')

    plt.title("Uklad Lorenza")
    plt.show()

def rysowanie_wykresowxz(x, y):
    plt.plot(x, y)

    plt.xlabel('X')
    plt.ylabel('Z')
    plt.title("Uklad Lorenza")
    plt.show()

def rysowanie_wykresowyz(x, y):
    plt.plot(x, y)

    plt.xlabel('Y')
    plt.ylabel('Z')
    plt.title("Uklad Lorenza")
    plt.show()

def wykres_w_3d(xc, yc, zc):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(xc, yc, zc)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Układ Lorenza')

    plt.show()

x = input("Wpisz LV dla kodu Lotki-Volterry, UL dla układu Lorenza: ")
dt = float(input("Wpisz krok symulacji, do wyboru [0.08, 0.02, 0.001]: "))

if x == "LV":
    a = 1.2
    b = 0.6
    c = 0.3
    d = 0.8

    tsp = [0, 25]


    t = np.arange(tsp[0], tsp[1]+dt, dt)

    n = len(t)

    y = np.zeros(n)
    x = np.zeros(n)
    x[0] = 2
    y[0] = 1

    #1 Eulera dla lotki volterry

    xc, yc = eulera_dla_Lotki_Volterry(x, y, dt, n)
    print("Eulera")
    rysowanie_wykresow(xc, yc)

    #2 odeint

    solution = si.odeint(do_odeinta_LV, [x[0], y[0]], t)
    x_solution = solution[:, 0]
    y_solution = solution[:, 1]

    print("Odeint")
    rysowanie_wykresow(x_solution, y_solution)

    #3 Obliczanie średniego błędu aproksymacji dla 1Eulera
    t = np.arange(tsp[0], tsp[1]+dt, dt)

    y1 = np.zeros((2, n))
    y1[0, :] = xc
    y1[1, :] = yc

    mean_error1 = np.mean(np.abs(solution.T - y1))
    print("Średni błąd aproksymacji dla", dt, ":", mean_error1)


elif x == "UL":
    sigma = 10
    beta = 8/3
    rho = 28


    tspan = [0, 25]
    t = np.arange(tspan[0], tspan[1]+dt, dt)
    n = len(t)

    y = np.zeros(n)
    x = np.zeros(n)
    z = np.zeros(n)

    x[0] = y[0] = z[0] = 1



    #1 Metoda Eulera
    xc, yc, zc = eulera_dla_układu_lorenza(x, y, z, dt, n)
    print("Eulera")
    rysowanie_wykresowxy(xc, yc)
    rysowanie_wykresowxz(xc, zc)
    rysowanie_wykresowyz(yc, zc)

    wykres_w_3d(xc, yc, xc)

    #2 odeint


    solution = si.odeint(do_odeinta_UK, [x[0], y[0], z[0]], t)
    x_solution = solution[:, 0]
    y_solution = solution[:, 1]
    z_solution = solution[:, 2]

    print("Odeint")
    rysowanie_wykresowxy(x_solution, y_solution)
    rysowanie_wykresowxz(x_solution, z_solution)
    rysowanie_wykresowyz(y_solution, z_solution)

    wykres_w_3d(x_solution, y_solution, z_solution)

    #3 Obliczanie średniego błędu aproksymacji dla 1Eulera
    t = np.arange(tspan[0], tspan[1]+dt, dt)

    y1 = np.zeros((3, n))
    y1[0, :] = xc
    y1[1, :] = yc
    y1[2, :] = zc

    mean_error1 = np.mean(np.abs(solution.T - y1))
    print("Średni błąd aproksymacji dla", dt, ":", mean_error1)
else:
    print("zle wybrana litera")
