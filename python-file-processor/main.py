from src.processor import process_file
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Read an input file, process it, and write a final output file.")
    parser.add_argument("input_file", help="Path to the input text file.")
    parser.add_argument("output_file", help="Path to the output text file.")
    return parser.parse_args()


def main():
    args = parse_args()
    process_file(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
