import csv
total_records = 0
unique_boroughs = set()
brooklyn_count = 0

with open('taxi_zone_lookup.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_records += 1
        unique_boroughs.add(row['Borough'])
        if row['Borough'] == 'Brooklyn':
            brooklyn_count += 1

sorted_boroughs = sorted(unique_boroughs)

with open('/root/taxi_zone_output.txt', 'w') as f:
    f.write(f"Total no.of records: {total_records}\n")
    f.write(f"Unique boroughs: {', '.join(sorted_boroughs)}\n")
    f.write(f"Number of records for Brooklyn: {brooklyn_count}\n")