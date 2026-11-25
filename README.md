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

## Résultats (Données nettoyées, sans fuite de données, sans biais http/www)

| Modèle | Exactitude | Rappel (Phishing) | Temps d'entraînement |
| :--- | :--- | :--- | :--- |
| Random Forest (features de base) | 78.3 % | 75.7 % | 0.69 s |
| XGBoost (features de base) | 81.3 % | 74.0 % | 0.39 s |
| Random Forest (N-grammes TF-IDF) | **89.9 %** | **87.7 %** | 13.27 s |
| XGBoost (N-grammes TF-IDF) | **89.9 %** | 86.7 % | 18.26 s |

*Conclusion : L'ajout des n-grammes (lecture du texte) améliore l'exactitude de plus de 10 points par rapport aux caractéristiques numériques seules.*