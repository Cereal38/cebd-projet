import tkinter as tk
from tkinter import ttk

from utils import display


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q1 : départements de la région Auvergne-Rhône-Alpes')
        display.defineGridDisplay(self, 2, 1)

        # On définit les colonnes que l'on souhaite afficher dans la fenêtre et la requête
        columns = ('code_departement', 'nom_departement')
        query = """SELECT code_departement, nom_departement
                    FROM Departements JOIN Regions USING (code_region) 
                    WHERE nom_region = 'AUVERGNE RHONE ALPES'
                    ORDER BY nom_region"""

        # On utilise la fonction createTreeViewDisplayQuery pour afficher les résultats de la requête
        tree = display.createTreeViewDisplayQuery(self, columns, query,200)
        tree.grid(row=0, sticky="nswe")
