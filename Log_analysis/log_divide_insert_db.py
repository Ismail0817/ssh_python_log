import re
import mysql.connector

db_config = {
    'user': 'shojeeb',
    'password': 'shojeeb',
    'host': '192.168.10.244',
    'database': 'ssh_log'
}

# Connect to the database
cnx = mysql.connector.connect(**db_config)

# Create a cursor object
cursor = cnx.cursor()


with open('sample_log.txt', 'r') as f:
    for line in f:
        info_with_log = line.strip().split(': ')
        info = info_with_log[0]
        message = info_with_log[1]
        info_seperated = info.split(' ')
        match = re.search(r'(.+)([+-]\d{2}:\d{2})', info_seperated[0])
        
        if match:
            datetime_part = match.group(1)
            timezone_part = match.group(2)

        date_time = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', datetime_part).group()
        date, time = date_time.split('T')
        print(f'Date: {date}, Time: {time}, Timezone: {timezone_part} Host: {info_seperated[1]}, Process: {info_seperated[2]}, Message: {message}')

        # Execute a query
        query = 'INSERT INTO log (Date, Time, Host, Process, Message, Timezone) VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(query, (date, time, info_seperated[1], info_seperated[2], message, timezone_part))
    
# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
