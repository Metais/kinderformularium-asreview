# DRD Reference Extractor for ASReview

## Overview

This repository contains a simple tool for automatically extracting references from DRD (in `.docx` format) files stored in a folder named `DRDs` and converting them into CSV format. The resulting `.csv` files are organized within a new `csv` folder created inside the `DRDs` directory. These CSV files can then be used as input for [ASReview](https://asreview.nl/), a tool designed for automated systematic reviewing.

## Features

- **Batch Processing**: Automatically processes all `.docx` files within the `DRDs` folder.
- **One-Click Execution**: A user-friendly executable (.exe) that simplifies the reference extraction process.
- **CSV Output**: Generates `.csv` files formatted correctly for use with ASReview.
- **Folder Management**: Automatically creates a `csv` folder within the `DRDs` directory to store the output files.

## How It Works

1. **Folder Setup**: Ensure all `.docx` files you want to process are located in a folder named `DRDs`.
2. **Run the Tool**: Double-click the provided `.exe` file.
3. **Output**: The tool will extract references from each `.docx` file and save them in separate `.csv` files within a newly created `csv` folder inside the `DRDs` directory.

## Installation & Usage

1. **Download the Tool**: Download the latest release from the [Releases](https://github.com/Metais/kinderformularium-asreview/releases) section.
2. **Prepare Your Files**: Move all `.docx` files you want to convert into a folder named `DRDs`. Make sure the `.exe` file is in the same folder as the `DRDs` folder.
3. **Execute**: Double-click the `extractor.exe` file.
4. **Review Output**: Open the `csv` folder inside the `DRDs` directory to find your extracted references in CSV format.

## Folder Structure

After running the tool, your folder structure should look like this:

```
extractor.exe
DRDs/
│
├── document1.docx
├── document2.docx
│
└── csv/
    ├── document1.csv
    └── document2.csv
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
