import csv

with open('Dataset_Malawi_National_Football_Team_Matches.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(f"Column 1: {row[0]}, Column 2: {row[1]}")
'''

data = [
    ['Name', 'Age', 'City'],
    ['Aman', 28, 'Pune'],
    ['Poonam', 24, 'Jaipur'],
    ['Bobby', 32, 'Delhi']
]

csv_file_path = 'Dataset_Malawi_National_Football_Team_Matches.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' created successfully.")

'''




# USING A PYTHON PROGRAM READ THE TABLE PRESENT IN MYSQL DATABASE AND SAVE THE CONTENT INTO IN THE FILE ON DEKSTOP