#Libry
import csv
import string
import random
#User input vlaues. If user input dows not meet the requerments we use default values and store them as variables
while True:
    try:
        rows = int(input('Min rows 50/ max 5000 \n How many rows: '))
        if rows <= 49 or rows >=5001:
            print('Sorry, your response was less than expeted. Using default value 100.')
            rows = 100
        break
    except ValueError:
        rows = 100
        break
while True:
    try:
        char = int(input('Min characters 2/ max 5 \n How many characters: '))
        if char <= 1 or char >=6:
            print('Sorry, your response was less than expeted. Using default value 3.')
            char = 3
        break
    except ValueError:
        char = 3
        break
while True:
    try:
        cols = int(input('Min columns 5/ max 10 \n How many columns: '))
        if cols <= 4 or cols >= 11:
            print('Sorry, your response was less than expeted. Using default value 3.')
            cols = 10
        break
    except ValueError:
        cols = 10
        break
while True:
    try:
        nums = int(input('Each multiple column is a number column, cant be 0 min 3/max 5 \n Enter the value: '))
    except ValueError:
        print('Try again')
        continue
    if nums <= 2 or nums >=6:
        print('Sorry, your response did not mach. Min value can be 3 and max 5.')
        continue
    else:
        break
dest = str(input('Enter the file name, must write with file type: ') or 'Create-MyCSV.csv') #Asking for a user file name, if we dont enter the value, uses the default
line = 0
line1 = 0
#Function for random strings and integers
def id_generator(size= char, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def nr_generator(size= char, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print(nr_generator())
print(id_generator())
uusa = []
uusa1 = []
nums1 = nums -1

for i in range(rows * cols):
    line += 1
    uusa1.append(id_generator())
    
    if line == cols:
        uusa.append(uusa1)
        line = 0
        uusa1 = []
        
uusa[nums1::nums] = [nr_generator() for x in uusa[nums1::nums]]
print(uusa)

def write_csv_file(filename: dest, data: uusa):
        with open(filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";")
            for row in data:
                csv_writer.writerow(row)
write_csv_file(dest, uusa)
