
# Keyword File Counter

A stand-alone Python 3 script that recursively traverses a given root directory, searches for files matching a given **regular expression keyword**, and counts matches for each subdirectory.  
It can search in **filenames**, **file contents**, or **both**, and can output results as a JSON file and/or a bar chart.

---

## Requirements

- Python 3.8 or higher
- pip (Python package installer)
- Required Python packages:
  - `matplotlib` (only if you want a graph)
  - `argparse` (usually comes with Python)
  - `re` (comes with Python)
  - `os` (comes with Python)

---

## Installation

1. **Clone or copy this script** to your local machine:
```bash
git clone https://github.com/swatidhoke/keyword-file-counter.git
cd keyword-file-counter
````

2. **Install dependencies** (only needed for plotting):

```bash
python3 -m pip install matplotlib
```

---

## Usage

Run the script with:

```bash
python3 find_keyword_counts.py --root_dir /path/to/root --keyword "YOUR_REGEX"
```

### Arguments

| Argument       | Required | Description                                                         |
| -------------- | -------- | ------------------------------------------------------------------- |
| `--root_dir`   | Yes      | Root directory to start traversal                                   |
| `--keyword`    | Yes      | Regular expression for keyword match                                |
| `--mode`       | No       | Where to search: `filename`, `content`, or `both` (default: `both`) |
| `--out`        | No       | Output type: `json`, `plot`, or `both` (default: `both`)            |
| `--output-dir` | No       | Directory where results will be saved (default: current dir)        |

---

### Examples

1. **Search for files starting with `test_` in filenames only**:

   ```bash
   python3 find_keyword_counts.py --root_dir ./myfolder --keyword "^test_" --mode filename
   ```

2. **Search for keyword inside file contents**:

   ```bash
   python3 find_keyword_counts.py --root_dir ./docs --keyword "Confidential" --mode content
   ```

3. **Save results as JSON and plot in `./output` folder**:

   ```bash
   python3 find_keyword_counts.py --root_dir ./src --keyword "TODO" --mode both --out both --output-dir ./output
   ```

---

## Output

* **JSON File**: Contains `{subdir: count}` mapping.
* **PNG File**: Bar chart of counts per subdir (requires `matplotlib`).

Example JSON:

```json
{
  "": 0,
  "a": 1,
  "a/b": 2,
  "a/b/c": 0
}
```

---

## Testing

You can create a small test dataset like this:

```bash
mkdir -p test_root/a/b/c
echo "TESTResult content" > test_root/a/file_TESTResult.txt
echo "no match here" > test_root/a/b/file1.txt
echo "TESTResult in content" > test_root/a/b/c/file2.txt
```

Run:

```bash
python3 find_keyword_counts.py --root_dir ./test_root --keyword "TESTResult"
```


 
