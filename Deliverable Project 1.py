name = input("Welcome to GC mini golf! What is your name? ")
print("Hi, {}!".format(name))

holes = input("How many holes would you like to play (3-6)? ")

# Validate user input
while holes not in ["3", "4", "5", "6"]:
    print("Invalid input. Please choose a number of holes between 3 and 6.")
    holes = input("How many holes would you like to play (3-6)? ")

par = int(holes) * 3

total_score = 0
for i in range(1, int(holes) + 1):
    putts = int(input("How many putts for hole {}? (par: {}) ".format(i, 3)))
    total_score += putts

score_diff = total_score - par
if score_diff < 0:
    print("Great job, {}! Your total score was: {}.".format(name, score_diff))
elif score_diff > 0:
    print("Nice try, {}... Your total score was: +{}.".format(name, score_diff))
else:
    print("Good game, {}. Your total score was: 0.".format(name))

