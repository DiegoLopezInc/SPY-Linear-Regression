# SPY Linear Regression Analysis

## Purpose
This project aims to measure recent volatility in the equities market by creating a simple linear regression model of the SPDR S&P 500 ETF Trust (SPY) from April 21, 2024, to July 21, 2024.

## Project Goals
1. Clean and preprocess SPY market data
2. Develop a linear regression model to predict closing prices
3. Analyze the model's performance and feature importance
4. Visualize the results using a Streamlit web application

## Requirements
- Python 3.7+
- pandas
- numpy
- scikit-learn
- matplotlib
- streamlit

## Project Structure
- `dataCleaner.py`: Handles data preprocessing and feature engineering
- `model.py`: Contains the linear regression model and training functions
- `app.py`: Streamlit web application for displaying results and visualizations
- `SPY_4-21-2024_to_7-21-2024.csv`: Raw data file (not included in repository)

## Installation
1. Clone the repository 
2. Install required packages: `pip install -r requirements.txt`

## Usage
1. Ensure the SPY data file is in the correct location
2. Run the Streamlit app: `streamlit run app.py`

## Features
- Data cleaning and preprocessing
- Linear regression model training
- Model performance metrics (MSE, RMSE, R-squared)
- Visualization of actual vs predicted close prices
- Feature importance analysis

## License
Undecided
