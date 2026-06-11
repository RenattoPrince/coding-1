import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Data
Titanic = pd.read_csv(r"Titanic Dataset.csv")

# 2. Initial Inspection
print("Dataset Shape:", Titanic.shape)
print("\nMissing Values:\n", Titanic.isnull().sum())

# 3. Visualizing Missing Data
plt.figure(figsize=(10,6))
sns.heatmap(Titanic.isnull(), cmap="spring", cbar=False)
plt.title("Missing Data Heatmap")
plt.show() 

# 4. Cleaning
# Note: dropping NA before get_dummies is good, but check if you're losing too much data!
Titanic.dropna(inplace=True)

# 5. Encoding Categorical Variables
# We use drop_first=True to avoid the "Dummy Variable Trap" (Multicollinearity)
sex = pd.get_dummies(Titanic["Gender"], drop_first=True)
embarked = pd.get_dummies(Titanic["Embarked"], drop_first=True)
pclass = pd.get_dummies(Titanic["Pclass"], drop_first=True)

# 6. Concatenate and Drop Original Columns
# It's best to drop the original string columns after you've created the dummies
Titanic = pd.concat([Titanic, sex, embarked, pclass], axis=1)
Titanic.drop(['Gender', 'Embarked', 'Pclass'], axis=1, inplace=True)

# 7. Final Result
print("\nCleaned Data Preview:")
print(Titanic.head())