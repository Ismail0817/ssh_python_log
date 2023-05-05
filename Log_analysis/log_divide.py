import re

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
        print(f'Date: {date}, Time: {time}, Host: {info_seperated[1]}, Process: {info_seperated[2]}, Message: {message}')
