import re

def analyze_memory(memory):
    """
    Extracts 'mul(x, y)', 'don't()', and 'do()' instructions from memory,
    along with their positions in the memory string.

    :param memory: String containing the memory data.
    :return: List of dictionaries with pattern, match, start, and end positions.
    """
    # Define regex patterns
    patterns = {
        "mul": r"mul\(\d{1,3},\d{1,3}\)",
        "don't": r"don't\(\)",
        "do": r"do\(\)"
    }

    # List to store matches
    matches = []

    # Debug: Start of analysis
    print(f"DEBUG: Starting analysis of memory with length {len(memory)}.")

    # Find all matches for each pattern
    for pattern_name, pattern in patterns.items():
        print(f"DEBUG: Searching for pattern '{pattern_name}' using regex '{pattern}'.")
        for match in re.finditer(pattern, memory):
            match_info = {
                "pattern": pattern_name,
                "match": match.group(),
                "start": match.start(),
                "end": match.end()
            }
            matches.append(match_info)
            print(f"DEBUG: Found match for '{pattern_name}' at positions {match.start()}-{match.end()}: {match.group()}.")

    # Sort matches by starting position
    matches_sorted = sorted(matches, key=lambda x: x['start'])

    # Debug: Summary of findings
    print(f"DEBUG: Analysis complete. Total matches found: {len(matches_sorted)}.")
    for match in matches_sorted:
        print(f"DEBUG: Pattern '{match['pattern']}' - Match '{match['match']}' at [{match['start']}, {match['end']}].")

    return matches_sorted

def filter_matches_based_on_conditions(matches):
    """
    Filters the list of ordered matches, saving only certain items based on whether
    a 'do' or 'don't' appears earlier in the list.

    :param matches: List of dictionaries containing match details.
    :return: List of filtered matches.
    """
    filtered_matches = []
    allow_save = None  # Initialize flag to track the last "do" or "don't".

    for match in matches:
        if match['pattern'] == 'do':
            allow_save = True  # Allow saving subsequent items.
            print(f"DEBUG: Found 'do' at {match['start']}. Allowing save of subsequent items.")
        elif match['pattern'] == "don't":
            allow_save = False  # Prevent saving subsequent items.
            print(f"DEBUG: Found 'don't' at {match['start']}. Preventing save of subsequent items.")
        elif match['pattern'] == 'mul':
            if allow_save:
                filtered_matches.append(match)
                print(f"DEBUG: Saving 'mul' at {match['start']} because of preceding 'do'.")
            else:
                print(f"DEBUG: Skipping 'mul' at {match['start']} because of preceding 'don't' or no 'do'.")
    
    return filtered_matches

def extract_mul_matches(matches):
    """
    Extracts the 'match' values for items with the pattern 'mul'.

    :param matches: List of dictionaries containing match details.
    :return: List of strings containing only the 'mul' matches.
    """
    return [match['match'] for match in matches if match['pattern'] == 'mul']


def extract_coordinates(matches):
    """
    Extracts numerical coordinates from the list of matches.
    
    :param matches: List of strings matching the pattern, e.g., ["mul(123,456)", "mul(78,90)"].
    :return: List of tuples with extracted coordinates, e.g., [(123, 456), (78, 90)].
    """
    coordinates = [
        tuple(map(int, re.findall(r"\d{1,3}", match))) for match in matches
    ]
    print(f"DEBUG: Extracted {len(coordinates)} coordinate pairs.")
    return coordinates


def multiply_and_sum(coordinates):
    """
    Multiplies each pair of coordinates and sums the results.
    
    :param coordinates: List of tuples, e.g., [(123, 456), (78, 90)].
    :return: Total sum of the multiplications.
    """
    total_sum = sum(x * y for x, y in coordinates)
    print(f"DEBUG: Total sum of all products: {total_sum}")
    return total_sum


if __name__ == "__main__":
    # Define the input file path
    input_file = "puzzles/day3/day3_input.txt"

    try:
        with open(input_file, "r") as f:
            memory = f.read()
    except FileNotFoundError:
        print(f"ERROR: Input file '{input_file}' not found.")
        exit(1)
    except ValueError as e:
        print(f"ERROR: Failed to process memory. {e}")
        exit(1)

    print(f"DEBUG: Memory read successfully. First 20 characters: {memory[:20]}")

    # Analyze memory and calculate results
    matches = analyze_memory(memory)
    filtered_matches = filter_matches_based_on_conditions(matches)
    muls = extract_mul_matches(filtered_matches)
    coordinates = extract_coordinates(muls)
    total = multiply_and_sum(coordinates)
