# ============================================================
# FILE DATA ANALYZER SYSTEM
# Google Colab Implementation
# ============================================================

import os
import glob
import json
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import files


# ============================================================
# 1. CONFIGURATION
# ============================================================

SUPPORTED_EXTENSIONS = [".txt", ".csv", ".json", ".xlsx", ".xls"]

SUMMARY_FILE = "file_analysis_summary.csv"

# Cache prevents the same file from being loaded repeatedly
DATA_CACHE = {}

# Stores files uploaded in the current session
UPLOADED_FILES = []


# ============================================================
# 2. GENERAL UTILITY FUNCTIONS
# ============================================================

def print_separator():
    print("\n" + "=" * 70)


def clean_filename(filename):
    """
    Returns only the filename without directory information.
    """
    return os.path.basename(filename)


def get_extension(filename):
    """
    Returns the lowercase file extension.
    """
    return os.path.splitext(filename)[1].lower()


def count_words(text):
    """
    Counts words in a string.
    """
    if text is None:
        return 0

    text = str(text)
    return len(re.findall(r"\b[\w'-]+\b", text))


# ============================================================
# 3. WORD COUNT FUNCTIONS
# ============================================================

def count_words_in_text(text):
    """
    Word count for TXT content.
    """
    return count_words(text)


def count_words_in_dataframe(df):
    """
    Counts words only in text/string columns of a DataFrame.
    """
    total = 0

    object_columns = df.select_dtypes(include=["object", "string"]).columns

    for column in object_columns:
        total += df[column].fillna("").astype(str).apply(count_words).sum()

    return int(total)


def count_words_in_json(data):
    """
    Recursively counts words in JSON keys and string values.
    """

    total = 0

    if isinstance(data, dict):
        for key, value in data.items():
            total += count_words(str(key))
            total += count_words_in_json(value)

    elif isinstance(data, list):
        for item in data:
            total += count_words_in_json(item)

    elif isinstance(data, str):
        total += count_words(data)

    return total


# ============================================================
# 4. FILE LOADING FUNCTIONS
# ============================================================

def load_text_file(filename):
    """
    Reads a TXT file.
    """

    encodings = ["utf-8", "latin1"]

    for encoding in encodings:
        try:
            with open(filename, "r", encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue

    raise ValueError("Unable to decode text file.")


def load_csv_file(filename):
    """
    Reads CSV using UTF-8 first and latin1 as fallback.
    """

    try:
        return pd.read_csv(filename, encoding="utf-8")

    except UnicodeDecodeError:
        return pd.read_csv(filename, encoding="latin1")


def load_json_file(filename):
    """
    Reads JSON file.
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def load_excel_file(filename):
    """
    Reads Excel file.
    """

    return pd.read_excel(filename)


def load_file(filename):
    """
    Loads a file according to its extension.

    Uses cache so the same file is not repeatedly loaded.
    """

    filename = clean_filename(filename)

    if filename in DATA_CACHE:
        return DATA_CACHE[filename]

    extension = get_extension(filename)

    if extension == ".txt":
        data = load_text_file(filename)

    elif extension == ".csv":
        data = load_csv_file(filename)

    elif extension == ".json":
        data = load_json_file(filename)

    elif extension in [".xlsx", ".xls"]:
        data = load_excel_file(filename)

    else:
        raise ValueError(
            f"Unsupported file format: {extension}"
        )

    DATA_CACHE[filename] = data

    return data


# ============================================================
# 5. FIND SUPPORTED FILES USING GLOB
# ============================================================

def get_files_using_glob():
    """
    Finds supported files using glob.

    The generated summary report is excluded so it does not
    become an input file during the next execution.
    """

    detected_files = []

    for extension in SUPPORTED_EXTENSIONS:

        pattern = f"*{extension}"

        matching_files = glob.glob(pattern)

        for filename in matching_files:

            filename = clean_filename(filename)

            if filename == SUMMARY_FILE:
                continue

            if filename not in detected_files:
                detected_files.append(filename)

    return sorted(detected_files)


# ============================================================
# 6. FILE INFORMATION
# ============================================================

def get_file_type(filename):
    """
    Returns a readable file type.
    """

    extension = get_extension(filename)

    mapping = {
        ".txt": "Text",
        ".csv": "CSV",
        ".json": "JSON",
        ".xlsx": "Excel",
        ".xls": "Excel"
    }

    return mapping.get(extension, "Unknown")


# ============================================================
# 7. SECTION 1 - TEXT FILE PROCESSING
# ============================================================

def text_file_processing(filename):
    """
    Processes only TXT files.

    Output is intentionally limited to text-file information.
    """

    print_separator()
    print("TEXT FILE PROCESSING")
    print_separator()

    if get_extension(filename) != ".txt":
        print("Selected file is not a TXT file.")
        return

    text = load_file(filename)

    lines = text.splitlines()
    characters = len(text)
    words = count_words_in_text(text)

    print(f"File       : {filename}")
    print(f"Lines      : {len(lines)}")
    print(f"Characters : {characters}")
    print(f"Words      : {words}")


# ============================================================
# 8. SECTION 2 - CSV FILE PROCESSING
# ============================================================

def csv_file_processing(filename):
    """
    Processes only CSV files.

    Shows dataset structure and constraints.
    """

    print_separator()
    print("CSV FILE PROCESSING")
    print_separator()

    if get_extension(filename) != ".csv":
        print("Selected file is not a CSV file.")
        return

    df = load_file(filename)

    print(f"File    : {filename}")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names:")
    for column in df.columns:
        print(f"- {column}")

    print("\nDataset Constraints:")

    print(f"Missing Values : {int(df.isnull().sum().sum())}")
    print(f"Duplicate Rows : {int(df.duplicated().sum())}")

    numeric_columns = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    print(f"Numeric Columns: {len(numeric_columns)}")


# ============================================================
# 9. SECTION 3 - JSON FILE PROCESSING
# ============================================================

def json_file_processing(filename):
    """
    Processes only JSON files.

    Shows JSON structure without printing unrelated analyses.
    """

    print_separator()
    print("JSON FILE PROCESSING")
    print_separator()

    if get_extension(filename) != ".json":
        print("Selected file is not a JSON file.")
        return

    data = load_file(filename)

    print(f"File : {filename}")

    if isinstance(data, dict):

        print("Root Type : Dictionary")
        print(f"Number of Keys : {len(data)}")

        print("\nKeys:")
        for key in data.keys():
            print(f"- {key}")

    elif isinstance(data, list):

        print("Root Type : List")
        print(f"Number of Items : {len(data)}")

        if len(data) > 0:
            print(f"First Item Type : {type(data[0]).__name__}")

    else:

        print(f"Root Type : {type(data).__name__}")


# ============================================================
# 10. SECTION 4 - EXCEL FILE PROCESSING
# ============================================================

def excel_file_processing(filename):
    """
    Processes only Excel files.
    """

    print_separator()
    print("EXCEL FILE PROCESSING")
    print_separator()

    if get_extension(filename) not in [".xlsx", ".xls"]:
        print("Selected file is not an Excel file.")
        return

    df = load_file(filename)

    print(f"File    : {filename}")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names:")

    for column in df.columns:
        print(f"- {column}")


# ============================================================
# 11. SECTION 5 - WORD COUNT
# ============================================================

def word_count_processing(filename):
    """
    Counts words only.

    Does not display statistics, filtering or dataset details.
    """

    print_separator()
    print("WORD COUNT")
    print_separator()

    extension = get_extension(filename)

    data = load_file(filename)

    if extension == ".txt":

        total_words = count_words_in_text(data)

    elif extension in [".csv", ".xlsx", ".xls"]:

        total_words = count_words_in_dataframe(data)

    elif extension == ".json":

        total_words = count_words_in_json(data)

    else:

        print("Unsupported file format.")
        return

    print(f"File        : {filename}")
    print(f"Total Words : {total_words}")


# ============================================================
# 12. SECTION 6 - DATA FILTERING
# ============================================================

def data_filtering(filename):
    """
    Filters a numeric column.

    For the Superstore dataset, Sales > mean Sales is used.
    """

    print_separator()
    print("DATA FILTERING")
    print_separator()

    extension = get_extension(filename)

    if extension not in [".csv", ".xlsx", ".xls"]:
        print("Filtering requires a tabular file.")
        return

    df = load_file(filename)

    if "Sales" not in df.columns:

        numeric_columns = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        if len(numeric_columns) == 0:
            print("No numeric column available for filtering.")
            return

        column = numeric_columns[0]

    else:

        column = "Sales"

    mean_value = df[column].mean()

    filtered_df = df[df[column] > mean_value]

    print(f"File              : {filename}")
    print(f"Column            : {column}")
    print(f"Mean Value        : {mean_value:.2f}")
    print(f"Filter Condition  : {column} > {mean_value:.2f}")
    print(f"Filtered Rows     : {len(filtered_df)}")

    if len(filtered_df) > 0:

        print("\nFirst 5 Filtered Records:")

        display(filtered_df.head())


# ============================================================
# 13. SECTION 7 - STATISTICAL ANALYSIS
# ============================================================

def statistical_analysis(filename):
    """
    Performs descriptive statistical analysis only.
    """

    print_separator()
    print("STATISTICAL ANALYSIS")
    print_separator()

    extension = get_extension(filename)

    if extension not in [".csv", ".xlsx", ".xls"]:
        print("Statistical analysis requires a tabular file.")
        return

    df = load_file(filename)

    numeric_df = df.select_dtypes(include=np.number)

    if numeric_df.empty:
        print("No numeric columns found.")
        return

    print(f"File    : {filename}")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nNumeric Columns:")

    for column in numeric_df.columns:
        print(f"- {column}")

    print("\nDescriptive Statistics:")

    display(
        numeric_df.describe().round(3)
    )


# ============================================================
# 14. SECTION 8 - MULTIPLE FILE PROCESSING USING GLOB
# ============================================================

def multiple_file_processing():
    """
    Finds and processes multiple supported files using glob.

    Only a concise summary is printed.
    Detailed operations are available through the individual
    menu sections.
    """

    print_separator()
    print("MULTIPLE FILE PROCESSING USING GLOB")
    print_separator()

    file_list = get_files_using_glob()

    if not file_list:

        print("No supported files found.")
        return []

    print(f"Files Detected : {len(file_list)}")

    for index, filename in enumerate(file_list, start=1):

        print(
            f"{index}. {filename} "
            f"({get_file_type(filename)})"
        )

    return file_list


# ============================================================
# 15. SECTION 9 - DATA VISUALIZATION
# ============================================================

def data_visualization(filename):
    """
    Creates visualizations for numeric data.

    For Superstore:
    1. Sales histogram
    2. Sales vs Profit comparison
    """

    print_separator()
    print("DATA VISUALIZATION")
    print_separator()

    extension = get_extension(filename)

    if extension not in [".csv", ".xlsx", ".xls"]:

        print("Visualization requires a tabular file.")
        return

    df = load_file(filename)

    # --------------------------------------------------------
    # Visualization 1: Histogram
    # --------------------------------------------------------

    numeric_columns = df.select_dtypes(
        include=np.number
    ).columns.tolist()

    if len(numeric_columns) == 0:

        print("No numeric data available.")
        return

    preferred_column = (
        "Sales"
        if "Sales" in df.columns
        else numeric_columns[0]
    )

    plt.figure(figsize=(8, 5))

    plt.hist(
        df[preferred_column].dropna(),
        bins=30
    )

    plt.title(f"Distribution of {preferred_column}")
    plt.xlabel(preferred_column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    print(f"Histogram generated for: {preferred_column}")

    # --------------------------------------------------------
    # Visualization 2: Sales vs Profit
    # --------------------------------------------------------

    if "Sales" in df.columns and "Profit" in df.columns:

        sample_df = df[
            ["Sales", "Profit"]
        ].dropna().head(100)

        plt.figure(figsize=(8, 5))

        plt.bar(
            range(len(sample_df)),
            sample_df["Sales"],
            label="Sales"
        )

        plt.plot(
            range(len(sample_df)),
            sample_df["Profit"],
            label="Profit"
        )

        plt.title("Sales and Profit Comparison")
        plt.xlabel("Record Index")
        plt.ylabel("Value")
        plt.legend()
        plt.tight_layout()
        plt.show()

        print("Sales vs Profit visualization generated.")


# ============================================================
# 16. AUTOMATIC BATCH SUMMARY
# ============================================================

def create_summary_report(file_list):
    """
    Creates a concise CSV report.

    One row is generated for each input file.
    """

    print_separator()
    print("AUTOMATIC SUMMARY REPORT")
    print_separator()

    summary_data = []

    for filename in file_list:

        extension = get_extension(filename)

        try:

            data = load_file(filename)

            file_type = get_file_type(filename)

            rows = ""
            columns = ""
            words = 0

            # ------------------------------------------------
            # TXT
            # ------------------------------------------------

            if extension == ".txt":

                rows = len(data.splitlines())
                columns = ""
                words = count_words_in_text(data)

            # ------------------------------------------------
            # CSV / Excel
            # ------------------------------------------------

            elif extension in [".csv", ".xlsx", ".xls"]:

                rows = data.shape[0]
                columns = data.shape[1]
                words = count_words_in_dataframe(data)

            # ------------------------------------------------
            # JSON
            # ------------------------------------------------

            elif extension == ".json":

                if isinstance(data, list):
                    rows = len(data)

                elif isinstance(data, dict):
                    rows = len(data)

                else:
                    rows = 1

                columns = ""
                words = count_words_in_json(data)

            summary_data.append(
                {
                    "File": filename,
                    "Type": file_type,
                    "Rows": rows,
                    "Columns": columns,
                    "Words": words
                }
            )

        except Exception as error:

            summary_data.append(
                {
                    "File": filename,
                    "Type": get_file_type(filename),
                    "Rows": "Error",
                    "Columns": "Error",
                    "Words": "Error"
                }
            )

            print(
                f"Could not process {filename}: {error}"
            )

    summary_df = pd.DataFrame(summary_data)

    summary_df.to_csv(
        SUMMARY_FILE,
        index=False
    )

    print(f"Report created : {SUMMARY_FILE}")
    print(f"Files analyzed : {len(summary_df)}")

    print("\nSummary:")

    display(summary_df)

    return summary_df


# ============================================================
# 17. FILE SELECTION
# ============================================================

def select_file(file_list):
    """
    Lets the user select one file.
    """

    if not file_list:

        print("No files available.")
        return None

    print_separator()
    print("SELECT FILE")
    print_separator()

    for index, filename in enumerate(file_list, start=1):

        print(
            f"{index}. {filename} "
            f"[{get_file_type(filename)}]"
        )

    while True:

        try:

            choice = int(
                input(
                    "\nEnter file number: "
                )
            )

            if 1 <= choice <= len(file_list):

                return file_list[choice - 1]

            print("Please enter a valid number.")

        except ValueError:

            print("Please enter a number.")


# ============================================================
# 18. MAIN MENU
# ============================================================

def show_menu():

    print_separator()
    print("FILE DATA ANALYZER SYSTEM")
    print_separator()

    print("1. Text File Processing")
    print("2. CSV File Processing")
    print("3. JSON File Processing")
    print("4. Excel File Processing")
    print("5. Word Count")
    print("6. Data Filtering")
    print("7. Statistical Analysis")
    print("8. Multiple File Processing using glob")
    print("9. Data Visualization")
    print("10. Generate Summary Report")
    print("0. Exit")


# ============================================================
# 19. UPLOAD FILES
# ============================================================

print_separator()
print("UPLOAD FILES")
print_separator()

print(
    "Upload TXT, CSV, JSON or Excel files."
)

uploaded = files.upload()

UPLOADED_FILES = [
    clean_filename(filename)
    for filename in uploaded.keys()
]

print(
    f"\n{len(UPLOADED_FILES)} file(s) uploaded successfully."
)

for filename in UPLOADED_FILES:
    print(
        f"- {filename} "
        f"({get_file_type(filename)})"
    )


# ============================================================
# 20. GET AVAILABLE FILES
# ============================================================

available_files = get_files_using_glob()

if not available_files:

    print("\nNo supported files were found.")
    print("Please upload at least one supported file.")

else:

    print_separator()
    print("AVAILABLE FILES")
    print_separator()

    for index, filename in enumerate(
        available_files,
        start=1
    ):

        print(
            f"{index}. {filename} "
            f"[{get_file_type(filename)}]"
        )


# ============================================================
# 21. MENU LOOP
# ============================================================

while True:

    show_menu()

    choice = input(
        "\nEnter your choice: "
    ).strip()

    # --------------------------------------------------------
    # OPTION 1
    # --------------------------------------------------------

    if choice == "1":

        filename = select_file(
            available_files
        )

        if filename:
            text_file_processing(filename)

    # --------------------------------------------------------
    # OPTION 2
    # --------------------------------------------------------

    elif choice == "2":

        filename = select_file(
            available_files
        )

        if filename:
            csv_file_processing(filename)

    # --------------------------------------------------------
    # OPTION 3
    # --------------------------------------------------------

    elif choice == "3":

        filename = select_file(
            available_files
        )

        if filename:
            json_file_processing(filename)

    # --------------------------------------------------------
    # OPTION 4
    # --------------------------------------------------------

    elif choice == "4":

        filename = select_file(
            available_files
        )

        if filename:
            excel_file_processing(filename)

    # --------------------------------------------------------
    # OPTION 5
    # --------------------------------------------------------

    elif choice == "5":

        filename = select_file(
            available_files
        )

        if filename:
            word_count_processing(filename)

    # --------------------------------------------------------
    # OPTION 6
    # --------------------------------------------------------

    elif choice == "6":

        filename = select_file(
            available_files
        )

        if filename:
            data_filtering(filename)

    # --------------------------------------------------------
    # OPTION 7
    # --------------------------------------------------------

    elif choice == "7":

        filename = select_file(
            available_files
        )

        if filename:
            statistical_analysis(filename)

    # --------------------------------------------------------
    # OPTION 8
    # --------------------------------------------------------

    elif choice == "8":

        available_files = (
            multiple_file_processing()
        )

    # --------------------------------------------------------
    # OPTION 9
    # --------------------------------------------------------

    elif choice == "9":

        filename = select_file(
            available_files
        )

        if filename:
            data_visualization(filename)

    # --------------------------------------------------------
    # OPTION 10
    # --------------------------------------------------------

    elif choice == "10":

        available_files = get_files_using_glob()

        if available_files:

            create_summary_report(
                available_files
            )

        else:

            print(
                "No supported files found."
            )

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    elif choice == "0":

        print_separator()
        print("Program ended successfully.")
        print_separator()

        break

    # --------------------------------------------------------
    # INVALID CHOICE
    # --------------------------------------------------------

    else:

        print(
            "\nInvalid choice. "
            "Please select an option from 0 to 10."
        )