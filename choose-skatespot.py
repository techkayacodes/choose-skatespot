import random

# List of locations
locations = [
    "IS 5",
    "Astoria Skatepark",
    "52nd Park",
    "71st. Couldesac",
    "30th street-ish Skillman Ledge"
]

# Randomly select one location
final_location = random.choice(locations)

# Print out the final selected location
print(f"The final selected location is: {final_location}")
