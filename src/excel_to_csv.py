def excel_to_csv(excel_file, csv_file):
    """Converts an Excel file to a CSV file.

    Args:
        excel_file: Path to the Excel file (.xlsx).
        csv_file: Path to save the CSV file.
    """
    try:
        df = pd.read_excel(excel_file)  # Read the Excel file
        df.to_csv(csv_file, index=False, encoding='utf-8')  # Save as CSV
        print(f"File '{excel_file}' converted to '{csv_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{excel_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
excel_file='../Data/data.xlsx'
csv_file='../Data'
excel_to_csv(excel_file,csv_file)
