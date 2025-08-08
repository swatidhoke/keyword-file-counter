#!/usr/bin/env python3
"""
find_keyword_counts.py
Recursively walk a root directory, find files matching a regex in filename or content,
count matches per subdirectory, and output results to JSON and a bar chart.

Usage:
    python find_keyword_counts.py --root_dir /path/to/root --keyword "regex_pattern"
"""

import os
import re
import argparse
import json
import matplotlib.pyplot as plt

def search_file_for_keyword(filepath, keyword_pattern, search_mode):
    """Check if a file matches the regex based on the search_mode."""
    regex = re.compile(keyword_pattern)

    match_found = False
    if search_mode in ("filename", "both"):
        if regex.search(os.path.basename(filepath)):
            return True

    if search_mode in ("content", "both"):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if regex.search(line):
                        match_found = True
                        break
        except Exception:
            pass

    return match_found


def walk_and_count(root_dir, keyword_pattern, search_mode):
    """Walk directory and count matching files per subdirectory."""
    results = {}
    for dirpath, _, filenames in os.walk(root_dir):
        rel_dir = os.path.relpath(dirpath, root_dir)
        if rel_dir == ".":
            rel_dir = ""
        count = 0
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if search_file_for_keyword(filepath, keyword_pattern, search_mode):
                count += 1
        results[rel_dir] = count
    return results


def save_results_json(results, output_path):
    """Save dictionary results to JSON."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)


def plot_results(results, output_path):
    """Plot a bar chart of the results."""
    dirs = list(results.keys())
    counts = list(results.values())

    plt.figure(figsize=(10, 6))
    plt.bar(dirs, counts)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Subdirectory")
    plt.ylabel("Matching File Count")
    plt.title("Keyword Match Counts per Subdirectory")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Count files matching a regex in a directory tree.")
    parser.add_argument("--root_dir", required=True, help="Root directory to start traversal.")
    parser.add_argument("--keyword", required=True, help="Regex pattern to match.")
    parser.add_argument("--mode", choices=["filename", "content", "both"], default="both",
                        help="Search in filename, content, or both. Default: both.")
    parser.add_argument("--output_dir", default=".", help="Directory to save results.")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    # Count matches
    results = walk_and_count(args.root_dir, args.keyword, args.mode)

    # Save JSON
    json_path = os.path.join(args.output_dir, "results.json")
    save_results_json(results, json_path)

    # Save plot
    plot_path = os.path.join(args.output_dir, "results.png")
    plot_results(results, plot_path)

    print(f"✅ Results saved to {json_path}")
    print(f"📊 Plot saved to {plot_path}")


if __name__ == "__main__":
    main()
