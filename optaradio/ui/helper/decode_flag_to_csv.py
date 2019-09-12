import csv

from globals import *


# structure of the csv-file
# filename, country


def parse_unicode_to_list():
    file_list = []
    country_list = []
    with open(UNICODE_FLAG_FILE, "rb") as f:
        lines = f.readlines()
        for line in lines:
            code_line = line.decode("utf-8", "replace")
            if code_line[0:3] == "1F1" and code_line[6:9] == "1F1":
                file = code_line[0:11].replace(" ", "-", 1)
                country = code_line[76:].strip()
                file_list.append(file)
                country_list.append(country)
        f.close()
    return file_list, country_list


def save_unicode_csv():
    if not os.path.isfile(UNICODE_FLAG_LIST):
        with open(UNICODE_FLAG_LIST, 'w', newline='') as f:
            wr = csv.writer(f, delimiter=";")
            file_list, country_list = parse_unicode_to_list()
            for num, file in enumerate(file_list):
                wr.writerow([file, country_list[num]])
            f.close()
