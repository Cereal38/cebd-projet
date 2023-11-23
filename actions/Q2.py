import tkinter as tk
from tkinter import ttk

from utils import display


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q2 : département le plus froid par région')
        display.defineGridDisplay(self, 3, 1)

        columns = ('nom_region', 'nom_departement', 'temperature_moy_min')
        query = """
                    WITH TempMoy AS (
                        SELECT code_departement, AVG(temperature_moy_mesure) AS temperature_moy_mesure
                        FROM Mesures
                        GROUP BY code_departement
                    ), TempMin AS (
                        SELECT nom_region, nom_departement, ROUND(MIN(temperature_moy_mesure), 2) AS temperature_moy_min
                        FROM TempMoy JOIN Departements USING (code_departement) JOIN Regions USING (code_region) 
                        GROUP BY nom_region
                    )
                    SELECT * FROM TempMin"""
        # On utilise la fonction createTreeViewDisplayQuery pour afficher les résultats de la requête
        tree = display.createTreeViewDisplayQuery(self, columns, query,200)
        tree.grid(row=0, sticky="nswe")
