# AI Recommendation System

print("===================================")
print(" AI Recommendation System ")
print("===================================")

# Recommendation database
recommendations = {
    "technology": [
        "Python Programming",
        "Artificial Intelligence",
        "Web Development"
    ],
    "sports": [
        "Cricket",
        "Football",
        "Badminton"
    ],
    "music": [
        "Classical Music",
        "Pop Music",
        "Instrument Learning"
    ],
    "movies": [
        "Science Fiction",
        "Action Movies",
        "Comedy Movies"
    ],
    "books": [
        "Programming Books",
        "Novels",
        "Self-Improvement Books"
    ]
}

while True:
    print("\nAvailable Interests:")
    print("Technology, Sports, Music, Movies, Books")
    print("Type 'exit' to quit")

    interest = input("\nEnter your interest: ").lower()

    if interest == "exit":
        print("Thank you for using the Recommendation System!")
        break

    elif interest in recommendations:
        print("\nRecommended Items:")
        for item in recommendations[interest]:
            print("->", item)

    else:
        print("\nSorry! No recommendations available for that interest.")
