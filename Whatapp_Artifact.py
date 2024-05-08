import re
import pandas as pd

#Regex patterns to extract timestamp, sender, and message
#pattern = r'(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - (\w+): (.*)'
pattern = r'^(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - ([^:]+): (.*)$'

#Reading chat file
data = []
with open("C:\\Users\\S.DESKTOP-J9AB18Q\\Downloads\\WhatsApp Chat with Papa\\WhatsApp Chat with Papa.txt", 'r', encoding='utf-8') as file:
    for line in file:
        match = re.match(pattern, line)
        if match:
            timestamp, sender, message = match.groups()
            data.append({'Timestamp': timestamp, 'Sender': sender, 'Message': message})

#Creating DataFrame
df = pd.DataFrame(data)

#Output to Excel file
df.to_excel("output_excel_file.xlsx", index=False)
