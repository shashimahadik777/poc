from pathlib import Path


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

    with input_file.open("r", encoding="utf-8") as reader, output_file.open("w", encoding="utf-8") as writer:
        for index, raw_line in enumerate(reader, start=1):
            processed = transform_line(raw_line)
            if processed:
                writer.write(f"{index}: {processed}\n")
