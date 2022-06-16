import csv
import json
import math
import os
from pathlib import Path
from pprint import pprint



###################################################################################################
#  Environment Variables
###################################################################################################
maximum_allowable_rows = 20
file_counter = 0
row_counter = 0
source_dir = Path('/home/tweedledee101/dev/csv')
output_dir = Path('/home/tweedledee101/dev/csv/output_files/')
files = source_dir.glob('test.csv')
fieldname = []

make_output_file_directory = f'mkdir {output_dir}'
os.system(make_output_file_directory)




##################################################################################################
# Processing Checks
##################################################################################################
for file in files:
    print(file, "\n")

with open('test.csv', 'r') as f:
    dict_object = csv.DictReader(f)
    for row in dict_object:
        fieldnames = row.keys()
        print(fieldnames)
        for field in fieldnames:
            fieldname.append(field)
        break

    print(f"This is our list fieldname:\n{fieldname}")

    # nothing too crazy here, I just wanna check programmatically how much data we'll be processing
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    print(f"This is the type of Data: {type(data)}")
    row_count = len(data)
    print(f"Total number of rows: {row_count}")

    #Using math ceiling to round up to the nearest whole number
    files_to_create = math.ceil(row_count/maximum_allowable_rows)
    print(f"We're going to create {files_to_create} files")

    f.close()




###################################################################################################
# File Creation
###################################################################################################

with open('test.csv', 'r') as f:
    dict_object = csv.DictReader(f)

    #Now, while this read file is open, we need to create an output file.
    while file_counter < files_to_create:
        output_filename = f'test_{file_counter}.csv'
        print(f"File Number: {file_counter}")
        print(f"Filename: {output_filename}\n")
        file_counter += 1

        # The top of our loop states that we can only continue as long as the file_counter is less than the number
        # of files we would like to create: Now, we need to open a new file to write to
        with open(f'{output_dir}/{output_filename}', 'w', newline="", encoding="utf-8") as output:
            writer = csv.DictWriter(output, fieldnames=fieldname)
            writer.writeheader()
            print(f"Header Written to {output_filename}")
            
            for row in dict_object:
                row_counter += 1
                print(f"inside For Loop, File Number {file_counter}")
                print(f"Inside For Loop Row Number{row_counter}")
                #print(f"Row Values: {row}")
                writer.writerow(row)
                if row_counter >= maximum_allowable_rows:
                    row_counter = 0
                    break

