
CREATE TABLE Departements (
    code_departement TEXT,
    nom_departement TEXT,
    code_region INTEGER,
    zone_climatique TEXT,
    CONSTRAINT pk_departements PRIMARY KEY (code_departement),
    CONSTRAINT fk_region FOREIGN KEY (code_region) REFERENCES Regions(code_region)
);

CREATE TABLE Regions (
    code_region INTEGER,
    nom_region TEXT,
    CONSTRAINT pk_regions PRIMARY KEY (code_region)
);

CREATE TABLE Mesures (
    code_departement TEXT,
    date_mesure DATE,
    temperature_min_mesure FLOAT,
    temperature_max_mesure FLOAT,
    temperature_moy_mesure FLOAT,
    CONSTRAINT pk_mesures PRIMARY KEY (code_departement, date_mesure),
    CONSTRAINT fk_mesures FOREIGN KEY (code_departement) REFERENCES Departements(code_departement)
);

CREATE TABLE Communes (
    code_commune INTEGER PRIMARY KEY,
    nom_commune TEXT,
    status_commune TEXT,
    altitude_moyenne_commune INTEGER,
    population_commune INTEGER,
    superficie_commune INTEGER,
    code_canton_commune INTEGER,
    code_arrondissement_commune INTEGER
);
-- CREATE TABLE Travaux (
--     id_travaux INTEGER PRIMARY KEY AUTOINCREMENT,
--     cout_total_ht FLOAT,
--     cout_induit_ht FLOAT,
--     annee_travaux INTEGER,
--     type_logement TEXT,
--     annee_construction_logement_travaux INTEGER,
--     code_departement TEXT,
--     CONSTRAINT fk_travaux_code_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement),
--     CONSTRAINT ck_travaux_prix_positif CHECK (cout_total_ht > 0 AND cout_induit_ht > 0)
-- );

-- On a choisit de faire l'héritage avec la stratégie de la duplication.
-- Cela afin d'éviter de nombreux JOIN inutiles et pour simplifier la récupération des données depuis les CSV.
CREATE TABLE Isolations (
    id_isolation INTEGER PRIMARY KEY AUTOINCREMENT,
    cout_total_ht_isolation FLOAT,
    cout_induit_ht_isolation FLOAT,
    annee_isolation INTEGER,
    type_logement_isolation TEXT,
    annee_construction_logement_isolation INTEGER,
    code_departement TEXT,
    poste_isolation TEXT,
    isolant_isolation TEXT,
    epaisseur_isolation INTEGER,
    surface_isolation FLOAT,
    CONSTRAINT fk_isolation_code_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement)--,
--    CONSTRAINT ck_poste_isolation CHECK (poste_isolation IN ('COMBLES PERDUES', 'ITI', 'ITE', 'RAMPANTS', 'SARKING', 'TOITURE TERRASSE', 'PLANCHER BAS')),
--    CONSTRAINT ck_isolant_isolation CHECK (isolant_isolation IN ('AUTRES', 'LAINE VEGETALE', 'LAINE MINERALE', 'PLASTIQUES')),
--    CONSTRAINT ck_travaux_prix_positif CHECK (cout_total_ht_isolation > 0 AND cout_induit_ht_isolation > 0)
);

CREATE TABLE Chauffages (
    id_chauffage INTEGER PRIMARY KEY AUTOINCREMENT,
    cout_total_ht_chauffage FLOAT,
    cout_induit_ht_chauffage FLOAT,
    annee_chauffage INTEGER,
    type_logement_chauffage TEXT,
    annee_construction_logement_chauffage INTEGER,
    code_departement TEXT,
    energie_avant_travaux_chauffage TEXT,
    energie_installee_chauffage TEXT,
    generateur_chauffage TEXT,
    type_chaudiere_chauffage TEXT--,
--    CONSTRAINT fk_chauffage_code_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement)--,
--    CONSTRAINT ck_energie_avant_travaux_chauffage CHECK (energie_avant_travaux_chauffage IN ('AUTRES', 'BOIS', 'ELECTRICITE', 'FIOUL', 'GAZ')),
--    CONSTRAINT ck_energie_installee_chauffage CHECK (energie_installee_chauffage IN ('AUTRES', 'BOIS', 'ELECTRICITE', 'FIOUL', 'GAZ')),
--    CONSTRAINT ck_generateur_chauffage CHECK (generateur_chauffage IN ('AUTRES', 'CHAUDIERE', 'INSERT', 'POELE', 'PAC', 'RADIATEUR')),
--    CONSTRAINT ck_type_chaudiere_chauffage CHECK (type_chaudiere_chauffage IN ('STANDARD', 'AIR-EAU', 'A CONDENSATION', 'AUTRES', 'AIR-AIR', 'GEOTHERMIE', 'HPE')),
--    CONSTRAINT ck_travaux_prix_positif CHECK (cout_total_ht_chauffage > 0 AND cout_induit_ht_chauffage > 0)
);

CREATE TABLE Photovoltaiques (
    id_photovoltaique INTEGER PRIMARY KEY AUTOINCREMENT,
    cout_total_ht_photovoltaique  FLOAT,
    cout_induit_ht_photovoltaique  FLOAT,
    annee_photovoltaique  INTEGER,
    type_logement_photovoltaique  TEXT,
    annee_construction_logement_photovoltaique  INTEGER,
    code_departement TEXT,
    puissance_installee_photovoltaique INTEGER,
    types_panneaux_photovoltaique TEXT--,
--    CONSTRAINT fk_photovoltaique_code_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement)--,
--    CONSTRAINT ck_types_panneaux_photovoltaique CHECK (types_panneaux_photovoltaique IN ('MONOCRISTALLIN', 'POLYCRISTALLIN')),
--    CONSTRAINT ck_travaux_prix_positif CHECK (cout_total_ht_photovoltaique > 0 AND cout_induit_ht_photovoltaique > 0)
);
--TODO Q4 Ajouter les créations des nouvelles tables