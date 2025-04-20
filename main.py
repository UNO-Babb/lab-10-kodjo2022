#MapPlot.py
#Name:
#Date:
#Assignment:

import graduates
import pandas as pd
import matplotlib.pyplot as plt

grad_major = graduates.get_grad_major()

# Prepare data
records = []

for degree in grad_major:
    try:
        year = int(degree["Year"])
        if 1993 <= year <= 2003:
            gender_data = degree["Demographics"]["Gender"]
            gender_data["Year"] = year
            records.append(gender_data)
    except (ValueError, TypeError):
        continue  # skip if year is invalid

# Create DataFrame
df = pd.DataFrame(records)

# Group by year to eliminate duplicates
df = df.groupby("Year").sum(numeric_only=True)

# Reindex to ensure all years appear on the x-axis
all_years = pd.Index(range(1993, 2004))
df = df.reindex(all_years, fill_value=0)

# Plot
df.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title("Graduates by Gender (1993–2003)")
plt.xlabel("Year")
plt.ylabel("Number of Graduates")
plt.legend(title="Gender")

# Save and show
plt.savefig("output.png")
plt.show()



