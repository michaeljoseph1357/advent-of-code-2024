def calculate_total_distance(left_list, right_list):
    # Sort both lists
    print("\nDEBUG: Sorting the lists...")
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    print(f"DEBUG: Sorted left list: {left_sorted[:10]}... (showing first 10)")
    print(f"DEBUG: Sorted right list: {right_sorted[:10]}... (showing first 10)")
    
    # Calculate the sum of absolute differences
    print("\nDEBUG: Calculating absolute differences...")
    differences = [abs(l - r) for l, r in zip(left_sorted, right_sorted)]
    print(f"DEBUG: First 10 differences: {differences[:10]} (showing first 10)")
    
    total_distance = sum(differences)
    print(f"DEBUG: Total distance: {total_distance}")
    return total_distance

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

    # Calculate total distance
    result = calculate_total_distance(left_list, right_list)
    print(f"\nFinal Result: Total distance: {result}")
