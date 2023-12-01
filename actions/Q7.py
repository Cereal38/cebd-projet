import sqlite3
import tkinter as tk
from tkinter import ttk

from utils import db, display


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Définition de la taille de la fenêtre, du titre et des lignes/colonnes de l'affichage grid
        display.centerWindow(600, 400, self)
        self.title('Q7 : gérer les travaux de rénovation')
        display.defineGridDisplay(self, 1, 1)
        #ttk.Label(self, text="""Proposer des fonctionnalités permettant de gérer l'ajout, modification et suppression pour un type de travaux""",
        #          wraplength=500, anchor="center", font=('Helvetica', '10', 'bold')).grid(sticky="we", row=0)

        # On définis les onglets pour chaque travaux
        tabControl = ttk.Notebook(self)
        tabIsolation = ttk.Notebook(tabControl)
        tabChauffage = ttk.Notebook(tabControl)
        tabPhotovoltaique = ttk.Notebook(tabControl)
        tabControl.add(tabIsolation, text='Isolation')
        tabControl.add(tabChauffage, text='Chauffage')
        tabControl.add(tabPhotovoltaique, text='Photovoltaique')

        # Maintenant pour chaque onglet travaux on définis les onglets d'ajout, modification et suppressions
        tabIsolation1 = ttk.Frame(tabIsolation)
        tabIsolation2 = ttk.Frame(tabIsolation)
        tabIsolation3 = ttk.Frame(tabIsolation)
        tabChauffage1 = ttk.Frame(tabChauffage)
        tabChauffage2 = ttk.Frame(tabChauffage)
        tabChauffage3 = ttk.Frame(tabChauffage)
        tabPhotovoltaique1 = ttk.Frame(tabPhotovoltaique)
        tabPhotovoltaique2 = ttk.Frame(tabPhotovoltaique)
        tabPhotovoltaique3 = ttk.Frame(tabPhotovoltaique)
        tabIsolation.add(tabIsolation1, text='Ajouter')
        tabIsolation.add(tabIsolation2, text='Modifier')
        tabIsolation.add(tabIsolation3, text='Supprimer')
        tabChauffage.add(tabChauffage1, text='Ajouter')
        tabChauffage.add(tabChauffage2, text='Modifier')
        tabChauffage.add(tabChauffage3, text='Supprimer')
        tabPhotovoltaique.add(tabPhotovoltaique1, text='Ajouter')
        tabPhotovoltaique.add(tabPhotovoltaique2, text='Modifier')
        tabPhotovoltaique.add(tabPhotovoltaique3, text='Supprimer')


        display.defineGridDisplay(tabIsolation1, 11, 2)
        display.defineGridDisplay(tabIsolation2, 13, 2)
        display.defineGridDisplay(tabIsolation3, 2, 2)
        tabIsolation3.grid_rowconfigure(2, weight=10)
        display.defineGridDisplay(tabChauffage1, 11, 2)
        display.defineGridDisplay(tabChauffage2, 13, 2)
        display.defineGridDisplay(tabChauffage3, 2, 2)
        tabChauffage3.grid_rowconfigure(2, weight=10)
        display.defineGridDisplay(tabPhotovoltaique1, 9, 2)
        display.defineGridDisplay(tabPhotovoltaique2, 11, 2)
        display.defineGridDisplay(tabPhotovoltaique3, 3, 2)
        tabPhotovoltaique3.grid_rowconfigure(2, weight=10)
        tabControl.grid(row=0, column=0, sticky="nswe")

        #On va definir les case d'écriture pour les ajouts
        Isolation = []
        cout_total_ht_Isolation_Modif1 = ttk.Label(tabIsolation1, text='cout total ht').grid(row=0, column= 0, sticky="e")
        cout_induit_ht_Isolation_Modif1 = ttk.Label(tabIsolation1, text='cout induit ht').grid(row=1, column= 0, sticky="e")
        annee_Isolation_Modif1 = ttk.Label(tabIsolation1, text='annee isolation').grid(row=2, column= 0, sticky="e")
        type_logement_Isolation_Modif1 = ttk.Label(tabIsolation1, text='type logement').grid(row=3, column= 0, sticky="e")
        annee_construction_logement_Isolation_Modif1 = ttk.Label(tabIsolation1, text='annee construction logement').grid(row=4, column= 0, sticky="e")
        code_departement_Isolation_Modif1 = ttk.Label(tabIsolation1, text='code departement').grid(row=5, column= 0, sticky="e")
        poste_Isolation_Modif1 = ttk.Label(tabIsolation1, text='poste isolation').grid(row=6, column= 0, sticky="e")
        isolant_Isolation_Modif1 = ttk.Label(tabIsolation1, text='isolant').grid(row=7, column= 0, sticky="e")
        epaisseur_Isolation_Modif1 = ttk.Label(tabIsolation1, text='epaisseur').grid(row=8, column= 0, sticky="e")
        surface_Isolation_Modif1 = ttk.Label(tabIsolation1, text='surface').grid(row=9, column= 0, sticky="e")
        cout_total_ht_Isolation = tk.StringVar()
        cout_induit_ht_Isolation = tk.StringVar()
        annee_Isolation = tk.StringVar()
        type_logement_Isolation = tk.StringVar()
        annee_construction_logement_Isolation = tk.StringVar()
        code_departement_Isolation = tk.StringVar()
        poste_Isolation = tk.StringVar()
        isolant_Isolation = tk.StringVar()
        epaisseur_Isolation = tk.StringVar()
        surface_Isolation = tk.StringVar()
        cout_total_ht_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=cout_total_ht_Isolation).grid(row=0, column= 1, sticky="w")
        cout_induit_ht_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=cout_induit_ht_Isolation).grid(row=1, column= 1, sticky="w")
        annee_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=annee_Isolation).grid(row=2, column= 1, sticky="w")
        type_logement_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=type_logement_Isolation).grid(row=3, column= 1, sticky="w")
        annee_construction_logement_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=annee_construction_logement_Isolation).grid(row=4, column= 1, sticky="w")
        code_departement_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=code_departement_Isolation).grid(row=5, column= 1, sticky="w")
        poste_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=poste_Isolation).grid(row=6, column= 1, sticky="w")
        isolant_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=isolant_Isolation).grid(row=7, column= 1, sticky="w")
        epaisseur_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=epaisseur_Isolation).grid(row=8, column= 1, sticky="w")
        surface_Isolation_Modif2 = ttk.Entry(tabIsolation1, textvariable=surface_Isolation).grid(row=9, column= 1, sticky="w")
        Isolation.append(cout_total_ht_Isolation)
        Isolation.append(cout_induit_ht_Isolation)
        Isolation.append(annee_Isolation)
        Isolation.append(type_logement_Isolation)
        Isolation.append(annee_construction_logement_Isolation)
        Isolation.append(code_departement_Isolation)
        Isolation.append(poste_Isolation)
        Isolation.append(isolant_Isolation)
        Isolation.append(epaisseur_Isolation)
        Isolation.append(surface_Isolation)
        ttk.Button(tabIsolation1, text='Ajouter', command=lambda: self.AjouterIsolation(Isolation)).grid(row=10, column=1, sticky="w")

        Chauffage = []
        cout_total_ht_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='cout total ht').grid(row=0, column= 0, sticky="e")
        cout_induit_ht_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='cout induit ht').grid(row=1, column= 0, sticky="e")
        annee_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='annee chauffage').grid(row=2, column= 0, sticky="e")
        type_logement_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='type logement').grid(row=3, column=0, sticky="e")
        annee_construction_logement_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='annee construction logement').grid(row=4, column=0, sticky="e")
        code_departement_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='code departement').grid(row=5, column=0, sticky="e")
        energie_avant_travaux_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='energie avant travaux').grid(row=6, column=0, sticky="e")
        energie_installee_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='energie installee').grid(row=7, column=0, sticky="e")
        generateur_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='generateur chauffage').grid(row=8, column=0, sticky="e")
        type_chaudiere_Chauffage_Ajout1 = ttk.Label(tabChauffage1, text='type chaudiere').grid(row=9, column=0, sticky="e")
        cout_total_ht_Chauffage = tk.StringVar()
        cout_induit_ht_Chauffage = tk.StringVar()
        annee_Chauffage = tk.StringVar()
        type_logement_Chauffage = tk.StringVar()
        annee_construction_logement_Chauffage = tk.StringVar()
        code_departement_Chauffage = tk.StringVar()
        energie_avant_travaux_Chauffage = tk.StringVar()
        energie_installee_Chauffage = tk.StringVar()
        generateur_Chauffage = tk.StringVar()
        type_chaudiere_Chauffage = tk.StringVar()
        cout_total_ht_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=cout_total_ht_Chauffage).grid(row=0, column= 1, sticky="w")
        cout_induit_ht_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=cout_induit_ht_Chauffage).grid(row=1, column= 1, sticky="w")
        annee_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=annee_Chauffage).grid(row=2, column= 1, sticky="w")
        type_logement_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=type_logement_Chauffage).grid(row=3, column= 1, sticky="w")
        annee_construction_logement_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=annee_construction_logement_Chauffage).grid(row=4, column= 1, sticky="w")
        code_departement_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=code_departement_Chauffage).grid(row=5, column= 1, sticky="w")
        energie_avant_travaux_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=energie_avant_travaux_Chauffage).grid(row=6, column= 1, sticky="w")
        energie_installee_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=energie_installee_Chauffage).grid(row=7, column= 1, sticky="w")
        generateur_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=generateur_Chauffage).grid(row=8, column= 1, sticky="w")
        type_chaudiere_Chauffage_Ajout2 = ttk.Entry(tabChauffage1, textvariable=type_chaudiere_Chauffage).grid(row=9, column= 1, sticky="w")
        Chauffage.append(cout_total_ht_Chauffage)
        Chauffage.append(cout_induit_ht_Chauffage)
        Chauffage.append(annee_Chauffage)
        Chauffage.append(type_logement_Chauffage)
        Chauffage.append(annee_construction_logement_Chauffage)
        Chauffage.append(code_departement_Chauffage)
        Chauffage.append(energie_avant_travaux_Chauffage)
        Chauffage.append(energie_installee_Chauffage)
        Chauffage.append(generateur_Chauffage)
        Chauffage.append(type_chaudiere_Chauffage)
        ttk.Button(tabChauffage1, text='Ajouter', command=lambda: self.AjouterChauffage(Chauffage)).grid(row=10, columnspan=2)

        Photovoltaique = []
        cout_total_ht_Photovoltaique_Ajout1 = ttk.Label(tabPhotovoltaique1, text='cout total ht').grid(row=0, column= 0, sticky="e")
        cout_induit_ht_Photovoltaique_Ajout1 = ttk.Label(tabPhotovoltaique1, text='cout induit ht').grid(row=1, column= 0, sticky="e")
        annee_Photovoltaique_Ajout1 = ttk.Label(tabPhotovoltaique1, text='annee photovoltaique').grid(row=2, column= 0, sticky="e")
        type_logement_Photovoltaique_Ajout1 = ttk.Label(tabPhotovoltaique1, text='type logement').grid(row=3, column= 0, sticky="e")
        annee_construction_logement_Photovoltaique_Ajout1 = ttk.Label(tabPhotovoltaique1, text='annee construction logement').grid(row=4, column= 0, sticky="e")
        code_departement_Photovoltaique_Ajout1 = ttk.Label(tabPhotovoltaique1, text='code departement').grid(row=5, column= 0, sticky="e")
        puissance_installee_Photovoltaique_Ajout1 = ttk.Label(tabPhotovoltaique1, text='puissance installee').grid(row=6, column= 0, sticky="e")
        types_panneaux_Photovoltaique_Ajout1 = ttk.Label(tabPhotovoltaique1, text='types panneaux').grid(row=7, column= 0, sticky="e")
        cout_total_ht_Photovoltaique = tk.StringVar()
        cout_induit_ht_Photovoltaique = tk.StringVar()
        annee_Photovoltaique = tk.StringVar()
        type_logement_Photovoltaique = tk.StringVar()
        annee_construction_logement_Photovoltaique = tk.StringVar()
        code_departement_Photovoltaique = tk.StringVar()
        puissance_installee_Photovoltaique = tk.StringVar()
        types_panneaux_Photovoltaique = tk.StringVar()
        cout_total_ht_Photovoltaique_Ajout2 = ttk.Entry(tabPhotovoltaique1, textvariable=cout_total_ht_Photovoltaique).grid(row=0, column= 1, sticky="w")
        cout_induit_ht_Photovoltaique_Ajout2 = ttk.Entry(tabPhotovoltaique1, textvariable=cout_induit_ht_Photovoltaique).grid(row=1, column= 1, sticky="w")
        annee_Photovoltaique_Ajout2 = ttk.Entry(tabPhotovoltaique1, textvariable=annee_Photovoltaique).grid(row=2, column= 1, sticky="w")
        type_logement_Photovoltaique_Ajout2 = ttk.Entry(tabPhotovoltaique1, textvariable=type_logement_Photovoltaique).grid(row=3, column= 1, sticky="w")
        annee_construction_logement_Photovoltaique_Ajout2 = ttk.Entry(tabPhotovoltaique1, textvariable=annee_construction_logement_Photovoltaique).grid(row=4, column= 1, sticky="w")
        code_departement_Photovoltaique_Ajout2 = ttk.Entry(tabPhotovoltaique1, textvariable=code_departement_Photovoltaique).grid(row=5, column= 1, sticky="w")
        puissance_installee_Photovoltaique_Ajout2 = ttk.Entry(tabPhotovoltaique1, textvariable=puissance_installee_Photovoltaique).grid(row=6, column= 1, sticky="w")
        types_panneaux_Photovoltaique_Ajout2 = ttk.Entry(tabPhotovoltaique1, textvariable=types_panneaux_Photovoltaique).grid(row=7, column= 1, sticky="w")
        Photovoltaique.append(cout_total_ht_Photovoltaique)
        Photovoltaique.append(cout_induit_ht_Photovoltaique)
        Photovoltaique.append(annee_Photovoltaique)
        Photovoltaique.append(type_logement_Photovoltaique)
        Photovoltaique.append(annee_construction_logement_Photovoltaique)
        Photovoltaique.append(code_departement_Photovoltaique)
        Photovoltaique.append(puissance_installee_Photovoltaique)
        Photovoltaique.append(types_panneaux_Photovoltaique)
        ttk.Button(tabPhotovoltaique1, text='Ajouter', command=lambda: self.AjouterPhotovoltaique(Photovoltaique)).grid(row=8, columnspan=2)

        #On va maintenant définir les modifications
        Isolation_Modif = []
        Id_Isolation_Modif_label = ttk.Label(tabIsolation2, text='Id Isolation:').grid(row=0, column= 0, sticky="e")
        Id_Isolation_Modif_text = tk.StringVar()
        Id_Isolation_Modif = ttk.Combobox(tabIsolation2, textvariable=Id_Isolation_Modif_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_isolation FROM Isolations ORDER BY id_isolation")]).grid(row=0, column=1, sticky="w")
        
        cout_total_ht_Isolation_Modif1 = ttk.Label(tabIsolation2, text='cout total ht').grid(row=2, column= 0, sticky="e")
        cout_induit_ht_Isolation_Modif1 = ttk.Label(tabIsolation2, text='cout induit ht').grid(row=3, column= 0, sticky="e")
        annee_Isolation_Modif1 = ttk.Label(tabIsolation2, text='annee isolation').grid(row=4, column= 0, sticky="e")
        type_logement_Isolation_Modif1 = ttk.Label(tabIsolation2, text='type logement').grid(row=5, column= 0, sticky="e")
        annee_construction_logement_Isolation_Modif1 = ttk.Label(tabIsolation2, text='annee construction logement').grid(row=6, column= 0, sticky="e")
        code_departement_Isolation_Modif1 = ttk.Label(tabIsolation2, text='code departement').grid(row=7, column= 0, sticky="e")
        poste_Isolation_Modif1 = ttk.Label(tabIsolation2, text='poste isolation').grid(row=8, column= 0, sticky="e")
        isolant_Isolation_Modif1 = ttk.Label(tabIsolation2, text='isolant').grid(row=9, column= 0, sticky="e")
        epaisseur_Isolation_Modif1 = ttk.Label(tabIsolation2, text='epaisseur').grid(row=10, column= 0, sticky="e")
        surface_Isolation_Modif1 = ttk.Label(tabIsolation2, text='surface').grid(row=11, column= 0, sticky="e")
        cout_total_ht_Isolation_Modif = tk.StringVar()
        cout_induit_ht_Isolation_Modif = tk.StringVar()
        annee_Isolation_Modif = tk.StringVar()
        type_logement_Isolation_Modif = tk.StringVar()
        annee_construction_logement_Isolation_Modif = tk.StringVar()
        code_departement_Isolation_Modif = tk.StringVar()
        poste_Isolation_Modif = tk.StringVar()
        isolant_Isolation_Modif = tk.StringVar()
        epaisseur_Isolation_Modif = tk.StringVar()
        surface_Isolation_Modif = tk.StringVar()
        cout_total_ht_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=cout_total_ht_Isolation_Modif).grid(row=2, column= 1, sticky="w")
        cout_induit_ht_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=cout_induit_ht_Isolation_Modif).grid(row=3, column= 1, sticky="w")
        annee_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=annee_Isolation_Modif).grid(row=4, column= 1, sticky="w")
        type_logement_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=type_logement_Isolation_Modif).grid(row=5, column= 1, sticky="w")
        annee_construction_logement_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=annee_construction_logement_Isolation_Modif).grid(row=6, column= 1, sticky="w")
        code_departement_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=code_departement_Isolation_Modif).grid(row=7, column= 1, sticky="w")
        poste_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=poste_Isolation_Modif).grid(row=8, column= 1, sticky="w")
        isolant_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=isolant_Isolation_Modif).grid(row=9, column= 1, sticky="w")
        epaisseur_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=epaisseur_Isolation_Modif).grid(row=10, column= 1, sticky="w")
        surface_Isolation_Modif2 = ttk.Entry(tabIsolation2, textvariable=surface_Isolation_Modif).grid(row=11, column= 1, sticky="w")
        Isolation_Modif.append(cout_total_ht_Isolation_Modif)
        Isolation_Modif.append(cout_induit_ht_Isolation_Modif)
        Isolation_Modif.append(annee_Isolation_Modif)
        Isolation_Modif.append(type_logement_Isolation_Modif)
        Isolation_Modif.append(annee_construction_logement_Isolation_Modif)
        Isolation_Modif.append(code_departement_Isolation_Modif)
        Isolation_Modif.append(poste_Isolation_Modif)
        Isolation_Modif.append(isolant_Isolation_Modif)
        Isolation_Modif.append(epaisseur_Isolation_Modif)
        Isolation_Modif.append(surface_Isolation_Modif)
        ttk.Button(tabIsolation2, text='Valider', command=lambda: self.ModifierEntryIsolation(Isolation_Modif, Id_Isolation_Modif_text.get())).grid(row=1, column=1, sticky="w")
        ttk.Button(tabIsolation2, text='Modifier', command=lambda: self.ModifierIsolation(Isolation_Modif, Id_Isolation_Modif_text.get())).grid(row=12, column=1, sticky="w")

        Chauffage_Modif = []
        Id_Chauffage_Modif_label = ttk.Label(tabChauffage2, text='Id Chauffage:').grid(row=0, column= 0, sticky="e")
        Id_Chauffage_Modif_text = tk.StringVar()
        Id_Chauffage_Modif = ttk.Combobox(tabChauffage2, textvariable=Id_Chauffage_Modif_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_Chauffage FROM Chauffages ORDER BY id_chauffage")]).grid(row=0, column=1, sticky="w")

        cout_total_ht_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='cout total ht').grid(row=2, column= 0, sticky="e")
        cout_induit_ht_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='cout induit ht').grid(row=3, column= 0, sticky="e")
        annee_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='annee chauffage').grid(row=4, column= 0, sticky="e")
        type_logement_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='type logement').grid(row=5, column=0, sticky="e")
        annee_construction_logement_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='annee construction logement').grid(row=6, column=0, sticky="e")
        code_departement_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='code departement').grid(row=7, column=0, sticky="e")
        energie_avant_travaux_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='energie avant travaux').grid(row=8, column=0, sticky="e")
        energie_installee_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='energie installee').grid(row=9, column=0, sticky="e")
        generateur_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='generateur chauffage').grid(row=10, column=0, sticky="e")
        type_chaudiere_Chauffage_Modif1 = ttk.Label(tabChauffage2, text='type chaudiere').grid(row=11, column=0, sticky="e")
        cout_total_ht_Chauffage_Modif = tk.StringVar()
        cout_induit_ht_Chauffage_Modif = tk.StringVar()
        annee_Chauffage_Modif = tk.StringVar()
        type_logement_Chauffage_Modif = tk.StringVar()
        annee_construction_logement_Chauffage_Modif = tk.StringVar()
        code_departement_Chauffage_Modif = tk.StringVar()
        energie_avant_travaux_Chauffage_Modif = tk.StringVar()
        energie_installee_Chauffage_Modif = tk.StringVar()
        generateur_Chauffage_Modif = tk.StringVar()
        type_chaudiere_Chauffage_Modif = tk.StringVar()
        cout_total_ht_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=cout_total_ht_Chauffage_Modif).grid(row=2, column= 1, sticky="w")
        cout_induit_ht_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=cout_induit_ht_Chauffage_Modif).grid(row=3, column= 1, sticky="w")
        annee_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=annee_Chauffage_Modif).grid(row=4, column= 1, sticky="w")
        type_logement_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=type_logement_Chauffage_Modif).grid(row=5, column= 1, sticky="w")
        annee_construction_logement_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=annee_construction_logement_Chauffage_Modif).grid(row=6, column= 1, sticky="w")
        code_departement_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=code_departement_Chauffage_Modif).grid(row=7, column= 1, sticky="w")
        energie_avant_travaux_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=energie_avant_travaux_Chauffage_Modif).grid(row=8, column= 1, sticky="w")
        energie_installee_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=energie_installee_Chauffage_Modif).grid(row=9, column= 1, sticky="w")
        generateur_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=generateur_Chauffage_Modif).grid(row=10, column= 1, sticky="w")
        type_chaudiere_Chauffage_Modif2 = ttk.Entry(tabChauffage2, textvariable=type_chaudiere_Chauffage_Modif).grid(row=11, column= 1, sticky="w")
        Chauffage_Modif.append(cout_total_ht_Chauffage_Modif)
        Chauffage_Modif.append(cout_induit_ht_Chauffage_Modif)
        Chauffage_Modif.append(annee_Chauffage_Modif)
        Chauffage_Modif.append(type_logement_Chauffage_Modif)
        Chauffage_Modif.append(annee_construction_logement_Chauffage_Modif)
        Chauffage_Modif.append(code_departement_Chauffage_Modif)
        Chauffage_Modif.append(energie_avant_travaux_Chauffage_Modif)
        Chauffage_Modif.append(energie_installee_Chauffage_Modif)
        Chauffage_Modif.append(generateur_Chauffage_Modif)
        Chauffage_Modif.append(type_chaudiere_Chauffage_Modif)
        ttk.Button(tabChauffage2, text='Valider', command=lambda: self.ModifierEntryChauffage(Chauffage_Modif, Id_Chauffage_Modif_text.get())).grid(row=1, column=1, sticky="w")
        ttk.Button(tabChauffage2, text='Modifier', command=lambda: self.ModifierChauffage(Chauffage_Modif, Id_Chauffage_Modif_text.get())).grid(row=12, columnspan=2)

        Photovoltaique_Modif = []
        Id_Photovoltaique_Modif_label = ttk.Label(tabPhotovoltaique2, text='Id Photovoltaique:').grid(row=0, column= 0, sticky="e")
        Id_Photovoltaique_Modif_text = tk.StringVar()
        Id_Photovoltaique_Modif = ttk.Combobox(tabPhotovoltaique2, textvariable=Id_Photovoltaique_Modif_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_photovoltaique FROM Photovoltaiques ORDER BY id_photovoltaique")]).grid(row=0, column=1, sticky="w")
 
        cout_total_ht_Photovoltaique_Modif1 = ttk.Label(tabPhotovoltaique2, text='cout total ht').grid(row=2, column= 0, sticky="e")
        cout_induit_ht_Photovoltaique_Modif1 = ttk.Label(tabPhotovoltaique2, text='cout induit ht').grid(row=3, column= 0, sticky="e")
        annee_Photovoltaique_Modif1 = ttk.Label(tabPhotovoltaique2, text='annee photovoltaique').grid(row=4, column= 0, sticky="e")
        type_logement_Photovoltaique_Modif1 = ttk.Label(tabPhotovoltaique2, text='type logement').grid(row=5, column= 0, sticky="e")
        annee_construction_logement_Photovoltaique_Modif1 = ttk.Label(tabPhotovoltaique2, text='annee construction logement').grid(row=6, column= 0, sticky="e")
        code_departement_Photovoltaique_Modif1 = ttk.Label(tabPhotovoltaique2, text='code departement').grid(row=7, column= 0, sticky="e")
        puissance_installee_Photovoltaique_Modif1 = ttk.Label(tabPhotovoltaique2, text='puissance installee').grid(row=8, column= 0, sticky="e")
        types_panneaux_Photovoltaique_Modif1 = ttk.Label(tabPhotovoltaique2, text='types panneaux').grid(row=9, column= 0, sticky="e")
        cout_total_ht_Photovoltaique_Modif = tk.StringVar()
        cout_induit_ht_Photovoltaique_Modif = tk.StringVar()
        annee_Photovoltaique_Modif = tk.StringVar()
        type_logement_Photovoltaique_Modif = tk.StringVar()
        annee_construction_logement_Photovoltaique_Modif = tk.StringVar()
        code_departement_Photovoltaique_Modif = tk.StringVar()
        puissance_installee_Photovoltaique_Modif = tk.StringVar()
        types_panneaux_Photovoltaique_Modif = tk.StringVar()
        cout_total_ht_Photovoltaique_Modif2 = ttk.Entry(tabPhotovoltaique2, textvariable=cout_total_ht_Photovoltaique_Modif).grid(row=2, column= 1, sticky="w")
        cout_induit_ht_Photovoltaique_Modif2 = ttk.Entry(tabPhotovoltaique2, textvariable=cout_induit_ht_Photovoltaique_Modif).grid(row=3, column= 1, sticky="w")
        annee_Photovoltaique_Modif2 = ttk.Entry(tabPhotovoltaique2, textvariable=annee_Photovoltaique_Modif).grid(row=4, column= 1, sticky="w")
        type_logement_Photovoltaique_Modif2 = ttk.Entry(tabPhotovoltaique2, textvariable=type_logement_Photovoltaique_Modif).grid(row=5, column= 1, sticky="w")
        annee_construction_logement_Photovoltaique_Modif2 = ttk.Entry(tabPhotovoltaique2, textvariable=annee_construction_logement_Photovoltaique_Modif).grid(row=6, column= 1, sticky="w")
        code_departement_Photovoltaique_Modif2 = ttk.Entry(tabPhotovoltaique2, textvariable=code_departement_Photovoltaique_Modif).grid(row=7, column= 1, sticky="w")
        puissance_installee_Photovoltaique_Modif2 = ttk.Entry(tabPhotovoltaique2, textvariable=puissance_installee_Photovoltaique_Modif).grid(row=8, column= 1, sticky="w")
        types_panneaux_Photovoltaique_Modif2 = ttk.Entry(tabPhotovoltaique2, textvariable=types_panneaux_Photovoltaique_Modif).grid(row=9, column= 1, sticky="w")
        Photovoltaique_Modif.append(cout_total_ht_Photovoltaique_Modif)
        Photovoltaique_Modif.append(cout_induit_ht_Photovoltaique_Modif)
        Photovoltaique_Modif.append(annee_Photovoltaique_Modif)
        Photovoltaique_Modif.append(type_logement_Photovoltaique_Modif)
        Photovoltaique_Modif.append(annee_construction_logement_Photovoltaique_Modif)
        Photovoltaique_Modif.append(code_departement_Photovoltaique_Modif)
        Photovoltaique_Modif.append(puissance_installee_Photovoltaique_Modif)
        Photovoltaique_Modif.append(types_panneaux_Photovoltaique_Modif)
        ttk.Button(tabPhotovoltaique2, text='Valider', command=lambda: self.ModifierEntryPhotovoltaique(Photovoltaique_Modif, Id_Photovoltaique_Modif_text.get())).grid(row=1, column=1, sticky="w")
        ttk.Button(tabPhotovoltaique2, text='Modifier', command=lambda: self.ModifierPhotovoltaique(Photovoltaique_Modif, Id_Photovoltaique_Modif_text.get())).grid(row=10, columnspan=2)

        #On va maintenant définir les suppressions
        #Isolation
        Id_Isolation_label = ttk.Label(tabIsolation3, text='Id Isolation:').grid(row=0, column= 0, sticky="e")
        Id_Isolation_text = tk.StringVar()
        Id_Isolation = ttk.Combobox(tabIsolation3, textvariable=Id_Isolation_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_isolation FROM Isolations ORDER BY id_isolation")]).grid(row=0, column=1, sticky="w")
        
        columns = ('id_isolation', 'cout_total_ht_isolation', 'cout_induit_ht_isolation', 'annee_isolation', 'type_logement_isolation', 'annee_construction_logement_isolation', 'code_departement', 'poste_isolation', 'isolant_isolation', 'epaisseur_isolation', 'surface_isolation')
        query = """
            SELECT id_isolation, cout_total_ht_isolation, cout_induit_ht_isolation, annee_isolation, type_logement_isolation, annee_construction_logement_isolation, code_departement, poste_isolation, isolant_isolation, epaisseur_isolation, surface_isolation
            FROM Isolations
            ORDER BY id_isolation"""
        # On utilise la fonction createTreeViewDisplayQuery pour afficher les résultats de la requête
        tree = display.createTreeViewDisplayQuery(tabIsolation3, columns, query,200)
        tree.grid(row=2, columnspan=2,sticky="nswe")
        ttk.Button(tabIsolation3, text='Supprimer', command=lambda: self.SuppressionIsolation(Id_Isolation_text.get(), tree, tabIsolation3)).grid(row=1, columnspan=2)

        #Chauffage
        Id_Chauffage_label = ttk.Label(tabChauffage3, text='Id Chauffage:').grid(row=0, column= 0, sticky="e")
        Id_Chauffage_text = tk.StringVar()
        Id_Chauffage = ttk.Combobox(tabChauffage3, textvariable=Id_Chauffage_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_Chauffage FROM Chauffages ORDER BY id_chauffage")]).grid(row=0, column=1, sticky="w")
        
        columns_chauffage = ('id_chauffage','cout_total_ht_chauffage', 'cout_induit_ht_chauffage', 'annee_chauffage', 'type_logement_chauffage', 'annee_construction_logement_chauffage', 'code_departement', 'energie_avant_travaux_chauffage', 'energie_installee_chauffage', 'generateur_chauffage', 'type_chaudiere_chauffage')
        query_chauffage = """
            SELECT id_chauffage, cout_total_ht_chauffage, cout_induit_ht_chauffage, annee_chauffage, type_logement_chauffage, annee_construction_logement_chauffage, code_departement, energie_avant_travaux_chauffage, energie_installee_chauffage, generateur_chauffage, type_chaudiere_chauffage
            FROM Chauffages
            ORDER BY id_chauffage
        """
        # On utilise la fonction createTreeViewDisplayQuery pour afficher les résultats de la requête
        tree_chauffage = display.createTreeViewDisplayQuery(tabChauffage3, columns_chauffage, query_chauffage,200)
        tree_chauffage.grid(row=2, columnspan=2,sticky="nswe")
        ttk.Button(tabChauffage3, text='Supprimer', command=lambda: self.SuppressionChauffage(Id_Chauffage_text.get(), tree_chauffage, tabChauffage3)).grid(row=1, columnspan=2)

        #Photovoltaique
        Id_Photovoltaique_label = ttk.Label(tabPhotovoltaique3, text='Id Photovoltaique:').grid(row=0, column= 0, sticky="e")
        Id_Photovoltaique_text = tk.StringVar()
        Id_Photovoltaique = ttk.Combobox(tabPhotovoltaique3, textvariable=Id_Photovoltaique_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_photovoltaique FROM Photovoltaiques ORDER BY id_photovoltaique")]).grid(row=0, column=1, sticky="w")
        
        columns_photovoltaique = ('id_photovoltaique','cout_total_ht_photovoltaique', 'cout_induit_ht_photovoltaique', 'annee_photovoltaique', 'type_logement_photovoltaique', 'annee_construction_logement_photovoltaique', 'code_departement', 'puissance_installee_photovoltaique', 'types_panneaux_photovoltaique')
        query_photovoltaique = """
            SELECT id_photovoltaique, cout_total_ht_photovoltaique, cout_induit_ht_photovoltaique, annee_photovoltaique, type_logement_photovoltaique, annee_construction_logement_photovoltaique, code_departement, puissance_installee_photovoltaique, types_panneaux_photovoltaique
            FROM Photovoltaiques
            ORDER BY id_photovoltaique
        """
        # On utilise la fonction createTreeViewDisplayQuery pour afficher les résultats de la requête
        tree_photovoltaique = display.createTreeViewDisplayQuery(tabPhotovoltaique3, columns, query,200)
        tree_photovoltaique.grid(row=2, columnspan=2,sticky="nswe")
        ttk.Button(tabPhotovoltaique3, text='Supprimer', command=lambda: self.SuppressionPhotovoltaique(Id_Photovoltaique_text.get(), tree, tabPhotovoltaique3)).grid(row=1, columnspan=2)


    def AjouterIsolation(self, Isolation):
        tab = []
        for e in Isolation:
            if e.get() == '':
                tab.append(None)
            else:
                tab.append(e.get())
        cursor = db.data.cursor()
        cursor.execute("INSERT INTO Isolations (cout_total_ht_isolation, cout_induit_ht_isolation, annee_isolation, type_logement_isolation, annee_construction_logement_isolation, code_departement, poste_isolation, isolant_isolation, epaisseur_isolation, surface_isolation) VALUES (?, ?,?, ?, ?, ?, ?, ?, ?, ?)", tab)
        db.data.commit()

    def AjouterChauffage(self, Chauffage):
        tab = []
        for e in Chauffage:
            if e.get() == '':
                tab.append(None)
            else:
                tab.append(e.get())
        cursor = db.data.cursor()
        cursor.execute("INSERT INTO Chauffages (cout_total_ht_chauffage, cout_induit_ht_chauffage, annee_chauffage, type_logement_chauffage, annee_construction_logement_chauffage, code_departement, energie_avant_travaux_chauffage, energie_installee_chauffage, generateur_chauffage, type_chaudiere_chauffage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tab)
        db.data.commit()

    def AjouterPhotovoltaique(self, Photovoltaique):
        tab = []
        for e in Photovoltaique:
            if e.get() == '':
                tab.append(None)
            else:
                tab.append(e.get())
        cursor = db.data.cursor()
        cursor.execute("INSERT INTO Photovoltaiques (cout_total_ht_photovoltaique, cout_induit_ht_photovoltaique, annee_photovoltaique, type_logement_photovoltaique, annee_construction_logement_photovoltaique, code_departement, puissance_installee_photovoltaique, types_panneaux_photovoltaique) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", tab)
        db.data.commit()

    def SuppressionIsolation(self, id_isolation, tree, tabIsolation3):
        if (id_isolation != ''):
            cursor = db.data.cursor()
            cursor.execute("DELETE FROM Isolations WHERE id_isolation=?", [id_isolation])
            db.data.commit()
        columns = ('id_isolation', 'cout_total_ht_isolation', 'cout_induit_ht_isolation', 'annee_isolation', 'type_logement_isolation', 'annee_construction_logement_isolation', 'code_departement', 'poste_isolation', 'isolant_isolation', 'epaisseur_isolation', 'surface_isolation')
        query = """
            SELECT id_isolation, cout_total_ht_isolation, cout_induit_ht_isolation, annee_isolation, type_logement_isolation, annee_construction_logement_isolation, code_departement, poste_isolation, isolant_isolation, epaisseur_isolation, surface_isolation
            FROM Isolations
            ORDER BY id_isolation"""
        tree = display.createTreeViewDisplayQuery(tabIsolation3, columns, query,200)
        tree.grid(row=2, columnspan=2,sticky="nswe")
        Id_Isolation_text = tk.StringVar()
        Id_Isolation = ttk.Combobox(tabIsolation3, textvariable=Id_Isolation_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_isolation FROM Isolations ORDER BY id_isolation")]).grid(row=0, column=1, sticky="w")

    def SuppressionChauffage(self, id_chauffage, tree_chauffage, tabChauffage3):
        if (id_chauffage != ''):
            cursor = db.data.cursor()
            cursor.execute("DELETE FROM Chauffages WHERE id_chauffage=?", [id_chauffage])
            db.data.commit()
        columns_chauffage = ('id_chauffage','cout_total_ht_chauffage', 'cout_induit_ht_chauffage', 'annee_chauffage', 'type_logement_chauffage', 'annee_construction_logement_chauffage', 'code_departement', 'energie_avant_travaux_chauffage', 'energie_installee_chauffage', 'generateur_chauffage', 'type_chaudiere_chauffage')
        query_chauffage = """
            SELECT id_chauffage, cout_total_ht_chauffage, cout_induit_ht_chauffage, annee_chauffage, type_logement_chauffage, annee_construction_logement_chauffage, code_departement, energie_avant_travaux_chauffage, energie_installee_chauffage, generateur_chauffage, type_chaudiere_chauffage
            FROM Chauffages
            ORDER BY id_chauffage
        """
        tree_chauffage = display.createTreeViewDisplayQuery(tabChauffage3, columns_chauffage, query_chauffage,200)
        tree_chauffage.grid(row=2, columnspan=2,sticky="nswe")
        Id_Chauffage_text = tk.StringVar()
        Id_Chauffage = ttk.Combobox(tabChauffage3, textvariable=Id_Chauffage_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_Chauffage FROM Chauffages ORDER BY id_chauffage")]).grid(row=0, column=1, sticky="w")

    def SuppressionPhotovoltaique(self, id_photovoltaique, tree_photovoltaique, tabPhotovoltaique3):
        if (id_photovoltaique != ''):
            cursor = db.data.cursor()
            cursor.execute("DELETE FROM Photovoltaiques WHERE id_photovoltaique=?", [id_photovoltaique])
            db.data.commit()
        columns_photovoltaique = ('id_photovoltaique','cout_total_ht_photovoltaique', 'cout_induit_ht_photovoltaique', 'annee_photovoltaique', 'type_logement_photovoltaique', 'annee_construction_logement_photovoltaique', 'code_departement', 'puissance_installee_photovoltaique', 'types_panneaux_photovoltaique')
        query_photovoltaique = """
            SELECT id_photovoltaique, cout_total_ht_photovoltaique, cout_induit_ht_photovoltaique, annee_photovoltaique, type_logement_photovoltaique, annee_construction_logement_photovoltaique, code_departement, puissance_installee_photovoltaique, types_panneaux_photovoltaique
            FROM Photovoltaiques
            ORDER BY id_photovoltaique
        """
        tree_photovoltaique = display.createTreeViewDisplayQuery(tabPhotovoltaique3, columns_photovoltaique, query_photovoltaique,200)
        tree_photovoltaique.grid(row=2, columnspan=2,sticky="nswe")
        Id_Photovoltaique_text = tk.StringVar()
        Id_Photovoltaique = ttk.Combobox(tabPhotovoltaique3, textvariable=Id_Photovoltaique_text,values=[row[0] for row in db.data.cursor().execute("SELECT id_photovoltaique FROM Photovoltaiques ORDER BY id_photovoltaique")]).grid(row=0, column=1, sticky="w")
 
    def ModifierEntryIsolation(self, Isolation_Modif, id_isolation):
        tab = []
        cursor = db.data.cursor()
        result = cursor.execute("""
            SELECT cout_total_ht_isolation, cout_induit_ht_isolation, annee_isolation, type_logement_isolation, annee_construction_logement_isolation, code_departement, poste_isolation, isolant_isolation, epaisseur_isolation, surface_isolation
            FROM Isolations
            WHERE id_isolation = ?""", [id_isolation])
        i = 0
        tab2 = []
        for row in result:
            tab2.append(row)
        for e in Isolation_Modif:
            tab.append(e.set(tab2[0][i]))
            i = i + 1
        Isolation_Modif = tab

    def ModifierIsolation(self, Isolation_Modif, id_isolation):
        tab = []
        for e in Isolation_Modif:
            if e.get() == '' or e.get() == 'None':
                tab.append(None)
            else:
                tab.append(e.get())
        tab.append(id_isolation)
        try:
            cursor = db.data.cursor()
            cursor.execute("UPDATE Isolations SET cout_total_ht_isolation= ?, cout_induit_ht_isolation = ?, annee_isolation = ?, type_logement_isolation = ?, annee_construction_logement_isolation = ?, code_departement = ?, poste_isolation = ?, isolant_isolation = ?, epaisseur_isolation = ?, surface_isolation = ? WHERE id_isolation = ?", tab)
            db.data.commit()
        except sqlite3.Error as e:
            tk.messagebox.showerror("Erreur", message="Erreur: " + str(e))

    def ModifierEntryChauffage(self, Chauffage_Modif, id_chauffage):
        tab = []
        cursor = db.data.cursor()
        result = cursor.execute("""
            SELECT cout_total_ht_chauffage, cout_induit_ht_chauffage, annee_chauffage, type_logement_chauffage, annee_construction_logement_chauffage, code_departement, energie_avant_travaux_chauffage, energie_installee_chauffage, generateur_chauffage, type_chaudiere_chauffage
            FROM Chauffages
            WHERE id_chauffage = ?""", [id_chauffage])
        i = 0
        tab2 = []
        for row in result:
            tab2.append(row)
        for e in Chauffage_Modif:
            tab.append(e.set(tab2[0][i]))
            i = i + 1
        Chauffage_Modif = tab

    def ModifierChauffage(self, Chauffage_Modif, id_chauffage):
        tab = []
        for e in Chauffage_Modif:
            if e.get() == '' or e.get() == 'None':
                tab.append(None)
            else:
                tab.append(e.get())
        tab.append(id_chauffage)
        try:
            cursor = db.data.cursor()
            cursor.execute("UPDATE Chauffages SET cout_total_ht_chauffage= ?, cout_induit_ht_chauffage = ?, annee_chauffage = ?, type_logement_chauffage = ?, annee_construction_logement_chauffage = ?, code_departement = ?, energie_avant_travaux_chauffage = ?, energie_installee_chauffage = ?, generateur_chauffage = ?, type_chaudiere_chauffage = ? WHERE id_chauffage = ?", tab)
            db.data.commit()
        except sqlite3.Error as e:
            tk.messagebox.showerror("Erreur", message="Erreur: " + str(e))

    def ModifierEntryPhotovoltaique(self, Photovoltaique_Modif, id_photovoltaique):
        tab = []
        cursor = db.data.cursor()
        result = cursor.execute("""
            SELECT cout_total_ht_photovoltaique, cout_induit_ht_photovoltaique, annee_photovoltaique, type_logement_photovoltaique, annee_construction_logement_photovoltaique, code_departement, puissance_installee_photovoltaique, types_panneaux_photovoltaique
            FROM Photovoltaiques
            WHERE id_photovoltaique = ?""", [id_photovoltaique])
        i = 0
        tab2 = []
        for row in result:
            tab2.append(row)
        for e in Photovoltaique_Modif:
            tab.append(e.set(tab2[0][i]))
            i = i + 1
        Photovoltaique_Modif = tab

    def ModifierPhotovoltaique(self, Photovoltaique_Modif, id_photovoltaique):
        tab = []
        for e in Photovoltaique_Modif:
            if e.get() == '' or e.get() == 'None':
                tab.append(None)
            else:
                tab.append(e.get())
        tab.append(id_photovoltaique)
        try:
            cursor = db.data.cursor()
            cursor.execute("UPDATE Photovoltaiques SET cout_total_ht_photovoltaique= ?, cout_induit_ht_photovoltaique = ?, annee_photovoltaique = ?, type_logement_photovoltaique = ?, annee_construction_logement_photovoltaique = ?, code_departement = ?, puissance_installee_photovoltaique = ?, types_panneaux_photovoltaique = ? WHERE id_photovoltaique = ?", tab)
            db.data.commit()
        except sqlite3.Error as e:
            tk.messagebox.showerror("Erreur", message="Erreur: " + str(e))
