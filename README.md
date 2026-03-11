# DevOps Monitoring Project

## Description
Ce projet est une **application de monitoring DevOps** qui illustre l'intégration de Docker, Prometheus et Grafana pour surveiller une application web simple.  

- **Application** : Flask qui compte le nombre de visites  
- **Monitoring** : Prometheus pour collecter les métriques  
- **Dashboard** : Grafana pour visualiser les métriques en temps réel  
- **Lancement facile** : Docker Compose pour orchestrer tous les services  

---

## Architecture du projet

```text
┌──────────────┐      ┌───────────────┐
│   Flask App  │ ---> │ Prometheus    │ ---> Grafana
│  /metrics    │      │ scrapes data  │    Dashboard
└──────────────┘      └───────────────┘

Flask App expose / et /metrics

Prometheus récupère les métriques via /metrics

Grafana affiche un dashboard en temps réel basé sur ces métriques

Fichiers principaux
Fichier	Description
app.py	Application Flask avec compteur de visites et endpoint Prometheus
requirements.txt	Dépendances Python (Flask, prometheus_client)
Dockerfile	Image Docker pour l’application Flask
prometheus.yml	Configuration de Prometheus pour scraper l’app Flask
docker-compose.yml	Orchestration Docker des 3 services : app, Prometheus, Grafana
README.md	Documentation du projet
grafana_dashboard.json (optionnel)	Export JSON du dashboard Grafana
Prérequis

Docker et Docker Compose installés sur la machine

Navigateur pour accéder à l’application, Prometheus et Grafana

Git pour récupérer le projet depuis GitHub (optionnel)

Installation et lancement

Cloner le projet depuis GitHub :

git clone https://github.com/iminesaid/devops-monitoring.git
cd devops-monitoring

Lancer tous les services :

docker-compose up --build

Première fois : Docker va construire les images et télécharger Prometheus/Grafana → peut prendre quelques minutes

Après : tu pourras relancer juste avec docker-compose up

Accéder aux services depuis un navigateur :

Service	URL
Application Flask	http://<IP_VM>:5000
Prometheus	http://<IP_VM>:9090
Grafana	http://<IP_VM>:3000

Login Grafana : admin / admin

Remplace <IP_VM> par l’IP de ta VM ou localhost si tu lances sur ton PC.

Utilisation

Rafraîchis la page Flask → le compteur visits augmente

Prometheus scrappe les métriques automatiquement toutes les 5 secondes

Grafana met à jour le dashboard en temps réel

Exemple de métrique Prometheus
visits_total  5

Le nombre correspond aux visites sur la page / de l’application

Points forts / objectifs pédagogiques

Apprentissage de Docker Compose et orchestration multi-services

Découverte de Prometheus et Grafana pour le monitoring

Visualisation des métriques en temps réel pour comprendre le flux DevOps

Déploiement simple sur une machine locale ou VM
