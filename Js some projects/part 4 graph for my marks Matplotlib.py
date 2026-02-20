import matplotlib.pyplot as plt
from datetime import datetime

#This time I am making a scatter graph for my percenatge of grades for maths from start of year 8 to present marks.

My_Marks=[66, 83, 75, 20, 50, 60, 71, 50, 0, 75, 80, 78, 50, 80, 80] # These are the marks
Time_OF_MARKS_returned=["18/09/25", "18/09/25", "18/09/25", "18/09/25", "18/09/25", "15/10/25", "21/10/25", "21/10/25", "21/10/25", "21/10/25", "19/11/25", "12/12/25", "27/01/26", "28/01/26", "10/02/26"] # these are the time of when the marks got returned

# Convert strings to actual date objects
dates = [datetime.strptime(d, "%d/%m/%y") for d in Time_OF_MARKS_returned]

# To calc the total avrg

overall_avg = sum(My_Marks) / len(My_Marks)
# Group 2 by date to finde the daily avrg
daily_data = {}
for date, mark in zip(dates, My_Marks):
    if date not in daily_data:
        daily_data[date] = []
    daily_data[date].append(mark)
    # Sort the unique dates and calculate their averages
unique_dates = sorted(daily_data.keys())
daily_avgs = [sum(daily_data[d]) / len(daily_data[d]) for d in unique_dates]

def scatter_graph():
    plt.figure(figsize=(10, 6))
    plt.axhline(y=overall_avg, color='red', linestyle='--', linewidth=1.5, label=f'Overall Average({overall_avg:.1f}%)') #To show the overall avg with a line on the output which is 62


    # Add a line showing the daily averages to see the trend
    plt.plot(unique_dates, daily_avgs, color='green', marker='s', linestyle='-', linewidth=2, label='Daily Average')
    # Creating the scatter graph
    plt.scatter(dates, My_Marks, color='blue', marker='o', edgecolors='black')

    # Adding titles and labels
    plt.title('Maths Grade Progress: Year 8 to Present', fontsize=14)
    plt.xlabel('Date of Mark Returned', fontsize=12)
    plt.ylabel('Percentage Grade (%)', fontsize=12)
    
    # Setting the y-axis limit to 100% since these are grades
    plt.ylim(0, 100)
    
    # Formatting the layout to prevent overlapping text
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend() #Shows the labels
    plt.gcf().autofmt_xdate() # Tilts dates for better readability
    
    plt.show()

scatter_graph()
