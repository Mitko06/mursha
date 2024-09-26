import csv
#
infile=  open('people.csv', mode='r', encoding='utf-8')
reader = csv.reader(infile)

#
filtered_people = []
# обработване на всеки ред в файла
for row in reader:
# Извличаме данни
        first_name = row[0]
        last_name = row[1]
        age = int(row[2])

   # Променяме възрастта  
        if first_name =='Август' and last_name == 'Попов':
                age=35

# филтриране на дадените критерии   
        if age < 38 and last_name != "Писаров" :
                filtered_people.append([first_name, last_name, age,])

infile.close()

print("Filtered People:")
for person in filtered_people:
       print(person)

# филтрираните данни се записват в нов файл с кодиране    
outfile =  open('people_filtered.csv' , mode='w' , encoding="utf-8" , newline='') 
writer = csv.writer(outfile)

#Записване на  филтрираните данни
writer.writerows(filtered_people)
outfile.close()

checkfile = open('people_filtered.csv' , mode='r', encoding="utf-8")
reader = csv.reader(checkfile)
print("Output File Content:")
for row in reader:
    print(row)

    checkfile.close()
else:
    print("NO data to write to the output file.")