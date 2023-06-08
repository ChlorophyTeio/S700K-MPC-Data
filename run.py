import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Font manager
font_path = r".\FiraCode-Regular.ttf"
custom_font = FontProperties(fname=font_path)

# Read Excel file
df = pd.read_excel('data.xlsx')

# Extract data from column 1 to column 6
x1 = df.iloc[:, 0].values
curve1 = df.iloc[:, 1].values
x2 = df.iloc[:, 2].values
curve2 = df.iloc[:, 3].values
x3 = df.iloc[:, 4].values
curve3 = df.iloc[:, 5].values

# Set figure size
plt.figure(figsize=(10, 6))

# Plot line charts
plt.plot(x1, curve1, label=df.columns[1])
plt.plot(x2, curve2, label=df.columns[3])
plt.plot(x3, curve3, label=df.columns[5])

# Add data value markers
plt.scatter(x1, curve1, color='red', marker='o', s=10)
plt.scatter(x2, curve2, color='blue', marker='o', s=10)
plt.scatter(x3, curve3, color='green', marker='o', s=10)

# Set legend and titles
plt.legend()
plt.xlabel("x (Time of Sampling Point)")
plt.ylabel("Curve (Power at Time Point)")
plt.title("S700K Power Curve")

# Print data (Debug)
# # x
# print("x1 (Time of Sampling Point):")
# for val in x1:
#     print(f"{val:.5f}")
# # y
# print("Curve1 (Power at Time Point):")
# for val in curve1:
#     print(f"{val:.5f}")

# Set the format of tick labels
# x
plt.xticks(np.arange(0, max(x1), 0.1))
plt.xticks(rotation=90, ha='center', fontsize=8)
plt.xticks(ticks=plt.xticks()[0], labels=[f"{tick:.1f}" for tick in plt.xticks()[0]])
# y
plt.yticks(np.arange(0, max(curve1), 0.1))
plt.yticks(rotation=0, ha='right', fontsize=8)

# Display the plot
plt.show()
