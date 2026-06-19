show1_people = int(input("Enter the number of people who watched show 1"))
show1_rating = float(input("Enter the average rating for show 1"))

show2_people = int(input("Enter the number of people who watched show 2"))
show2_rating = float(input("Enter the average rating for show 2"))

show3_people = int(input("Enter the number of people who watched show 3"))
show3_rating = float(input("Enter the average rating for show 3"))

total_people = show1_people + show2_people + show3_people

total_rating = (
    show1_people * show1_rating +
    show2_people * show2_rating +
    show3_people * show3_rating
)

average_rating = total_rating / total_people

print(f"The overall average rating for the show is {average_rating:.2f}") 