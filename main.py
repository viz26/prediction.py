import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# Read data from CSV file
df = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\student_data.csv')

# Convert marks column to int data type
marks_columns = ['PHYSICS', 'CHEM', 'MATHS', 'COMP']
df[marks_columns] = df[marks_columns].astype(int)

# Calculate highest and lowest marks in each subject
highest_marks = df[marks_columns].max()
lowest_marks = df[marks_columns].min()

# Calculate average marks across all subjects
df['Average Marks'] = df[marks_columns].mean(axis=1)
average_marks = df['Average Marks'].mean()

# Print highest, lowest, and average marks
print('Highest marks:')
print(highest_marks)
print('Lowest marks:')
print(lowest_marks)
print('Average marks:')
print(average_marks)

# Create a bar chart for lowest marks
plt.bar(lowest_marks.index, lowest_marks.values)
plt.title('Lowest Marks')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.show()

# Create a bar chart for highest marks
plt.bar(highest_marks.index, highest_marks.values)
plt.title('Highest Marks')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.show()

# Create a histogram for average marks
plt.hist(df['Average Marks'], bins=10)
plt.title('Average Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()

# Create a pie chart of the distribution of marks in each subject
marks_dist = df[marks_columns].sum()
plt.pie(marks_dist, labels=marks_columns, autopct='%1.1f%%')
plt.title('Distribution of Marks')
plt.show()

# Create a scatter plot of physics marks vs. maths marks
plt.scatter(df['PHYSICS'], df['MATHS'])
plt.title('PHYSICS MARKS vs. MATHS MARKS')
plt.xlabel('PHYSICS MARKS')
plt.ylabel('MATHS MARKS')
plt.show()

# Create a line chart of computer marks over time
df['Date'] = pd.date_range(start='1/1/2022', periods=len(df), freq='W')
today = date.today().strftime("%d/%m/%Y")
plt.plot(df['Date'], df['COMP'])
plt.title(f'Computer Marks over Time ({today})')
plt.xlabel('Date')
plt.ylabel('Marks')
plt.show()
