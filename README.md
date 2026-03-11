# DevOps Monitoring Project

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

> Petit projet de monitoring DevOps montrant comment utiliser **Docker**, **Prometheus** et **Grafana** pour surveiller une application web simple.

---

## Table des matières

- Description
- Architecture
- Fichiers du projet
- Prérequis
- Installation
- Utilisation
- Objectifs du projet

---

## Description

Dans ce projet, j'ai mis en place une petite stack de monitoring composée de trois outils :

| Composant | Rôle |
|-----------|------|
| **Flask** | Application web simple qui compte le nombre de visites |
| **Prometheus** | Récupère les métriques exposées par l'application |
| **Grafana** | Affiche ces métriques sous forme de dashboard |

L'objectif est de montrer comment on peut **monitorer une application avec des outils DevOps courants**.

---

## Architecture


+─────────────────────────────────────────────────────────+
| Docker Network |
| |
| +─────────────+ scrape +──────────────+ |
| | Flask App | ────────────> | Prometheus | |
| | | | | |
| | :5000 | | :9090 | |
| | /metrics | +──────+───────+ |
| +─────────────+ | |
| | datasource |
| +──────v───────+ |
| | Grafana | |
| | :3000 | |
| +──────────────+ |
+─────────────────────────────────────────────────────────+


### Comment ça fonctionne

1. L'utilisateur visite l'application Flask.
2. Un compteur de visites est incrémenté.
3. Prometheus récupère la métrique `/metrics` toutes les **5 secondes**.
4. Grafana interroge Prometheus et affiche les données dans un dashboard.

---

## Fichiers du projet


devops-monitoring/
├── app.py
├── requirements.txt
├── Dockerfile
├── prometheus.yml
├── docker-compose.yml
├── grafana_dashboard.json (optionnel)
└── README.md


### Description rapide

- **app.py** → application Flask avec le compteur de visites  
- **requirements.txt** → dépendances Python  
- **Dockerfile** → image Docker pour l'application  
- **prometheus.yml** → configuration de Prometheus  
- **docker-compose.yml** → lance tous les services ensemble  
- **grafana_dashboard.json** → export du dashboard Grafana  

---

## Prérequis

Avant de lancer le projet il faut avoir :

- Docker
- Docker Compose
- Un navigateur web

Git est optionnel si vous clonez le projet.

---

## Installation et lancement

### 1. Cloner le projet

```bash
git clone https://github.com/iminesaid/devops-monitoring.git
cd devops-monitoring
2. Lancer les services
docker-compose up --build

La première fois Docker doit télécharger les images, donc cela peut prendre un peu de temps.

Pour les lancements suivants :

docker-compose up
Accès aux services
Service	URL
Flask	http://localhost:5000

Prometheus	http://localhost:9090

Grafana	http://localhost:3000

Connexion Grafana :

user : admin
password : admin
Utilisation

Ouvrir l'application Flask dans le navigateur.

Rafraîchir la page plusieurs fois.

Le compteur de visites augmente.

Prometheus récupère cette métrique automatiquement.

Grafana affiche l'évolution dans le dashboard.

Exemple de métrique
visits_total 5

Cela signifie que la page a été visitée 5 fois.

Objectifs du projet

Ce projet m'a permis de :

Comprendre comment dockeriser une application

Utiliser Docker Compose pour lancer plusieurs services

Découvrir Prometheus et le scraping de métriques

Créer un dashboard Grafana

Voir le fonctionnement d'une petite stack de monitoring DevOps

Auteur

Imene Said

GitHub :
https://github.com/iminesaid
