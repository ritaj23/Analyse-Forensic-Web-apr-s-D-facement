# 🔍 Web Forensic Analysis – SQL Injection Detection

## 📌 Description

Ce projet consiste à analyser un fichier access.log afin de détecter des activités suspectes après un incident de web defacement.

L’objectif principal est d’identifier :

* Les adresses IP suspectes
* Le type d’attaque utilisée
* Les requêtes malveillantes

---

## 🎯 Objectifs

* Analyser les logs d’un serveur web
* Détecter une attaque de type SQL Injection
* Extraire les preuves à partir des logs
* Automatiser l’analyse avec Python

---

## 🧰 Technologies utilisées

* 🐍 Python 3
* 📄 Fichier access.log
* 💻 CMD (Windows)

---

## 📂 Structure du projet

/project
│── access.log
│── analysis.py
│── README.md

---

## ⚙️ Installation

Aucune installation spécifique n’est requise.

✔️ Assurez-vous d’avoir Python installé :

python --version

---

## ▶️ Exécution

Dans le terminal (CMD) :

py analysis.py

---

## 📊 Résultats attendus

Le script affiche :

* ✅ IP suspecte
* 🔁 Nombre de tentatives
* ⚠️ Type d’attaque (SQL Injection)
* 📄 Requêtes suspectes

---

## 🧪 Exemple d’attaque détectée

GET /product.php?id=1' OR '1'='1

---

## 🚨 Analyse

* IP suspecte : 192.168.1.50
* Type d’attaque : SQL Injection
* Cible : product.php
* Action : tentative d’accès à admin.php

---

## 🔐 Recommandations

* Utiliser des requêtes préparées
* Valider les entrées utilisateur
* Implémenter un WAF
* Surveiller les logs régulièrement

---

## 📌 Remarques

* Aucun outil Kali Linux utilisé
* Aucune dépendance externe requise
* Projet basé uniquement sur Python standard

---

## 👨‍💻 Auteur

* Nom : [Votre Nom]
* Module : Sécurité / Forensic Web

---

## ⭐️ Conclusion

Ce projet démontre l’importance de l’analyse des logs dans la détection des attaques web et la compréhension du comportement des attaquants.
