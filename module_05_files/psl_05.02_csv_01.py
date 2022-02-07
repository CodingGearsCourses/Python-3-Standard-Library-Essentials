# --------------------------------
# CodingGears.io
# --------------------------------
# Working with csv files

# TODO: Import csv
import csv

# List of lists
phone_number_list = [["John", "111-111-1111", "Bombay"],
                     ["Peter", "222-222-222", "Boston"],
                     ["Mouse", "333-333-3333", "Dallas"]]

# TODO: csv file
file_csv = "sample_data/my_csv_data.csv"

# TODO: Write the list to a file in csv format
# with open(file_csv, "w", newline="\n") as csv_file_handler1:
#     csv_writer = csv.writer(csv_file_handler1)
#     csv_writer.writerows(phone_number_list)
#     csv_writer.writerow(["Kelly", "123-000-0000", "Austin"])
#     csv_writer.writerow(["Kooper", "123-111-1111", "Denver"])

# TODO:  Read row by row
with open(file_csv, "r", newline="\n") as csv_file_handler2:
    csv_reader = csv.reader(csv_file_handler2)
    for row in csv_reader:
        print(row[0] + " : " + row[1] + " (" + row[2] + ")")

