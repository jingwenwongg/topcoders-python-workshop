branding = int(input("Enter branding expenses"))
travel = int(input("Enter travel expenses"))
food = int(input("Enter food expenses"))
logistics = int(input("Enter logistics expenses"))

total = float(branding + travel + food + logistics)

branding_pct = (branding / total) * 100
travel_pct = (travel / total) * 100
food_pct = (food / total) * 100
logistics_pct = (logistics / total) * 100

print (f"Total expenses : Rs.{total:.2f}")
print (f"Branding expenses percentage : {branding_pct:.2f}%")
print (f"Travel expenses percentage : {travel_pct:.2f}%")
print (f"Food expenses percentage : {food_pct:.2f}%")
print (f"Logistics expenses percentage : {logistics_pct:.2f}%")