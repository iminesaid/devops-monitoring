# DevOps Monitoring Project

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

> Application de monitoring DevOps illustrant l'intégration de **Docker**, **Prometheus** et **Grafana** pour surveiller une application web en temps réel.

---

## Table des matières

- [Description](#description)
- [Architecture](#architecture)
- [Fichiers du projet](#fichiers-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation-et-lancement)
- [Utilisation](#utilisation)
- [Objectifs pédagogiques](#objectifs-pédagogiques)

---

## Description

Ce projet met en place une stack de monitoring complète avec trois composants principaux :

| Composant | Rôle |
|-----------|------|
| **Flask** | Application web qui expose un compteur de visites et un endpoint `/metrics` |
| **Prometheus** | Collecte et stocke les métriques exposées par Flask toutes les 5 secondes |
| **Grafana** | Visualise les métriques sous forme de dashboard interactif en temps réel |

---

## Architecture
```
+─────────────────────────────────────────────────────────+
|                    Docker Network                        |
|                                                          |
|  +─────────────+    scrape     +──────────────+         |
|  |  Flask App  | ────────────> |  Prometheus  |         |
|  |             |               |              |         |
|  |  :5000/     |               |    :9090     |         |
|  |  :5000/     |               +──────+───────+         |
|  |   metrics   |                      | data source     |
|  +─────────────+               +──────v───────+         |
|                                 |   Grafana    |         |
|                                 |    :3000     |         |
|                                 +──────────────+         |
+─────────────────────────────────────────────────────────+
```

**Flux de données :**
1. L'utilisateur visite l'app Flask — le compteur s'incrémente
2. Prometheus scrape `/metrics` toutes les **5 secondes**
3. Grafana interroge Prometheus et affiche les métriques en **temps réel**

---

## Fichiers du projet
```
devops-monitoring/
├── app.py                    # Application Flask (compteur + endpoint /metrics)
├── requirements.txt          # Dépendances Python (Flask, prometheus_client)
├── Dockerfile                # Image Docker pour l'app Flask
├── prometheus.yml            # Configuration Prometheus (scrape interval, targets)
├── docker-compose.yml        # Orchestration des 3 services
├── grafana_dashboard.json    # Export JSON du dashboard Grafana (optionnel)
└── README.md                 # Documentation
```

---

## Prérequis

- [Docker](https://docs.docker.com/get-docker/) et [Docker Compose](https://docs.docker.com/compose/install/) installés
- Un navigateur web
- Git pour cloner le projet *(optionnel)*

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

> **Note :** La première exécution peut prendre quelques minutes le temps que Docker construise les images et télécharge Prometheus et Grafana. Les lancements suivants se font simplement avec `docker-compose up`.

### 3. Accéder aux services

| Service | URL | Identifiants |
|---------|-----|--------------|
| Flask App | http://\<IP_VM\>:5000 | — |
| Prometheus | http://\<IP_VM\>:9090 | — |
| Grafana | http://\<IP_VM\>:3000 | `admin` / `admin` |

> Remplace `<IP_VM>` par l'adresse IP de ta machine ou `localhost` si tu travailles en local.

### 4. Arrêter les services
```bash
docker-compose down
```

---

## Utilisation

1. **Flask** — Rafraîchis la page plusieurs fois, le compteur `visits_total` s'incrémente à chaque visite.
2. **Prometheus** — Tape `visits_total` dans la barre de recherche pour interroger la métrique directement.
3. **Grafana** — Connecte-toi et consulte le dashboard pour visualiser l'évolution en temps réel.

### Exemple de métrique Prometheus
```
# HELP visits_total Total number of visits
# TYPE visits_total counter
visits_total 5
```

---

## Objectifs pédagogiques

- Maîtriser **Docker Compose** pour l'orchestration de services multiples
- Comprendre le fonctionnement de **Prometheus** : scraping, exposition de métriques, PromQL
- Construire un **dashboard Grafana** connecté à une source de données réelle
- Visualiser le flux DevOps complet : application → métriques → monitoring → visualisation

---

## Contribution

Les contributions sont les bienvenues. N'hésite pas à ouvrir une *issue* ou une *pull request*.

---

<p align="center">
  <a href="https://github.com/iminesaid">github.com/iminesaid</a>
</p>
