# Archive Content Lister

A simple GUI application that lists the contents of archive files (ZIP, 7Z, RAR) and saves them to a text file.

## Features

- Support for multiple archive formats:
  - ZIP files
  - 7Z files
  - RAR files
- User-friendly GUI interface
- Automatically creates an output directory
- Saves archive contents to text files
- Clear status messages and error handling

## Requirements

- Python 3.6+
- Required Python packages:
  - py7zr
  - rarfile
- For RAR support:
  - Windows: WinRAR
  - Linux: `unrar`
  - macOS: `unrar`

## Installation

1. Clone this repository:
```bash
git clone https://github.com/F47E/Zip-Content-Lister.git
cd Zip-Content-Lister
```

2. Install required Python packages:
```bash
pip install py7zr rarfile
```

3. Install RAR support for your operating system:
- Windows: Install WinRAR
- Linux: `sudo apt-get install unrar`
- macOS: `brew install unrar`

## Usage

1. Run the application:
```bash
python archive-lister.py
```

2. Use the GUI to:
   - Click "Browse" to select an archive file
   - View the output directory path
   - Click "Process Archive File" to generate the listing

The contents list will be saved in the `output` directory with the name format: `archive_name.extension.txt`

## Error Handling

The application handles various errors including:
- Invalid archive files
- Missing archive files
- File access permissions
- Unsupported archive formats

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is a permissive license that is short and to the point. It lets people do anything they want with your code as long as they provide attribution back to you and don't hold you liable.

## Author

[F47E](https://github.com/F47E)
