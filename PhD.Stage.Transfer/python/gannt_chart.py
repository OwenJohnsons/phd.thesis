#%%
'''
Code Purpose: Generate a gantt chart for PhD timeline
Author: Owen A. Johnson
Date: 2024-02-24
'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import scienceplots; plt.style.use(['science', 'ieee'])

# Sample data for tasks
tasks = {
    'Annoy Evan': {'start': datetime(2024, 3, 8), 'end': datetime(2026, 8, 31)},
    'Thesis Writing': {'start': datetime(2026, 3, 1), 'end': datetime(2026, 8, 31)},
    'X-Ray Project' : {'start': datetime(2025, 1, 1), 'end': datetime(2026, 3, 31)},
    'Radio Stars and Planets': {'start': datetime(2024, 3, 8), 'end': datetime(2025, 9, 8)},
    'LOFTS' : {'start': datetime(2024, 6, 1), 'end': datetime(2025, 6, 1)},
    'NenuSETI': {'start': datetime(2024, 3, 8), 'end': datetime(2024, 5, 10)},
    'Redback': {'start': datetime(2024, 3, 8), 'end': datetime(2024, 9, 1)}
}

# Create figure and axis
fig, ax = plt.subplots(figsize=(8,2))
ibm_cols = ['#F92A82', '#C7B8EA', '#4F518C', '#9EE493', '#76E5FC', '#F7996E', '#276FBF']

# Formatting
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.xlabel('PhD Timeline', fontsize=14)
plt.grid(True, which='both', axis='x', linestyle='--', zorder = 0)

i = 0 
for task, values in tasks.items():
    start_date = values['start']
    end_date = values['end']
    duration = end_date - start_date

    ax.barh(task, duration, left=start_date, height=1, color=ibm_cols[i], edgecolor='black', zorder = 3)
    i += 1

# Show plot
plt.savefig('PhD_gannt_chart.pdf', dpi=300, bbox_inches='tight')
plt.show()