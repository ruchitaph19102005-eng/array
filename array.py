def parse_scores_from_string(s):
    parts = [p.strip() for p in s.replace(",", " ").split()]
    scores = []

    for p in parts:
        if p == "":
            continue
        try:
            scores.append(float(p))
        except ValueError:
            print(f"Warning: skipping non-numeric token: {p}")

    return scores

def read_scores():
    # Always prompt user interactively
    raw = input("Enter scores separated by spaces or commas: ")
    return parse_scores_from_string(raw)

def main():
    scores = read_scores()

    if not scores:
        print("No valid scores provided.")
        return

    total = sum(scores)
    avg = total / len(scores)

    print("=== Scores Output ===")
    print(f"Count: {len(scores)}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")

    # Local branch output: max & min
    print("\n=== Local branch output (max & min) ===")
    print(f"Maximum: {max(scores)}")
    print(f"Minimum: {min(scores)}")

if __name__ == "__main__":
    main()
