import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/Users/mahaj/OneDrive/Documents/yield_df.csv.zip")

# Encode categorical columns: 'Area' and 'Item'
le_area = LabelEncoder()
le_item = LabelEncoder()
df['Area'] = le_area.fit_transform(df['Area'])
df['Item'] = le_item.fit_transform(df['Item'])

# Define features (X) and target (y)
X = df[['Area', 'Item', 'average_rain_fall_mm_per_year', 'pesticides_tonnes', 'avg_temp']]
y = df['hg/ha_yield']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f" Mean Absolute Error: {mae:.2f}")
print(f" R-squared: {r2:.2f}")

# Plot actual vs predicted
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.2, color='green', edgecolors='w', linewidths=0.5)

# Plot formatting
plt.xlabel('Actual Yield (hg/ha)', fontsize=12)
plt.ylabel('Predicted Yield (hg/ha)', fontsize=12)
plt.title('📊 Actual vs Predicted Crop Yield', fontsize=14)
plt.grid(True)
plt.tight_layout()

# Optional: Add 1:1 reference line to visualize perfect prediction
min_val = min(min(y_test), min(y_pred))
max_val = max(max(y_test), max(y_pred))
plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label='Perfect Prediction')
plt.legend()


plt.show()
# .\myenv\Scripts\Activate.ps1
