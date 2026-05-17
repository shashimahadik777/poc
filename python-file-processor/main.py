from src.processor import process_file, generate_timestamped_filename
from pathlib import Path
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Read an input file, process it, and write a final output file.")
    parser.add_argument("input_file", help="Path to the input text file.")
    parser.add_argument("--output-file", "-o", help="Path to the output text file. If not provided, generates a timestamped filename.")
    parser.add_argument("--output-dir", "-d", default="output", help="Directory for output file (used when output_file is not specified).")
    return parser.parse_args()


def main():
    args = parse_args()
    
    # Determine output file path
    if args.output_file:
        output_path = args.output_file
    else:
        # Generate timestamped filename in the specified directory
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamped_name = generate_timestamped_filename("output", "txt")
        output_path = output_dir / timestamped_name
    
    print(f"📂 Input file: {args.input_file}")
    print(f"💾 Output file: {output_path}")
    print(f"⏳ Processing...")
    
    process_file(args.input_file, str(output_path))
    
    print(f"✅ Done! File saved successfully.")


if __name__ == "__main__":
    main()
