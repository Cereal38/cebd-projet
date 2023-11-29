
create table Departements (
    code_departement TEXT,
    nom_departement TEXT,
    code_region INTEGER,
    zone_climatique TEXT,
    constraint pk_departements primary key (code_departement),
    constraint fk_region foreign key (code_region) references Regions(code_region)
);

create table Regions (
    code_region INTEGER,
    nom_region TEXT,
    constraint pk_regions primary key (code_region)
);

create table Mesures (
    code_departement TEXT,
    date_mesure DATE,
    temperature_min_mesure FLOAT,
    temperature_max_mesure FLOAT,
    temperature_moy_mesure FLOAT,
    constraint pk_mesures primary key (code_departement, date_mesure),
    constraint fk_mesures foreign key (code_departement) references Departements(code_departement)
);

create table Communes (
    code_commune INTEGER PRIMARY KEY,
    nom_commune TEXT,
    status_commune TEXT,
    altitude_moyenne_commune INTEGER,
    population_commune INTEGER,
    superficie_commune INTEGER,
    code_canton_commune INTEGER,
    code_arrondissement_commune INTEGER
);
-- create table Travaux (
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
create table Isolations (
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
    surface_isolation FLOAT--,
    CONSTRAINT fk_isolation_code_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement)--,
--    CONSTRAINT ck_poste_isolation CHECK (poste_isolation IN ('COMBLES PERDUES', 'ITI', 'ITE', 'RAMPANTS', 'SARKING', 'TOITURE TERRASSE', 'PLANCHER BAS')),
--    CONSTRAINT ck_isolant_isolation CHECK (isolant_isolation IN ('AUTRES', 'LAINE VEGETALE', 'LAINE MINERALE', 'PLASTIQUES')),
--    CONSTRAINT ck_travaux_prix_positif CHECK (cout_total_ht_isolation > 0 AND cout_induit_ht_isolation > 0)
);

create table Chauffages (
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

create table Photovoltaiques (
    id_photovoltaique INTEGER PRIMARY KEY AUTOINCREMENT,
    cout_total_ht_photovoltaique  FLOAT,
    cout_induit_ht_photovoltaique  FLOAT,
    annee_photovoltaique  INTEGER,
    type_logement_photovoltaique  TEXT,
    annee_construction_logement_photovoltaique  INTEGER,
    code_departement TEXT,
    puissance_installee_photovoltaique INTEGER,
    types_panneaux_photovoltaique TEXT--,
--    CONSTRAINT fk_photovoltaique_code_departement FOREIGN KEY (code_departement) REFERENCES Departements(code_departement),
--    CONSTRAINT ck_types_panneaux_photovoltaique CHECK (types_panneaux_photovoltaique IN ('MONOCRISTALLIN', 'POLYCRISTALLIN')),
--    CONSTRAINT ck_travaux_prix_positif CHECK (cout_total_ht_photovoltaique > 0 AND cout_induit_ht_photovoltaique > 0)
);
--TODO Q4 Ajouter les créations des nouvelles tables