import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dataCleaner import data, X, y
from model import train_model

# Set the title of the web app
st.title('SPY Linear Regression Model for 4/21/2024 to 7/21/2024')

# Display the data
st.subheader('Raw Data')
st.write(data)

# Train the model
model, mse, rmse, r2 = train_model(X, y)

# Display model results
st.subheader('Model Results')
st.write(f'Mean Squared Error: {mse:.2f}')
st.write(f'Root Mean Squared Error: {rmse:.2f}')
st.write(f'R-squared: {r2:.2f}')

# Plot actual vs predicted values
st.subheader('Actual vs Predicted Close Prices')
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(y, model.predict(X), alpha=0.5)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
ax.set_xlabel('Actual Close Price')
ax.set_ylabel('Predicted Close Price')
st.pyplot(fig)

# Feature importance
st.subheader('Feature Importance')
feature_importance = pd.DataFrame({'Feature': X.columns, 'Importance': model.coef_})
feature_importance = feature_importance.sort_values('Importance', ascending=False)
st.bar_chart(feature_importance.set_index('Feature'))