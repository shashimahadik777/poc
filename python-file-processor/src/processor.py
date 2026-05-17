from pathlib import Path
from datetime import datetime


def generate_timestamped_filename(base_name: str = "output", extension: str = "txt") -> str:
    """Generate a filename with current date and time.
    
    Args:
        base_name: The base filename without extension
        extension: The file extension (without dot)
    
    Returns:
        A filename string with format: base_name_YYYY-MM-DD_HH-MM-SS.extension
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{base_name}_{timestamp}.{extension}"


def transform_line(line: str) -> str:
    """Process a single input line and return the transformed output line."""
    normalized = line.strip()
    if not normalized:
        return ""
    return normalized.upper()


def process_file(input_path: str, output_path: str) -> None:
    """Read the input file, process each line, and write the final output file."""
    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    line_count = 0
    with input_file.open("r", encoding="utf-8") as reader, output_file.open("w", encoding="utf-8") as writer:
        for index, raw_line in enumerate(reader, start=1):
            processed = transform_line(raw_line)
            if processed:
                writer.write(f"{index}: {processed}\n")
                line_count += 1
    
    print(f"   Processed {line_count} lines")
