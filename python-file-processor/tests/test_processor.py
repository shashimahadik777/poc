from pathlib import Path
from src.processor import transform_line, process_file
import pytest


def test_transform_line_returns_uppercase():
    assert transform_line(" hello world \n") == "HELLO WORLD"


def test_transform_line_ignores_blank_lines():
    assert transform_line("   \n") == ""


def test_process_file_creates_output(tmp_path: Path):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    input_file.write_text("line one\nline two\n", encoding="utf-8")

    process_file(str(input_file), str(output_file))

    content = output_file.read_text(encoding="utf-8")
    assert "1: LINE ONE" in content
    assert "2: LINE TWO" in content


def test_process_file_missing_input_raises():
    with pytest.raises(FileNotFoundError):
        process_file("missing.txt", "output.txt")
