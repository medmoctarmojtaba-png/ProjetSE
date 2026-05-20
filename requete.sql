CREATE DATABASE gestion_commande;
USE gestion_commande;
CREATE TABLE client (id_client INT AUTO_INCREMENT PRIMARY KEY,nom VARCHAR(50),prenom VARCHAR(100),adresse TEXT);
CREATE TABLE produit (id_produit INT AUTO_INCREMENT PRIMARY KEY,nom_produit VARCHAR(50),prix DECIMAL(10.2));
CREATE TABLE commande (id_commande INT AUTO_INCREMENT PRIMARY KEY,id_client INT,nom VARCHAR(100),FOREIGN KEY(id_client)REFERENCES client(id_client));
INSERT INTO client (id_client, nom, prenom, adresse) VALUES
(1, 'Mint Mohamed', 'Aicha', 'Nouakchott, Tevragh-Zeina'),
(2, 'Ould Ahmed', 'Mohamed', 'Nouakchott, Ksar'),
(3, 'Mint Sidi', 'Fatimetou', 'Nouadhibou, Centre Ville'),
(4, 'Ould Sidi', 'Sidi', 'Rosso, Quartier Escale'),
(5, 'Mint Cheikh', 'Mariem', 'Atar, Vieille Ville');
INSERT INTO produit (id_produit, nom_produit, prix) VALUES
(101, 'Ordinateur HP', 450000.00),
(102, 'Souris Logitech', 5000.00),
(103, 'Clavier Mécanique', 25000.00),
(104, 'Écran 24 pouces', 120000.00);
INSERT INTO commande (id_commande, id_client, id_produit, quantite, date_commande) VALUES
(1001, 1, 101, 1, '2025-10-01'),
(1002, 1, 102, 2, '2025-10-01'),
(1003, 2, 103, 1, '2025-10-05'),
(1004, 3, 104, 1, '2025-10-10'),
(1005, 4, 102, 1, '2025-10-12');
SELECT * FROM produit;
SELECT * FROM client;
SELECT * FROM commande;
