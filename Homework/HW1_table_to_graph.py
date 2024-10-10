######Import Packages, Read CSV, & Prepare for Plotting######

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('feigin2014_table1_mortality.csv')

# Convert year to datetime for better plotting
df['year'] = pd.to_datetime(df['year'], format='%Y')

######Create Plot to Transform Table to Graph######

# Create the plot
fig, axes = plt.subplots(3, 1, figsize=(12, 15), sharex=True)
fig.suptitle('Mortality Rates by Year, Income Group, and Age Group', fontsize=16)

age_groups = ['<75', '>=75', 'all']
colors = {'high': 'blue', 'low_and_middle': 'red', 'all': 'green'}

for i, age in enumerate(age_groups):
    ax = axes[i]
    data = df[df['age_group'] == age]

    for income in ['high', 'low_and_middle', 'all']:
        income_data = data[data['income_group'] == income]
        ax.plot(income_data['year'], income_data['mortality_rate'],
                label=income, color=colors[income], marker='o')

        # Add confidence interval
        ax.fill_between(income_data['year'],
                        income_data['interval_low'],
                        income_data['interval_high'],
                        alpha=0.2, color=colors[income])

    ax.set_title(f'Age Group: {age}')
    ax.set_ylabel('Mortality Rate\n(per 100,000 person-years)')
    ax.legend(title='Income Group')
    ax.grid(True, linestyle='--', alpha=0.7)

    # # Uncomment this to set y-axis to logarithmic scale with custom tick locations
    # ax.set_yscale('log')

    # Custom y-axis ticks based on the age group
    if age == '<75':
        yticks = [20, 30, 40, 50, 60, 70]
    elif age == '>=75':
        yticks = [1000, 1500, 2000, 2500]
    else:  # 'all'
        yticks = [60, 80, 100, 120, 140]

    ax.set_yticks(yticks)
    ax.set_yticklabels([str(y) for y in yticks])

plt.xlabel('Year')
plt.tight_layout()
plt.show()
