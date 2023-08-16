import pandas as pd

df = pd.read_csv('Precios index.csv')

# Calculate the annual ROI for each column for 2021-2022
print("ROI for 2021-2022:")
for column in df.columns:
    initial_value = df.loc['2021-01-02', column]
    final_value = df.loc['2022-01-02', column]
    roi = ((final_value - initial_value) / initial_value) * 100
    print(f"{column}: {roi:.2f}%")

# Calculate the annual ROI for each column for 2022-2023
print("\nROI for 2022-2023:")
for column in df.columns:
    initial_value = df.loc['2022-01-02', column]
    final_value = df.loc['2023-08-15', column]
    roi = ((final_value - initial_value) / initial_value) * 100
    print(f"{column}: {roi:.2f}%")