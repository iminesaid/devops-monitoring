# DevOps Monitoring Project

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

> Petit projet de monitoring DevOps montrant comment utiliser **Docker**, **Prometheus** et **Grafana** pour surveiller une application web simple.

---

## Table des matières

- [Description](#description)
- [Architecture](#architecture)
- [Fichiers du projet](#fichiers-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation-et-lancement)
- [Utilisation](#utilisation)
- [Objectifs du projet](#objectifs-du-projet)

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
```
+─────────────────────────────────────────────────────────+
|                    Docker Network                        |
|                                                          |
|  +─────────────+    scrape     +──────────────+         |
|  |  Flask App  | ────────────> |  Prometheus  |         |
|  |             |               |              |         |
|  |  :5000      |               |    :9090     |         |
|  |  /metrics   |               +──────+───────+         |
|  +─────────────+                      | datasource      |
|                                +──────v───────+         |
|                                |   Grafana    |         |
|                                |    :3000     |         |
|                                +──────────────+         |
+─────────────────────────────────────────────────────────+
```

### Comment ça fonctionne

1. L'utilisateur visite l'application Flask.
2. Un compteur de visites est incrémenté.
3. Prometheus récupère la métrique `/metrics` toutes les **5 secondes**.
4. Grafana interroge Prometheus et affiche les données dans un dashboard.

---

## Fichiers du projet
```
devops-monitoring/
├── app.py
├── requirements.txt
├── Dockerfile
├── prometheus.yml
├── docker-compose.yml
├── grafana_dashboard.json    (optionnel)
└── README.md
```

- **app.py** — application Flask avec le compteur de visites
- **requirements.txt** — dépendances Python
- **Dockerfile** — image Docker pour l'application
- **prometheus.yml** — configuration de Prometheus
- **docker-compose.yml** — lance tous les services ensemble
- **grafana_dashboard.json** — export du dashboard Grafana

---

## Prérequis

- [Docker](https://docs.docker.com/get-docker/) et [Docker Compose](https://docs.docker.com/compose/install/)
- Un navigateur web
- Git *(optionnel)*

---

## Installation et lancement

### 1. Cloner le projet
```bash
git clone https://github.com/iminesaid/devops-monitoring.git
cd devops-monitoring
```

### 2. Lancer les services
```bash
docker-compose up --build
```

> La première fois, Docker doit télécharger les images — cela peut prendre quelques minutes. Pour les lancements suivants, utilise simplement `docker-compose up`.

### 3. Accéder aux services

| Service | URL | Identifiants |
|---------|-----|--------------|
| Flask | http://localhost:5000 | — |
| Prometheus | http://localhost:9090 | — |
| Grafana | http://localhost:3000 | `admin` / `admin` |

### 4. Arrêter les services
```bash
docker-compose down
```

---

## Utilisation

1. Ouvrir l'application Flask dans le navigateur.
2. Rafraîchir la page plusieurs fois — le compteur de visites augmente.
3. Prometheus récupère cette métrique automatiquement.
4. Grafana affiche l'évolution dans le dashboard.

### Exemple de métrique
```
# HELP visits_total Total number of visits
# TYPE visits_total counter
visits_total 5
```

Cela signifie que la page a été visitée 5 fois.

---

## Objectifs du projet

Ce projet m'a permis de :

- Comprendre comment dockeriser une application
- Utiliser Docker Compose pour lancer plusieurs services
- Découvrir Prometheus et le scraping de métriques
- Créer un dashboard Grafana
- Voir le fonctionnement d'une petite stack de monitoring DevOps

---

<p align="center">
  <a href="https://github.com/iminesaid">github.com/iminesaid</a>
</p>
