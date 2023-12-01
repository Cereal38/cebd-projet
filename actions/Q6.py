import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils import db, display

CODE_DEPARTEMENT = '56'


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(1200, 800, self)
        self.title('Q6 : Graphique correlation temperatures minimales - coût de travaux')
  #       display.defineGridDisplay(self, 2, 1)
  #       ttk.Label(self, text="""Pour l’Isère et l'année 2022, donner deux courbes sur le même graphique  :
  #  - par annee, l’évolution de la moyenne des températures minimales
  #  - par annee, l’évolution des totaux de coûts de travaux tout type confondu""",
  #                 wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0)

        # Average min temperature by year in the department
        queryTmin = """SELECT AVG(temperature_min_mesure), strftime('%Y', date_mesure) as annee
              FROM Mesures JOIN Departements USING (code_departement)
              WHERE code_departement = """ + CODE_DEPARTEMENT + """
              GROUP BY annee
              ORDER BY annee"""
        
        # Total cost of chauffage by year in the department
        queryCostChauffage = """SELECT SUM(cout_total_ht_chauffage), annee_chauffage as annee
              FROM Chauffages JOIN Departements USING (code_departement)
              WHERE code_departement = """ + CODE_DEPARTEMENT + """
              GROUP BY annee
              ORDER BY annee"""
        
        queryCostIsolation = """SELECT SUM(cout_total_ht_isolation), annee_isolation as annee
              FROM Isolations JOIN Departements USING (code_departement)
              WHERE code_departement = """ + CODE_DEPARTEMENT + """
              GROUP BY annee
              ORDER BY annee"""

        queryCostPhotovoltaique = """SELECT SUM(cout_total_ht_photovoltaique), annee_photovoltaique as annee
              FROM Photovoltaiques JOIN Departements USING (code_departement)
              WHERE code_departement = """ + CODE_DEPARTEMENT + """
              GROUP BY annee
              ORDER BY annee"""
        
        # Get data in array
        cursor = db.data.cursor()
        resultTmin = []
        for row in cursor.execute(queryTmin):
            resultTmin.append(row)
        resultChauffage = []
        for row in cursor.execute(queryCostChauffage):
            resultChauffage.append(row)
        resultIsolation = []
        for row in cursor.execute(queryCostIsolation):
            resultIsolation.append(row)
        resultPhotovoltaique = []
        for row in cursor.execute(queryCostPhotovoltaique):
            resultPhotovoltaique.append(row)
        cursor.close()

        annee = []
        tmin = []
        cost = []

        # Fill annee
        for row in resultTmin:
            if row[1] is not None and int(row[1]) not in annee:
                annee.append(int(row[1]))
        for row in resultChauffage:
            if row[1] is not None and int(row[1]) not in annee:
                annee.append(int(row[1]))
        for row in resultIsolation:
            if row[1] is not None and int(row[1]) not in annee:
                annee.append(int(row[1]))
        for row in resultPhotovoltaique:
            if row[1] is not None and int(row[1]) not in annee:
                annee.append(int(row[1]))
        annee.sort()

        # Fill tmin by adding value at the right index
        for i in range(len(annee)):
            tmin.append(0)
        for row in resultTmin:
            if row[1] is not None:
                tmin[annee.index(int(row[1]))] = row[0]
        
        # Fill cost by adding value at the right index
        for i in range(len(annee)):
            cost.append(0)
        for row in resultChauffage:
            if row[1] is not None:
                cost[annee.index(int(row[1]))] = row[0]
        for row in resultIsolation:
            if row[1] is not None:
                cost[annee.index(int(row[1]))] += row[0]
        for row in resultPhotovoltaique:
            if row[1] is not None:
                cost[annee.index(int(row[1]))] += row[0]

        # Plot data
        # 1 x axis for 2 y axis
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot(annee, tmin, 'g-')
        ax2.plot(annee, cost, 'b-')
        ax1.set_xlabel('Annee')
        ax1.set_ylabel('Temperature minimale moyenne (°C)', color='g')
        ax2.set_ylabel('Coût total (€)', color='b')
        ax1.tick_params(axis='y', labelcolor='g')
        ax2.tick_params(axis='y', labelcolor='b')
        plt.title('Evolution des températures minimales et des coûts de travaux en fonction de l\'année (Département ' + CODE_DEPARTEMENT + ')')
        plt.grid(True)

        # Affichage du graphique (Prend toute la fenêtre)
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




        
        
