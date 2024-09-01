# DRD Reference Extractor for ASReview

(Scroll down for more information on the second tool: the ASReview output processor)

## Overview

This repository contains a simple tool for automatically extracting references from DRD (in `.docx` format) files stored in a folder named `DRDs` and converting them into CSV format. The resulting `.csv` files are organized within a new `csv` folder created inside the `DRDs` directory. These CSV files can then be used as input for [ASReview](https://asreview.nl/), a tool designed for automated systematic reviewing.

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

# ASReview Output Processor

## Overview

This tool is designed to process ASReview output files, simplifying the workflow for systematic review projects. The program takes care of extracting and processing relevant data from the ASReview-generated files, outputting a new Excel file with the results.

## How It Works

Before running the program, ensure you have the following:

1. ASReview output files in .xlsx format, in a folder named "ExcelFiles".
2. Corresponding .asreview files with the same name as the .xlsx files, in a folder named "ASReviewFiles".
3. The configuration file (config.txt) found in this repository.
4. Once the previous steps are set up, run `process_asreview_output.exe`, found in the [Releases](https://github.com/Metais/kinderformularium-asreview/releases) section.

## Folder Structure

Make sure your project directory is organized as follows:

```
project_directory/
│
├── ExcelFiles/
│   ├── your_file_1.xlsx
│   ├── your_file_2.xlsx
│   └── ...
│
├── ASReviewFiles/
│   ├── your_file_1.asreview
│   ├── your_file_2.asreview
│   └── ...
│
├── config.txt
└── ASReviewOutputProcessor.exe
```

## Configuration

The config.txt file allows you to customize the program's behavior, so that it either includes or excludes the check on full text availability of a paper for your institution:

```
# Set to 'true' if you want to add another column detailing possible lack of full-text capability
only_full_texts=false

# Set to your institution's URL for the WorldCat website, only matters if the previous setting is set to 'true'
institution_worldcat_url=https://ru.on.worldcat.org/
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
