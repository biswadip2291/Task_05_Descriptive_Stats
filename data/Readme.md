# Task 05: Descriptive Statistics and Large Language Models

This repository documents the research project for Task 5, which explores the strengths and limitations of Large Language Models (LLMs) in performing descriptive statistical analysis on a sports dataset.

**Researcher:** Biswadip Bhattacharyya 
**Date:** July 31, 2024  
**Dataset:** 2025 Syracuse Women's Lacrosse (stats as of May 12, 2025)  
**LLM Used:** ChatGPT-4 with Advanced Data Analysis (simulated interaction)

---

## 1. Project Objective

The goal of this project is to evaluate how well an LLM can interact with a small real-world dataset, answer factual and inferential questions, and perform defined metric-based analysis. A special focus is placed on the need for prompt engineering and user guidance to ensure valid results.

---

## 2. Methodology and Initial Steps

### 2.1 Data Acquisition and Preparation

- The dataset was provided as an image (`2025 Syracuse Women's Lacrosse Syracuse Combined Team Statistics.jpg`).
- The data was manually transcribed into two machine-readable CSV files:
  - `game_results_2025.csv`: Contains game-by-game results (opponent, score, win/loss). Score was split into `SU_Score` and `Opponent_Score`.
  - `player_stats_2025.csv`: Contains individual player statistics (Goals, Assists, Points, Shots, etc.).

> ⚠️ Note: In accordance with submission guidelines, the actual CSV files are **not included** in this repository.

### 2.2 Validation Script

A validation script (`scripts/validation.py`) was developed using **pandas** to independently compute ground-truth results and verify the LLM's answers.

---

## 3. LLM Interaction: Phase 1 (Simple Questions)

### ✅ Prompt 1: Data Ingestion

- **Action**: Uploaded both CSVs into the LLM session.
- **Task**: Load into pandas DataFrames and verify with `.head()` and `.info()`.

### ✅ Prompt 2: Factual Questions

See [`prompts/02_simple_questions.txt`](prompts/02_simple_questions.txt)

- **Q1:** Total games played and final win-loss record  
  - ✅ 19 games, Record: 10 Wins – 9 Losses  
- **Q2:** Leader in total points  
  - ✅ Emma Ward, 76 points  
- **Q3:** Most caused turnovers (CT)  
  - ✅ Coco Vandiver, 40 CTs  

> ✅ **Validation**: All answers confirmed using the validation script.

---

## 4. LLM Interaction: Phase 2 (Complex Questions & Metric Definition)

### ❓ Challenge Prompt: "Who was the most efficient goal scorer?"

The term “efficient” required a clear user-defined metric. I defined **Shooting Percentage = Goals / Shots**, with a filter for players with ≥30 shots.

See [`prompts/03_complex_questions_metrics_definition.txt`](prompts/03_complex_questions_metrics_definition.txt)

### ✅ Expected LLM Steps:

1. Filter players with ≥30 shots  
2. Create a new column `Shooting_Pct = G / Sh`  
3. Sort descending and return top 3

### 🏅 Correct Output:
- Caroline Trinkaus (32/72 = **44.4%**)
- Mileena Cotter (21/50 = **42.0%**)
- Molly Guzik (14/34 = **41.2%**)

> ⚠️ **Insight**: LLM accuracy depends on precise metric definitions. Ambiguity leads to incorrect or inconsistent output.

---


## 5. Key Takeaways

- **LLMs are highly effective** at structured, factual queries when given clean data.
- **Prompt engineering is critical** when working with derived metrics or ambiguous terms.
- **Simple scripts for validation** are essential to assess correctness.

