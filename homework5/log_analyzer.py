import collections
import sys
from typing import Optional


def parse_log_line(line: str) -> dict:
    """
    Parses a single log line into a dictionary with keys: 'date', 'time', 'level', and 'message'.
    Args:
        line (str): A log line in the format 'DATE TIME LEVEL MESSAGE'.
    Returns:
        dict: A dictionary with parsed log information.
    Raises:
        ValueError: If the log line format is incorrect.
    """
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        raise ValueError(f"Invalid log format: {line}")
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3],
    }


def load_logs(file_path: str) -> list:
    """
    Loads log entries from a file, parsing each line into a dictionary.
    Args:
        file_path (str): Path to the log file.
    Returns:
        list: A list of dictionaries representing log entries.
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    logs.append(parse_log_line(line.strip()))
                except ValueError as e:
                    print(f"Error in line {line_number}: {e}")
                    return []
        return logs
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []


# для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters log entries by a specific log level.

    Args:
        logs (list): A list of log entries, where each entry is a dictionary.
        level (str): The log level to filter by (e.g., 'INFO', 'ERROR').

    Returns:
        list: A list of log entries that match the specified level.
    """
    filtered_logs = filter(lambda item: item['level'] == level, logs)
    return list(filtered_logs)


def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of log entries for each log level.
    Args:
        logs (list): A list of log entries, where each entry is a dictionary containing at least a 'level' key.
    Returns:
        dict: A dictionary where keys are log levels (e.g., 'INFO', 'ERROR') and values are their respective counts.
    """
    levels = [log['level'] for log in logs]
    level_count = collections.Counter(levels)
    return dict(level_count)


def display_log_counts(counts: dict) -> None:
    """
    Formats and displays log counts as a table.
    Args:
        counts (dict): A dictionary where keys are log levels (e.g., 'INFO', 'ERROR')
                       and values are the counts of each level.
    Returns:
        None: Prints the formatted table to the console.
    Example:
        Input:
        counts = {'INFO': 5, 'ERROR': 2, 'WARNING': 3}

        Output:
        Рівень логування | Кількість
        --------------------------
        INFO             | 5
        ERROR            | 2
        WARNING          | 3
    """
    # Define table headers
    header = ('Рівень логування', 'Кількість')
    # Calculate the maximum width for the first column
    first_column_header_width = len(header[0])
    first_column_data_width = max(list(map(lambda x: len(x), counts.keys())))
    first_column_width = max(first_column_header_width, first_column_data_width)
    # Print the table header
    print("{:<{width}} | {}".format(header[0], header[1], width=first_column_width))
    print("-" * (first_column_width + 3 + len(header[1])))
    # Print table rows with log level and their counts
    for level, count in counts.items():
        print("{:<{width}} | {}".format(level, count, width=first_column_width))


def display_logs(logs: list, level: Optional[str] = None) -> None:
    """
    Displays log details, optionally filtered by a specific log level.
    Args:
        logs (list): A list of log entries as dictionaries.
        level (str, optional): The log level to filter by (e.g., 'INFO', 'ERROR'). If None, all logs are displayed.
    Returns:
        None
    """
    level = f" для рівня '{level}'" if level else ''
    print(f"\nДеталі логів{level}:")
    if not logs:
        print("Empty")
    else:
        print('\n'.join(f"{log['date']} {log['time']} - {log['message']}" for log in logs))


def main():
    # Check if there are enough arguments provided
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer.py <log_file_path> [<log_level>]")
        return

    # Get the command line arguments
    file_path = sys.argv[1]
    level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    # Load logs from the specified file
    logs = load_logs(file_path)
    # If logs could not be loaded (file not found or parsing failed), stop further execution
    if not logs:
        return

    # Count the number of logs by level
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # If a log level is specified, filter the logs by that level
    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        display_logs(filtered_logs, level)


if __name__ == "__main__":
    main()
