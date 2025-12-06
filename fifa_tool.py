import csv

def load_players(filename):
    players = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            players.append(row)
    return players


def find_player(players, name):
    name = name.lower()
    for p in players:
        if p["short_name"].lower() == name:
            return p
    return None


def print_player(p):
    print("Name:", p["short_name"])
    print("Overall:", p["overall"])
    print("Age:", p["age"])
    print("Club:", p["club"])
    print("Position:", p["position"])


def show_top_players(players, n):
    # Sắp xếp theo chỉ số overall giảm dần
    sorted_players = sorted(
        players,
        key=lambda p: int(p["overall"]),
        reverse=True
    )
    print(f"\nTop {n} players by overall:")
    for p in sorted_players[:n]:
        print_player(p)
        print("-" * 20)


def main():
    players = load_players("players.csv")
    print("Loaded", len(players), "players.")

    while True:
        print("\nMenu:")
        print("1. Find player by name")
        print("2. Show top N players by overall")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter player name: ")
            player = find_player(players, name)
            if player is None:
                print("Player not found.")
            else:
                print_player(player)

        elif choice == "2":
            n_str = input("How many players to show? ")
            if not n_str.isdigit():
                print("Please enter a number.")
                continue
            n = int(n_str)
            show_top_players(players, n)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
