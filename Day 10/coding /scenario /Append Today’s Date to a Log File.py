#Append Today’s Date to a Log File

#Explanation:We open the file in append mode ("a") so new entries are added without erasing old ones. We use the datetime module to get today’s date.

from datetime import datetime

# Open log file in append mode
with open("daily_log.txt", "a") as f:
    today = datetime.now().strftime("%Y-%m-%d")
    f.write(f"{today} - Task Completed\n")

print("Date appended to log file.")
