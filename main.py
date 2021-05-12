import copy
import csv

# something to see how git work
# testing from working copy, using Texastic


# function to clone a list
def cloning(list1):
    list_copy = copy.deepcopy(list1)
    return list_copy


# function to check if scanning is finished
def listcheck():
    check = 0
    for iterator in range(len(temp)):
        if int(check_list[iterator][1]) == int(temp[iterator][1]):
            check += 1
        else:
            break
    if check == len(temp):
        return True
    else:
        return False


# for saving the file's data and comparing
temp = []

# for keeping track with the quantities
check_list = []

# read in and write file
csv_reader = csv.reader(open('testfile.csv', "r"), delimiter=",")
csv_writer = csv.writer(open('result.csv', "w"))

# Copy to a temp file & Copy to check_list
for row in csv_reader:
    temp.append(row)

check_list = cloning(temp)

for x in range(len(check_list)):
    check_list[x][1] = 0

# sorting the lists (for comparing)

# Search the list until 'q'
choice = ''
while choice != 'q':
    if listcheck():
        print("\n-----LIST IS FULL. STOP SCANNING-----")
        choice = 'q'
    else:
        upc_search = input("\nScan a upc ('q' to quit):")
        i = 0
        for row in temp:
            if upc_search.isnumeric() is not True:
                choice = upc_search
                if choice != 'q':

                    print(f"\n{choice} is not a UPC ('q' to quit). ")
                    break
                else:
                    break
            elif int(row[0]) == int(upc_search):
                choice = upc_search
                if int(check_list[i][1]) < int(row[1]):
                    check_list[i][1] += 1
                    print(f'Scanned {upc_search} successfully')
                    print(f"Current {upc_search}'s quantities: {check_list[i][1]}")
                else:
                    print(f'MAXIMUM QUANTITY REACHED')
                break
            else:
                i += 1
                continue
        else:
            print("Not Found")
        # for loop
# while loop

if listcheck() is False:
    print("\nFinished Scanning")
    print("There are missing item(s). Check output csv file for more information.")
csv_writer.writerows(check_list)
