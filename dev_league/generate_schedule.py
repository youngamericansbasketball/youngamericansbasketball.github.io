import csv
import itertools
import random

def make_division_scheds(input_file, output_file):
    # Read team names from CSV
    teams = []
    with open(input_file, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        team_col_index = 0

        for row in reader:
            if row:
                teams.append(row[team_col_index])

    # If odd number of teams, add a BYE
    bye = None
    if len(teams) % 2 == 1:
        bye = "BYE"
        teams.append(bye)

    num_teams = len(teams)
    half = num_teams // 2

    # Create round-robin pairings using the circle method
    rotation = teams[:]
    all_rounds = []

    for _ in range(num_teams - 1):
        round_matches = []
        for i in range(half):
            t1 = rotation[i]
            t2 = rotation[num_teams - 1 - i]
            if t1 != bye and t2 != bye:
                round_matches.append((t1, t2))
        all_rounds.append(round_matches)

        # Rotate teams (except the first)
        rotation = [rotation[0]] + rotation[-1:] + rotation[1:-1]

    # We now have a full round-robin. But we only need 5 weeks.
    # If fewer than 5 rounds exist, we repeat rounds as needed.
    schedule = []
    while len(schedule) < 5:
        schedule.extend(all_rounds)

    schedule = schedule[:5]  # keep only 5 weeks

    # Write schedule to CSV
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["week", "home_team", "away_team"])

        for week_number, games in enumerate(schedule, start=1):
            for home, away in games:
                writer.writerow([week_number, home, away])

    print(f"5-week schedule generated and saved to {output_file}")
    
def make_master_sched(input_file, output_file):
    print("Combining division schedules into master schedule...")
    
    all_games = []
    division_files = [
        "prek-k_schedule.csv",
        "1-3_grade_schedule.csv",
        "4-6_grade_schedule.csv",
        "7-12_grade_schedule.csv"]
    for division_file in division_files:
        with open(f"{input_file}{division_file}", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                all_games.append(row)  # row is [week, home_team, away_team]
                
    # Shuffle all games to randomize order
    # random.shuffle(all_games)
    
    # Write master schedule to CSV
    with open(output_file, "w", encoding="utf-8") as f:
        # Sort by week number (first column)
        all_games.sort(key=lambda x: int(x[0]))
        
        # Write to CSV
        writer = csv.writer(f)
        writer.writerow(["week", "home_team", "away_team"])
        for game in all_games:
            writer.writerow(game)
            
    print(f"Master schedule generated and saved to {output_file}")


if __name__ == "__main__":
    # Make the individual division schedules
    make_division_scheds("./dev_league/manually_update/team_names/prek-k.csv", "./dev_league/auto_generated/prek-k_schedule.csv")
    make_division_scheds("./dev_league/manually_update/team_names/1-3_grade.csv", "./dev_league/auto_generated/1-3_grade_schedule.csv")
    make_division_scheds("./dev_league/manually_update/team_names/4-6_grade.csv", "./dev_league/auto_generated/4-6_grade_schedule.csv")
    make_division_scheds("./dev_league/manually_update/team_names/7-12_grade.csv", "./dev_league/auto_generated/7-12_grade_schedule.csv")
    # Combine into master schedule
    make_master_sched("./dev_league/auto_generated/", "./dev_league/auto_generated/master_schedule.csv")
