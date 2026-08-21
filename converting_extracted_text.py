from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any
import json

with open("FM_UNICODE_PAIRS.json", "r", encoding="utf-8") as f:
    mappings = json.load(f)

mapping_dict = {
    item["legacy"]: item["unicode"]
    for item in mappings
}

def build_trie(pairs: tuple[tuple[str, str], ...]) -> dict[str, Any]:
    root: dict[str, Any] = {}
    for legacy, unicode_text in pairs:
        if not legacy:
            continue
        node = root
        for character in legacy:
            node = node.setdefault(character, {})
        node.setdefault("", unicode_text)
    return root


def fm_abhaya_to_unicode(text: str) -> str:
    """Convert FM Abhaya / FM Abaya encoded text to Sinhala Unicode."""

    if not text:
        return ""

    # Longest mappings must be checked first
    mappings = sorted(
        mapping_dict.items(),
        key=lambda x: len(x[0]),
        reverse=True
    )

    output = []
    index = 0

    while index < len(text):
        matched = False

        for legacy, unicode_text in mappings:
            if text.startswith(legacy, index):
                output.append(unicode_text)
                index += len(legacy)
                matched = True
                break

        if not matched:
            output.append(text[index])
            index += 1

    return "".join(output)


def extract_and_convert_pdf(text: str | Path) -> str:
    """Extract FM Abhaya text from a PDF and convert it to Unicode."""
    return fm_abhaya_to_unicode(text)


def convert_file(input_path: str | Path, output_path: str | Path) -> Path:
    """Convert a PDF or UTF-8 legacy text file and save UTF-8 Unicode text."""
    input_file = Path(input_path)
    output_file = Path(output_path)

    if input_file.suffix.lower() == ".pdf":
        unicode_text = extract_and_convert_pdf(input_file)
    else:
        unicode_text = fm_abhaya_to_unicode(input_file.read_text(encoding="utf-8"))

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(unicode_text, encoding="utf-8")
    return output_file