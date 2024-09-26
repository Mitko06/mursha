import csv

def filter_and_correct_people(input_file, output_file):
    with open(input_file, mode='r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        
        
        with open(output_file, mode='w', encoding="utf-8", newline='') as csvfile_out:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            
            
            writer.writeheader()
            
            for row in reader:
                
                if row['Име'] == 'Август' and row['Фамилия'] == 'Попов':
                    row['Години'] = '35'
                
                
                if int(row['Години']) < 38 and row['Фамилия'] != 'Писаров':
                    writer.writerow(row)

input_file = 'people.csv'
output_file = 'people_filtered.csv'


filter_and_correct_people(input_file, output_file)
