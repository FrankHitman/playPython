import os
import sqlite3
import pandas as pd

def create_table(cursor, table_name, columns):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    if cursor.fetchone() is None:
        columns_definition = ", ".join([f"{col} TEXT" for col in columns])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})")

def insert_data(cursor, table_name, data):
    cursor.execute(f"PRAGMA table_info({table_name})")
    table_info = cursor.fetchall()
    num_columns = len(table_info)
    
    filtered_data = []
    for row in data:
        if len(row) < num_columns:
            row.extend([None] * (num_columns - len(row)))
        if len(row) > num_columns and pd.isna(row[0]):
            row.pop(0)
        if not pd.isna(row[1]):  # 过滤掉第二列为空的行
            filtered_data.append(row)
    data = filtered_data
    placeholders = ", ".join(["?" for _ in range(num_columns)])
    cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", data)

def process_excel_file(file_path, cursor):
    xls = pd.ExcelFile(file_path)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        if not df.empty:
            columns = df.columns.tolist()
            columns = [str(col).replace(': ','') if str(col).startswith('Unnamed') else str(col) for col in columns ]  # handle the first nil column
            create_table(cursor, 'QA', columns)
            data = df.values.tolist()
            insert_data(cursor, 'QA', data)

def process_directory(directory, cursor):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xls') or file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                process_excel_file(file_path, cursor)

def main():
    directory = os.path.dirname(os.path.abspath(__file__))

    db_path = os.path.join(directory ,'extracted_data.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    process_directory(directory, cursor)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

