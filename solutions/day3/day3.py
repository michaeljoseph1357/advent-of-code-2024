import re

def analyze_memory(memory):
    """
    Extracts 'mul(x, y)' instructions from memory where x and y are 1- to 3-digit numbers.
    
    :param memory: String containing the memory data.
    :return: List of all valid matches.
    """
    # Define the regex pattern to match "mul(x, y)"
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    # Find all matches in the memory string
    matches = re.findall(pattern, memory)

    print(f"DEBUG: Found {len(matches)} valid 'mul' instructions.")
    return matches


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
    coordinates = extract_coordinates(matches)
    total = multiply_and_sum(coordinates)
