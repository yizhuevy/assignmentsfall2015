import csv

# Open our input and output files
csvfile = open('cleanme.csv', 'r')
outfile = open('cleaned.csv', 'w') 
# 'w' open a file for writing. create a new file to put the cleaned-up info

# Now a DictReader and DictWriter
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)


#write headers
writer.writeheader()

zip = str(zip)


# Clean and write the data to output
for row in reader:
    row['first_name'] = row['first_name'].upper()
    row['zip'] = row['zip'].zfill(5)
    row['addr'] = row['addr'].replace(" ", "")
    row['city'] = row['city'].replace("&nbsp;", "")
    if int(row['amount']) < 1000:
    		 dict.clear(row);
   # print row
    writer.writerow(row)


	