# DevOps Monitoring Demo

## Description
Ce projet montre une application Flask simple qui compte le nombre de visites.
- Monitoring avec Prometheus
- Dashboard live avec Grafana
- Lancement facile avec Docker Compose

## Lancer le projet
1. Ouvrir un terminal dans le dossier du projet
2. Lancer la commande :
```bash
docker-compose up --build
Accès aux services

Application Flask : http://10.0.2.15:5000

Prometheus : http://10.0.2.15:9090

Grafana : http://10.0.2.15:3000

Login Grafana : admin / admin

Notes

Chaque rafraîchissement de l’application augmente le compteur de visites

Le dashboard Grafana montre les métriques en temps réel

