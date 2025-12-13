import os
import sys

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
    # 1️⃣ Use CLI arguments if provided
    if len(sys.argv) > 1:
        return parse_scores_from_string(" ".join(sys.argv[1:]))

    # 2️⃣ Use environment variable SCORES
    env = os.getenv("SCORES")
    if env:
        return parse_scores_from_string(env)

    # 3️⃣ Only prompt if interactive terminal
    if sys.stdin.isatty():
        raw = input("Enter scores separated by spaces or commas: ")
        return parse_scores_from_string(raw)

    # 4️⃣ No input available
    print("No scores provided via arguments, SCORES env, or interactive input.")
    return []

def main():
    scores = read_scores()

    if not scores:
        print("No valid scores provided.")
        sys.exit(1)

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
