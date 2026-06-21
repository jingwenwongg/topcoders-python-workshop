from datetime import datetime

date1 = input()
date2 = input()

start_date = datetime.strptime(date1, "%b %d %Y %I:%M%p")
end_date = datetime.strptime(date2, "%b %d %Y %I:%M%p")

difference = end_date - start_date

print(f"{difference.days} days, {difference.seconds // 3600}:{(difference.seconds % 3600) // 60:02d}:{difference.seconds % 60:02d}")