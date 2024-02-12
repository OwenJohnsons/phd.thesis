#%% 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import scienceplots; plt.style.use(['science', 'ieee'])

# Sample data for tasks
tasks = {
    'Task 1': {'start': datetime(2024, 1, 1), 'end': datetime(2024, 1, 5)},
    'Task 2': {'start': datetime(2024, 1, 3), 'end': datetime(2024, 1, 8)},
    'Task 3': {'start': datetime(2025, 1, 6), 'end': datetime(2025, 1, 12)}
}

# Create figure and axis
fig, ax = plt.subplots()

# Plotting Gantt chart with no gaps between bars
for task, values in tasks.items():
    start_date = values['start']
    end_date = values['end']
    duration = end_date - start_date

    ax.barh(task, duration, left=start_date, height=1, color='skyblue', edgecolor='black')

# Formatting
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.MonthLocator())
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
plt.xlabel('Timeline')
# plt.ylabel('Tasks')
# plt.title('Gantt Chart')
plt.grid(True)

# Show plot
plt.show()
