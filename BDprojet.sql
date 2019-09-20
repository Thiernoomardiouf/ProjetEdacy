CREATE DATABASE BDprojet;
Use BDprojet;

-- Voici le code pour créer la table Classe 

CREATE TABLE Classe (IdClasse INTEGER NOT NULL,
Numeroclasse VARCHAR (30) NOT NULL,
Nomclasse VARCHAR (30) NOT NULL,
Nombre INTEGER NOT NULL,
PRIMARY KEY (IdClasse));

-- Le code pour créer la table Eleve

CREATE TABLE Eleve (IdEleve INTEGER NOT NULL,
Numeroeleve VARCHAR (5) DEFAULT NULL,
Nom VARCHAR (50) NOT NULL,
Prenom VARCHAR (50) NOT NULL,
Classe VARCHAR (50) NOT NULL,
PRIMARY KEY (IdEleve));

