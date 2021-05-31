# fileparse.py
#
# Exercise 3.17 - Michael King

#From filenames to file-like objects

import csv

def parse_csv(lines, select = None, types=[str, int, float], has_headers = True, delimiter=',', silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''

    if select and not has_headers:
        raise RuntimeError('select argument requires column headers') #Raise a runtime error if columns are specified but 'has_headers' is false
        

    rows = csv.reader(lines, delimiter=delimiter)

        # Read the file headers
    headers = next(rows) if has_headers else []

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:    # Skip rows with no data
            continue
            # Filter the row if specific columns were selected
        if indices:
            row = [ row[index] for index in indices ]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

            #Make a tuple or dictionary

        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records
