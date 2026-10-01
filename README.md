# File Data Analyzer System

> A reusable, menu-driven Python system for analyzing TXT, CSV, JSON,
> and Excel files in Google Colab.

## Overview

The File Data Analyzer System provides one workflow for reading multiple
file formats and performing common data-analysis operations. It supports
word counting, data filtering, descriptive statistics, visualization,
multiple-file discovery using `glob`, data-quality checks, batch
processing, and automatic CSV summary generation.

The implementation is designed for Google Colab and uses Pandas and
NumPy for data processing, with Matplotlib for visualization and Python
standard libraries for file handling.

## Key Features

-   **TXT processing** --- lines, characters, and word count.
-   **CSV processing** --- rows, columns, column names, missing values,
    duplicates, and numeric-column information.
-   **JSON processing** --- root structure, keys/items, and word
    counting.
-   **Excel processing** --- worksheet data structure and column
    information.
-   **Word counting** --- supported for TXT, CSV, Excel, and JSON
    content.
-   **Data filtering** --- numeric filtering, including the demonstrated
    `Sales > mean(Sales)` condition.
-   **Statistical analysis** --- descriptive statistics for numeric
    columns.
-   **Data visualization** --- numeric distribution and Sales/Profit
    comparison charts where applicable.
-   **Multiple-file processing** --- automatic discovery with Python
    `glob`.
-   **Automatic summary report** --- creates
    `file_analysis_summary.csv`.
-   **Data-quality checks** --- missing values and duplicate rows.
-   **Data caching** --- avoids unnecessarily loading the same file
    repeatedly.
-   **Report exclusion** --- the generated summary CSV is excluded from
    future input discovery.

## Objectives

1.  Provide a reusable workflow for analyzing different file formats.
2.  Automate common data-analysis operations.
3.  Reduce repetitive analysis code.
4.  Support batch processing of multiple files.
5.  Produce statistical and visual insights.
6.  Generate a concise machine-readable summary report.
7.  Provide a simple interactive interface suitable for Google Colab.

## Technology Stack

  Technology             Purpose
  ---------------------- ------------------------------------------
  Python                 Core implementation
  Pandas                 Data loading, manipulation, and analysis
  NumPy                  Numeric data handling
  Matplotlib             Visualization
  `glob`                 Multiple-file discovery
  `json`                 JSON processing
  `os`                   File/path handling
  `re`                   Word-count pattern matching
  Google Colab           Execution environment
  `google.colab.files`   File upload

## Supported Formats

  -----------------------------------------------------------------------
  Format                  Extension               Main Operations
  ----------------------- ----------------------- -----------------------
  Text                    `.txt`                  Text processing, word
                                                  count

  CSV                     `.csv`                  Structure, word count,
                                                  filtering, statistics,
                                                  visualization

  JSON                    `.json`                 Structure, word count

  Excel                   `.xlsx`, `.xls`         Structure, word count,
                                                  filtering, statistics,
                                                  visualization
  -----------------------------------------------------------------------

## System Workflow

``` text
File Upload
     ↓
File Format Detection
     ↓
Appropriate File Loader
     ↓
Cached Data
     ↓
Selected Analysis Operation
     ├── Word Count
     ├── Data Filtering
     ├── Statistical Analysis
     ├── Visualization
     └── File/Format Processing
     ↓
Batch Processing / Summary Report
     ↓
file_analysis_summary.csv
```

## Interactive Menu

``` text
1. Text File Processing
2. CSV File Processing
3. JSON File Processing
4. Excel File Processing
5. Word Count
6. Data Filtering
7. Statistical Analysis
8. Multiple File Processing using glob
9. Data Visualization
10. Generate Summary Report
0. Exit
```

Each option has a separate responsibility. For example, the Word Count
option reports word-count information only, while Statistical Analysis
reports numeric descriptive statistics. This prevents the repetitive
output seen when unrelated operations are combined.

## Demonstration Dataset

The demonstrated implementation uses the **Sample - Superstore** CSV
dataset.

  Property                       Demonstrated Result
  ---------------------------- ---------------------
  Rows                                         9,994
  Columns                                         21
  Missing values                                   0
  Duplicate rows                                   0
  Numeric columns                                  6
  Word count                                 333,992
  Mean Sales                                 229.858
  Median Sales                                 54.49
  Mean Profit                                 28.657
  Median Profit                                8.667
  Sales standard deviation                   623.245
  Profit standard deviation                  234.260
  Rows with Sales above mean                   2,360

These figures describe the demonstrated dataset execution and are not
hard-coded requirements for every future input file.

## Dataset Constraints

The demonstrated dataset has:

-   9,994 rows and 21 columns.
-   No missing values.
-   No duplicate rows.
-   Six numeric fields.
-   `Sales` as the demonstrated filtering field.
-   A mean-based filtering condition.
-   333,992 words across analyzed text columns.

The system itself is not restricted to these exact dimensions; it
detects the structure of the supplied input.

## Processing Logic

### TXT

The system reads text content, counts lines and characters, and
calculates the number of words.

### CSV

CSV files are read with UTF-8 first and Latin-1 as a fallback. The
system can inspect structure, count words in string columns, filter
numeric data, calculate statistics, and visualize numeric values.

### JSON

JSON content is recursively inspected. Dictionary keys, string values,
and strings inside lists contribute to the word count.

### Excel

Excel files are read with Pandas and processed as tabular data using the
same relevant analysis functions as CSV files.

## Word Count

Word counting is performed using a regular-expression-based word
pattern.

For tabular files, only text/string columns are counted. Numeric fields
are not treated as words.

For JSON, the implementation recursively processes dictionary keys,
string values, and list contents.

## Data Filtering

For the demonstrated Superstore dataset:

``` text
Column: Sales
Condition: Sales > Mean Sales
Mean Sales: approximately 229.86
Filtered rows: 2,360
```

The function displays the filtering condition, resulting row count, and
a sample of matching records.

## Statistical Analysis

The statistical module:

1.  Loads the selected tabular file.
2.  Identifies numeric columns.
3.  Uses Pandas descriptive statistics.
4.  Displays count, mean, standard deviation, minimum, quartiles, and
    maximum.

For the demonstrated dataset, mean Sales is approximately `229.858` and
mean Profit is approximately `28.657`.

## Visualization

The visualization module creates:

1.  A histogram for an available numeric field, preferring `Sales` when
    present.
2.  A Sales/Profit comparison visualization when both columns exist.

Charts are generated only when suitable numeric data is available.

## Multiple-File Processing

Python `glob` is used to discover supported files automatically.

Supported patterns include:

``` text
*.txt
*.csv
*.json
*.xlsx
*.xls
```

The generated `file_analysis_summary.csv` is excluded so that the system
does not accidentally analyze its own previous report.

## Automatic Summary Report

The system creates:

``` text
file_analysis_summary.csv
```

The report contains:

  Field     Description
  --------- ------------------------------------
  File      Input filename
  Type      Detected file type
  Rows      Number of records where applicable
  Columns   Number of columns where applicable
  Words     Calculated word count

## Robustness

The implementation includes:

-   UTF-8/Latin-1 CSV fallback.
-   Unsupported-format checks.
-   Empty-directory handling.
-   Numeric-column validation before filtering/statistics.
-   Input validation for menu selections.
-   File caching.
-   Generated-report exclusion.
-   Error capture during batch summary generation.

## How to Run in Google Colab

1.  Open Google Colab.
2.  Create a new notebook.
3.  Paste the complete implementation into a code cell.
4.  Run the cell.
5.  Upload TXT, CSV, JSON, or Excel files when prompted.
6.  Select an operation from the menu.
7.  Use option `10` to generate the summary report.

The generated report will be saved as:

``` text
file_analysis_summary.csv
```

## Example Workflow

``` text
Upload Sample - Superstore.csv
        ↓
CSV File Processing
        ↓
View dataset structure and constraints
        ↓
Word Count
        ↓
View total word count
        ↓
Data Filtering
        ↓
View filtered records
        ↓
Statistical Analysis
        ↓
View descriptive statistics
        ↓
Data Visualization
        ↓
View charts
        ↓
Generate Summary Report
        ↓
file_analysis_summary.csv
```

## Project Structure

``` text
File Data Analyzer System/
├── README.md
├── analyzer.py
├── file_analysis_summary.csv
└── input files/
    ├── sample.txt
    ├── sample.csv
    ├── sample.json
    └── sample.xlsx
```

For Google Colab, the implementation may also be maintained entirely
inside a notebook.

## Future Enhancements

Possible extensions include:

-   Additional statistical measures.
-   More chart types.
-   Interactive visualizations.
-   Automated PDF/Excel reports.
-   Advanced filtering conditions.
-   Multi-column filtering.
-   Data cleaning.
-   Outlier detection.
-   Correlation analysis.
-   Automated dashboards.
-   Database connectivity.
-   Scheduled or recurring analysis.
-   A standalone web or desktop interface.

## Advantages

-   Reusable across multiple supported formats.
-   Modular function-based design.
-   Menu-driven and easy to operate.
-   Supports batch file discovery.
-   Reduces repeated file loading through caching.
-   Provides both numerical and visual analysis.
-   Generates a structured summary report.
-   Easy to extend with additional operations.

## Limitations

1.  Filtering is currently centered on numeric columns and a mean-based
    demonstration condition.
2.  Visualization is limited to the implemented chart types.
3.  Excel processing operates on the worksheet data loaded by Pandas.
4.  Very large datasets may require additional memory-management
    techniques.
5.  The current interface is intended for Google Colab.

## Conclusion

The File Data Analyzer System provides a modular and reusable workflow
for analyzing multiple file formats in Google Colab. It combines file
handling, word counting, filtering, descriptive statistics,
visualization, batch processing, data-quality checks, and automatic
reporting.

The separation of operations ensures that each menu option produces
focused, non-repetitive output. The implementation can also be extended
with additional analytics, reporting, visualization, and automation
features.

## Keywords

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Google Colab` · `CSV` ·
`JSON` · `Excel` · `TXT` · `Data Analysis` · `Statistics` ·
`Data Filtering` · `Visualization` · `Batch Processing` · `glob` ·
`Automation`

## License

This implementation is intended for educational and academic use. It may
be modified and extended for learning, demonstration, and data-analysis
purposes.
