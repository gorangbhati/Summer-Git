import mysql.connector
import csv
import os

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Gorang@2005',
    'database': 'peep'
}

csv_path = os.path.join(os.path.expanduser("~"), "Desktop", "dataset_stats.csv")

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS InstrumentStats (
            class VARCHAR(50),
            image_count INT,
            avg_width INT,
            avg_height INT,
            min_width INT,
            min_height INT,
            max_width INT,
            max_height INT,
            corrupt_files INT
        )
    """)

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO InstrumentStats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row['class'],
                int(row['image_count']),
                int(row['avg_width']),
                int(row['avg_height']),
                int(row['min_width']),
                int(row['min_height']),
                int(row['max_width']),
                int(row['max_height']),
                int(row['corrupt_files'])
            ))

    conn.commit()
    print("Data inserted successfully into InstrumentStats.")

except mysql.connector.Error as err:
    print("Database error:", err)

except Exception as e:
    print("Error:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
