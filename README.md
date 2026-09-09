# Projet CI/CD

Ce projet met en place une pipeline CI/CD pour une application web Python Flask.

## Fonctionnement du pipeline

À chaque exécution, la pipeline réalise automatiquement :

1. les tests unitaires avec `unittest`
2. les tests E2E avec `unittest` et `requests`
3. le build de l’image Docker
4. le push de l’image sur Docker Hub
5. le déploiement sur une VM Azure via SSH
6. une vérification de l’application avec l’endpoint `/health`

Le build et le déploiement ne sont exécutés que si les tests réussissent.

## Déclenchement du déploiement

La pipeline GitHub Actions se déclenche automatiquement à chaque `push` sur la branche `main`.

Aucune action manuelle n’est nécessaire après le push.

## Choix techniques

* **Python Flask** pour l’application web
* **unittest** pour les tests unitaires et E2E
* **requests** pour tester les endpoints HTTP
* **Docker** pour conteneuriser l’application
* **Docker Hub** pour stocker les images
* **GitHub Actions** pour automatiser la CI/CD
* **VM Azure** pour héberger l’application
* **SSH** pour effectuer le déploiement
* **GitHub Secrets** pour stocker les identifiants sensibles

Le conteneur utilise un nom fixe afin de garantir un déploiement idempotent.
