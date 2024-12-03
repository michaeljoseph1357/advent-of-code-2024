from collections import Counter

def calculate_total_distance(left_list, right_list):
    # Part 1: Sort and calculate the sum of absolute differences
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    differences = [abs(l - r) for l, r in zip(left_sorted, right_sorted)]
    total_distance = sum(differences)
    return total_distance

def calculate_similarity_score(left_list, right_list):
    # Part 2: Calculate similarity score
    print("\nDEBUG: Calculating similarity score...")
    right_count = Counter(right_list)  # Count occurrences in the right list
    print(f"DEBUG: Right list counts: {dict(list(right_count.items())[:10])}... (showing first 10)")
    
    similarity_score = 0
    for number in left_list:
        count = right_count[number]
        score = number * count
        similarity_score += score
        print(f"DEBUG: Number: {number}, Count in Right: {count}, Partial Score: {score}")
    
    print(f"DEBUG: Final similarity score: {similarity_score}")
    return similarity_score

if __name__ == "__main__":
    # Define the relative path to the input file
    input_file = "puzzles/day1/day1_input.txt"
    left_list = []
    right_list = []

    print("\nDEBUG: Reading the input file...")
    try:
        with open(input_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Split each line into two numbers
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
    except FileNotFoundError:
        print(f"ERROR: Input file '{input_file}' not found. Please check the path.")
        exit(1)
    except ValueError as e:
        print(f"ERROR: Failed to process a line in the input file. Check the file format. {e}")
        exit(1)

    print(f"DEBUG: Number of entries in left list: {len(left_list)}")
    print(f"DEBUG: Number of entries in right list: {len(right_list)}")
    print(f"DEBUG: First 10 entries in left list: {left_list[:10]}")
    print(f"DEBUG: First 10 entries in right list: {right_list[:10]}")

    # Part 1: Calculate total distance
    part1_result = calculate_total_distance(left_list, right_list)
    print(f"\nPart 1 Result: Total distance: {part1_result}")

    # Part 2: Calculate similarity score
    part2_result = calculate_similarity_score(left_list, right_list)
    print(f"\nPart 2 Result: Similarity score: {part2_result}")
