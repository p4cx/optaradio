from globals_web import *
import csv


def load_country_choices():
    def parse_unicode_to_list():
        country_list = []
        with open(UNICODE_FLAG_FILE, "rb") as f:
            lines = f.readlines()
            for line in lines:
                code_line = line.decode("utf-8", "replace")
                if code_line[0:3] == "1F1" and code_line[6:9] == "1F1":
                    country = code_line[76:].strip()
                    country_list.append(country)
            f.close()
        return country_list

    if not os.path.isfile(UNICODE_COUNTRIES_LIST):
        with open(UNICODE_COUNTRIES_LIST, 'w', newline='') as f:
            wr = csv.writer(f)
            country_list = parse_unicode_to_list()
            for country in country_list:
                wr.writerow([country])
            wr.writerow(["Rainbow"])
            f.close()

    country_list = []
    with open(UNICODE_COUNTRIES_LIST, 'r') as f:
        country_csv = csv.reader(f)
        for country in country_csv:
            country_list.append(country[0])
        f.close()
        return country_list
