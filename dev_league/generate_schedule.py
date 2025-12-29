import csv
import itertools
import math

def generate_schedule(input_file="manually_update/teams.csv", output_file="auto_generated/schedule.csv"):
    # Read team names from CSV
    teams = []
    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        team_col_index = 0

        # If header contains "team", use that column
        if "4-6" in [h.lower() for h in header]:
            print(header)
            team_col_index = [h.lower() for h in header].index("4-6")

        for row in reader:
            teams.append(row[team_col_index])

    # Generate all unique matchups
    matchups = list(itertools.combinations(teams, 2))

    # Split matchups into 5 weeks as evenly as possible
    total_weeks = 5
    games_per_week = math.ceil(len(matchups) / total_weeks)

    weeks = []
    for i in range(total_weeks):
        start = i * games_per_week
        end = start + games_per_week
        weeks.append(matchups[start:end])

    # Write schedule to CSV
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["week", "home_team", "away_team"])

        for week_number, games in enumerate(weeks, start=1):
            for home, away in games:
                writer.writerow([week_number, home, away])

    print(f"5-week schedule generated and saved to {output_file}")
    

#def test():
    #print("YAY")

if __name__ == "__main__":
    generate_schedule()
    #test()
