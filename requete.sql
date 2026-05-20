CREATE DATABASE gestion_commande;
USE gestion_commande;
CREATE TABLE client (id_client INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(50),prenom VARCHAR(100),adresse TEXT);
CREATE TABLE produit (id_produit INT AUTO_INCREMENT PRIMARY KEY,nom_produit VARCHAR(50),prix DECIMAL(10.2));
CREATE TABLE commande (id_commande INT AUTO_INCREMENT PRIMARY KEY,id_client INT,nom VARCHAR(100),FOREIGN KEY(id_client)REFERENCES client(id_client));
SELECT * FROM produit;