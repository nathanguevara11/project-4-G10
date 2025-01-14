# Machine Learning for Sports Betting

This project explores the application of machine learning (ML) to predict outcomes in various sports. We have investigated a variety of ML models and their ability to predict individual game outcomes, season records, post-season results, player performance, and more. A website was also developed to showcase the results.

## Table of Contents

- [Introduction](#introduction)
- [Basketball](#basketball)
- [Football](#football)
- [Hockey](#hockey)
- [Soccer](#soccer)
- [Conclusion](#conclusion)

## Introduction

Machine learning models were applied to predict outcomes across several sports, including Basketball, Football, Hockey, and Soccer. The focus was on leveraging historical data, identifying key features, and using advanced ML techniques to make accurate predictions.

## Basketball

The basketball model predicts the NBA champion for a given season using regular season data. 

### Data and Features
- Target: Championship winner (1 or 0).
- Features: Wins, losses, margin of victory, strength of schedule, ratings (offensive, defensive, net), pace factor, shooting percentages, and more.
- After feature importance analysis, the dataset was reduced to 12 features.

### Model
- **Algorithm:** Random Forest.
- **Performance:** Receiver Operating Characteristic (ROC) score of 0.88.
- **Strengths:** Averaged data over an 82-game season for better accuracy.
- **Weaknesses:** Small dataset with only 648 samples, even after SMOTE upsampling.

![image_360](https://github.com/user-attachments/assets/efe75689-cef7-4492-aa8e-b3605a52f023)

## Football

The goal was to predict the playoff outcomes for the 2024-2025 NFL season.

### Data and Features
- Data from the 2022-2023, 2023-2024, and 2024-2025 seasons.
- Features included win percentage, weather conditions, and score statistics.
- Limitation: Player performance, injuries, and coaching changes were not considered.

### Model
- **Algorithm:** Random Forest Classifier.
- **Performance:** 92.68% accuracy.
- Key features: Total game points (home and away) and quarter-wise point differentials.

## Hockey

Predictions were made for NHL team and player performances for the 2024-2025 season.

### Data Collection
- Data from 2021/2022, 2022/2023, and 2023/2024 NHL seasons.
- Features: Goals for/against, save percentage, and more.

### Models
1. **Random Forest (RF):**
   - R² = 0.973 (first run) and R² = 0.977 (second run).
   - Feature reduction improved efficiency.
2. **Linear Regression (LR):**
   - R² = 0.967.

### Results
- RF models consistently outperformed LR in accuracy.
- Predictions aligned with current pace projections.

## Soccer

The focus was on predicting outcomes of English Premier League matches.

### Data and Features
- Source: TheSportsDB API.
- Features: Average goals scored, possession, recent form, and more.
- Addressed class imbalance using SMOTE.

### Model
- **Algorithm:** Random Forest.
- **Performance:** 62.3% accuracy (above random chance).
- Predictions were made for the upcoming matchweek (1/14–1/16).

### Deployment
- Model saved using pickle for Flask deployment.
- User input integrated into predictions dynamically.

## Conclusion

This project demonstrates the potential of machine learning in sports betting predictions. Across all sports, Random Forest models consistently delivered strong performance, showcasing their robustness and adaptability. Future work will involve integrating more comprehensive datasets and refining the models for greater accuracy.

## Sources

NHL Data Sources - [naturalstattrick.com](https://www.naturalstattrick.com/) <br>
NFL Data Sources - [nfl.com](http://nfl.com/), [sportradar.com](http://sportradar.com/), [developersportradar.com](http://developersportradar.com/football), [sportslogos.net](http://sportslogos.net/)
