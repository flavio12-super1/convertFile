import csv

with open('dim_stop_times_latest.csv', 'r') as csv_file:
    with open('data.txt', 'w') as tsv_file:
        csv_reader = csv.reader(csv_file)
        tsv_writer = csv.writer(tsv_file, delimiter='\t')

        for row in csv_reader:
            tsv_writer.writerow(row)