def is_safe_report(report):
    """
    Checks if a report is safe based on the given conditions.
    :param report: List of integers representing levels in the report.
    :return: True if the report is safe, otherwise False.
    """
    differences = [abs(report[i] - report[i+1]) for i in range(len(report) - 1)]

    # All differences must be in the range [1, 3]
    if not all(1 <= diff <= 3 for diff in differences):
        return False

    # Report must be strictly increasing or strictly decreasing
    is_increasing = all(report[i] < report[i+1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i+1] for i in range(len(report) - 1))

    return is_increasing or is_decreasing


def is_safe_with_dampener(report):
    """
    Checks if a report is safe by removing at most one level and rechecking.
    :param report: List of integers representing levels in the report.
    :return: True if the report is safe, otherwise False.
    """
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the level at index i
        if is_safe_report(modified_report):  # Check the modified report
            return True
    return False


def analyze_reports(reports):
    """
    Analyzes the reports, identifying safe and unsafe ones.
    :param reports: List of reports, each report being a list of integers.
    :return: Tuple containing count of safe reports and a list of unsafe reports.
    """
    safe_count = 0
    unsafe_reports = []

    for report in reports:
        if is_safe_report(report):
            safe_count += 1
        else:
            unsafe_reports.append(report)

    return safe_count, unsafe_reports


def count_safe_with_dampener(unsafe_reports):
    """
    Counts how many reports from the list of unsafe reports can be made safe with the Problem Dampener.
    :param unsafe_reports: List of unsafe reports.
    :return: The count of reports that are safe with the Problem Dampener.
    """
    return sum(is_safe_with_dampener(report) for report in unsafe_reports)


if __name__ == "__main__":
    # Define the input file path
    input_file = "puzzles/day2/day2_input.txt"
    reports = []

    try:
        with open(input_file, "r") as f:
            for line in f:
                reports.append(list(map(int, line.strip().split())))
    except FileNotFoundError:
        print(f"ERROR: Input file '{input_file}' not found.")
        exit(1)
    except ValueError as e:
        print(f"ERROR: Failed to process a line in the input file. {e}")
        exit(1)

    # Analyze reports
    safe_count, unsafe_reports = analyze_reports(reports)

    # Analyze unsafe reports with the Problem Dampener
    dampener_safe_count = count_safe_with_dampener(unsafe_reports)

    # Output results
    print(f"Total reports read: {len(reports)}")
    print(f"Total safe reports: {safe_count}")
    print(f"Total unsafe reports: {len(unsafe_reports)}")
    print(f"Total reports made safe with Problem Dampener: {dampener_safe_count}")
    print(f"Final Total Safe Reports (including Dampener): {safe_count + dampener_safe_count}")
