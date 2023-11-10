# File README.md

## Description
This script is designed to download files from a list of URLs. It includes functionality for measuring the download time of each file and provides an option to save downloaded files locally.

## Usage

### Prerequisites
- Python 3.x installed

### Installation
No additional installation steps are required.

### Running the Script
1. Open a terminal.
2. Navigate to the directory containing the script.
3. Run the script using the following command:
   ```bash
   python script_name.py input_file.txt [--smode]
   ```
   - `script_name.py`: The name of the script file.
   - `input_file.txt`: The file containing a list of download URLs.
   - `--smode`: (Optional) Enable save mode to save downloaded files locally.

### Example
```bash
python download_script.py sample_urls.txt --smode
```

### Options
- **input_file.txt**: Required argument. Specify the file containing the list of download URLs.
- **--smode**: Optional argument. Enable save mode to save downloaded files locally.

### Output
- The script will display the download progress, including the filename, download time, and any errors encountered.
- After completion, it generates a JSON file named `statistic_input_file.txt_DD-MM-YYYY.json` containing download statistics.

## Important Notes
- Invalid URLs or URLs without a scheme will be skipped.
- Ensure that the input file exists before running the script.
- Save mode (`--smode`) will save files in the current working directory.

## License
This script is released under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.