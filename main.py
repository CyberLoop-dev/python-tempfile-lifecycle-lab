#!/usr/bin/env python3
"""Show temporary path lifetimes without leaving files behind."""
import argparse
import json
import tempfile
from pathlib import Path

def run_demo(base_dir=None):
    report = {}
    with tempfile.TemporaryDirectory(prefix="tempfile-lab-", dir=base_dir) as folder:
        folder_path = Path(folder)
        sample = folder_path / "example.txt"
        sample.write_text("temporary directory example\n", encoding="utf-8")
        report["temporary_directory"] = {
            "path": str(folder_path),
            "directory_exists_inside_context": folder_path.exists(),
            "file_exists_inside_context": sample.exists(),
            "file_size": sample.stat().st_size,
        }
    report["temporary_directory"]["directory_exists_after_context"] = folder_path.exists()
    with tempfile.NamedTemporaryFile(mode="w+", prefix="tempfile-lab-", suffix=".txt", delete=True, encoding="utf-8") as handle:
        handle.write("temporary named file\n")
        handle.flush()
        named_path = Path(handle.name)
        report["named_file"] = {
            "path": str(named_path),
            "exists_inside_context": named_path.exists(),
            "read_back": named_path.read_text(encoding="utf-8"),
        }
    report["named_file"]["exists_after_context"] = named_path.exists()
    return report

def main():
    parser = argparse.ArgumentParser(description="Demonstrate temporary-file cleanup.")
    parser.add_argument("--base-dir", help="existing directory to hold the TemporaryDirectory demo")
    parser.add_argument("--json", action="store_true", help="print JSON")
    args = parser.parse_args()
    try:
        report = run_demo(args.base_dir)
    except OSError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for section, values in report.items():
            print(section.replace("_", " ").title())
            for key, value in values.items():
                print(f"  {key.replace('_', ' ')}: {value}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
