# Phishing Detector

Détecteur de phishing par IA — API FastAPI + XGBoost + SHAP + extension Chrome.

## Installation
(à compléter) 


## Résultats de l'entraînement (sur données nettoyées)

| Modèle | Précision | Rappel (Phishing) | Temps d'entraînement |
| :--- | :--- | :--- | :--- |
| Random Forest (Features de base) | 79.39 % | 0.75 | ~21 sec |
| Random Forest (+ N-grammes) | 92.50 % | 0.91 | ~30 sec |
| **XGBoost (+ N-grammes)** | **93.29 %** | **0.91** | **17.8 sec** |