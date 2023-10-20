# Python Pip Helper CLI Tool

## Overview

This Python Pip Helper CLI Tool is designed to simplify the process of searching for and installing Python packages using `pip`. It allows you to search for packages, view package details, and install selected packages from the command line.

## Features

- Search for Python packages on PyPI.
- View package details including name, version, and description.
- Install selected packages to your Python environment.

## ScreenShot
![ArcoLinux-2023-10-09-1696872740_screenshot_1920x1080](https://github.com/raunakwete43/pypilot/assets/104648854/a43012b1-3d33-4889-9cbc-9bbd06d9a248)

## Prerequisites

Before using the tool, ensure that you have the following prerequisites installed:

- Python (3.6 or higher)
- `pip` package manager
- Required Python libraries: `requests`, `click`, `beautifulsoup4`

You can install the required libraries using `pip`:

```bash
pip install requests click beautifulsoup4
```

## Installation

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the script using Python:

```bash
python3 pypilot.py <package-name>
```

## Usage

### Searching for Packages

To search for packages, use the following command:

```bash
python3 pypilot.py <package-name> --pages=<number-of-pages>
```

- `<package-name>`: The name of the package you want to search for.
- `--pages`: (Optional) The number of pages to search (default is 1).

### Viewing Package Details

After searching for packages, the tool will display a list of packages with their details, including an index number.

### Installing Packages

To install packages, follow these steps:

1. In the displayed list of packages, note the index numbers of the packages you want to install.

2. Enter the index numbers separated by spaces when prompted to select the package(s) to install. For example, to install packages with indexes 1, 2, and 3, you can enter: `1 2 3`.

3. The selected packages will be installed to your Python environment.

### Example Usage

Here's an example of how to use the tool:

```bash
python3 pypilot.py numpy --page=2
```

This command searches for the "numpy" package across 2 pages of results, displays package details, and allows you to select and install packages.

## Color Customization

The tool uses `click.style` for text formatting and color customization. You can customize the colors in the code to match your terminal's color scheme.

## Error Handling

The tool provides error handling for various scenarios, such as invalid package names, installation errors, and input validation.

## Notes

- The tool checks if a package is already installed in your Python environment and indicates it as "(Installed)" in the package details.

- The default number of pages to search is set to 1. If you specify a higher number of pages, the tool will limit the search to the available pages.

- Inconsistent data on a page may occur if the web page structure changes. The tool provides a warning in such cases.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Raunak Wete]

## Acknowledgments

- [click](https://click.palletsprojects.com/en/7.x/) - A Python package for creating command-line interfaces.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - A library for web scraping and parsing HTML and XML.
- [PyPI](https://pypi.org/) - The Python Package Index.
