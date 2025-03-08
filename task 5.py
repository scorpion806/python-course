########################    1-Love Calculator  ###############################
def calculate_love_score(name1, name2):
    combined_names = (name1  + name2).lower()

    true_count = sum([combined_names.count(letter) for letter in "true"])
    love_count = sum([combined_names.count(letter) for letter in "love"])

    love_score = int(f"{true_count}{love_count}")

    counts = {letter: combined_names.count(letter) for letter in "true"}
    print("TRUE counts:")
    for letter, count in counts.items():
        print(f"{letter.upper()} occurs {count} times")
    print(f"Total = {true_count}\n")

    counts = {letter: combined_names.count(letter) for letter in "love"}
    print("LOVE counts:")
    for letter, count in counts.items():
        print(f"{letter.upper()} occurs {count} times")
    print(f"Total = {love_count}\n")

    print(f"Love Score = {love_score}")

    return love_score

name1 = "Angela Yu"
name2 = "Jack Bauer"
calculate_love_score(name1, name2)

#############################
