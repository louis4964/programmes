from math import * 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def complexe_carre(X, Y):
    # Création de la grille
    x, y = np.meshgrid(X, Y)
    Z = np.sqrt(x**2 + y**2)

    # Création de la figure
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Tracé de la surface
    surface = ax.plot_surface(x, y, Z, cmap='viridis', edgecolor='none')

    # Ajout d'une barre de couleur
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

    # Ajout des étiquettes et du titre
    ax.set_title("f : z --> z^2")
    ax.set_xlabel("Re(Z)")
    ax.set_ylabel("Im(Z)")
    ax.set_zlabel("Module de Z")

    # Affichage
    plt.show()

def complexe_cube(X,Y):
    # Création de la grille
    x, y = np.meshgrid(X, Y)
    # (x + iy)^3 = ( x**3 - 3*x*y**2) + i(3*x**2*y - y**2)
    Z = np.sqrt(( x**3 - 3*x*y**2)**2 + (3*x**2*y - y**2)**2)

    # Création de la figure
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Tracé de la surface
    surface = ax.plot_surface(x, y, Z, cmap='viridis', edgecolor='none')

    # Ajout d'une barre de couleur
    fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

    # Ajout des étiquettes et du titre
    ax.set_title("f : z --> z^3")
    ax.set_xlabel("Re(Z)")
    ax.set_ylabel("Im(Z)")
    ax.set_zlabel("Module de Z")

    # Affichage
    plt.show()

# Exemple d'utilisation
X = np.linspace(-100, 100, 200)
Y = np.linspace(-100, 100, 200)
complexe_carre(X, Y)
#complexe_cube(X,Y)


