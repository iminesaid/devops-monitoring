# 🚀 DevOps Monitoring Project

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

> Application de monitoring DevOps illustrant l'intégration de **Docker**, **Prometheus** et **Grafana** pour surveiller une application web en temps réel.

---

## 📋 Table des matières

- [Description](#-description)
- [Architecture](#-architecture)
- [Fichiers du projet](#-fichiers-du-projet)
- [Prérequis](#-prérequis)
- [Installation](#-installation-et-lancement)
- [Utilisation](#-utilisation)
- [Objectifs pédagogiques](#-objectifs-pédagogiques)

---

## 📖 Description

Ce projet met en place une stack de monitoring complète avec trois composants principaux :

| Composant | Rôle |
|-----------|------|
| 🐍 **Flask** | Application web qui expose un compteur de visites et un endpoint `/metrics` |
| 📊 **Prometheus** | Collecte et stocke les métriques exposées par Flask toutes les 5 secondes |
| 📈 **Grafana** | Visualise les métriques sous forme de dashboard interactif en temps réel |

---

## 🏗 Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    Docker Network                        │
│                                                          │
│  ┌─────────────┐    scrape     ┌──────────────┐         │
│  │  Flask App  │ ────────────> │  Prometheus  │         │
│  │             │               │              │         │
│  │  :5000/     │               │    :9090     │         │
│  │  :5000/     │               └──────┬───────┘         │
│  │   metrics   │                      │ data source     │
│  └─────────────┘               ┌──────▼───────┐         │
│                                 │   Grafana    │         │
│                                 │    :3000     │         │
│                                 └──────────────┘         │
└─────────────────────────────────────────────────────────┘
```

**Flux de données :**
1. L'utilisateur visite l'app Flask → le compteur s'incrémente
2. Prometheus scrape `/metrics` toutes les **5 secondes**
3. Grafana interroge Prometheus et affiche les métriques en **temps réel**

---

## 📁 Fichiers du projet
```
devops-monitoring/
├── app.py                    # Application Flask (compteur + endpoint /metrics)
├── requirements.txt          # Dépendances Python (Flask, prometheus_client)
├── Dockerfile                # Image Docker pour l'app Flask
├── prometheus.yml            # Config Prometheus (scrape interval, targets)
├── docker-compose.yml        # Orchestration des 3 services
├── grafana_dashboard.json    # Export JSON du dashboard Grafana (optionnel)
└── README.md                 # Documentation
```

---

## ✅ Prérequis

- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/install/) installés
- Un navigateur web
- *(Optionnel)* Git pour cloner le projet

---

## 🚀 Installation et lancement

### 1. Cloner le projet
```bash
git clone https://github.com/iminesaid/devops-monitoring.git
cd devops-monitoring
```

### 2. Lancer les services
```bash
docker-compose up --build
```

> ⏳ **Première fois :** Docker va construire les images et télécharger Prometheus/Grafana — cela peut prendre quelques minutes.
> ⚡ **Fois suivantes :** relancer simplement avec `docker-compose up`

### 3. Accéder aux services

| Service | URL | Credentials |
|---------|-----|-------------|
| 🐍 Flask App | http://\<IP_VM\>:5000 | — |
| 📊 Prometheus | http://\<IP_VM\>:9090 | — |
| 📈 Grafana | http://\<IP_VM\>:3000 | `admin` / `admin` |

> 💡 Remplace `<IP_VM>` par l'IP de ta machine ou utilise `localhost` en local.

### 4. Arrêter les services
```bash
docker-compose down
```

---

## 🎮 Utilisation

1. **Visite l'app Flask** → rafraîchis la page plusieurs fois, le compteur `visits_total` augmente
2. **Ouvre Prometheus** → tape `visits_total` dans la barre de recherche pour voir la métrique
3. **Ouvre Grafana** → connecte-toi et explore le dashboard pour voir l'évolution en temps réel

### Exemple de métrique Prometheus
```
# HELP visits_total Total number of visits
# TYPE visits_total counter
visits_total 5
```

---

## 🎯 Objectifs pédagogiques

- 🐳 Maîtriser **Docker Compose** pour l'orchestration multi-services
- 🔍 Comprendre le fonctionnement de **Prometheus** (scraping, métriques, PromQL)
- 📊 Construire un **dashboard Grafana** connecté à une source de données réelle
- 🔄 Visualiser le **flux DevOps** complet : app → métriques → monitoring → visualisation

---

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésite pas à ouvrir une *issue* ou une *pull request*.

---

<p align="center">
  Made with ❤️ — <a href="https://github.com/iminesaid">@iminesaid</a>
</p>
