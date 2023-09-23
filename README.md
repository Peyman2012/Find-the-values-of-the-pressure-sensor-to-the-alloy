# Find-the-values-of-the-pressure-sensor-to-the-alloy

**What is CSV?** 
CSV (Comma Separated Values) is a simple file format used to store tabular data, such as a spreadsheet or database. A CSV file stores tabular data (numbers and text) in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format.
For working CSV files in Python, there is an inbuilt module called csv. 

**Working with CSV files in Python**
Below are some operations that we perform while working with CSV files in Python

**Reading a CSV file**
Writing to a CSV file
Writing a dictionary to a CSV file
Storing email in CSV file

**Reading a CSV file**
Reading from a CSV file is done using the reader object. The CSV file is opened as a text file with Python’s built-in open() function, which returns a file object. In this example, we first open the CSV file in READ mode, file object is converted to csv.reader object and further operation takes place. Code and detailed explanation is given below.

    import csv

Here, we first open the CSV file in READ mode. The file object is named as 'f'. The file object is converted to csv.reader object. We save the csv.reader object as 'reader':

    with open('C:/Users/peyman/pythonProject17/sense.csv','r') as f:
    p=[]
    t=[]
    reader=csv.reader(f)


Now, we iterate through the remaining rows using a for loop. Each row is appended to a list called rows. If you try to print each row, one can find that a row is nothing but a list containing all the field values:

     for row in reader:
            t.append(row[0])
            p.append(row[1])
     for p in p[1:]:
            power.append(p)
     for t in t[1:]:
            time.append(t)


If the pressure on the alloy is between 0.35 and 0.85, the alloy will be damaged and broken:

     for i in range(len(power)):
         if float(power[i])>=0.35 and float(power[i])<=0.85:
             print(f'Time : {time[i]} s and Power : {power[i]} result :  This power is dangerous!!!!!!!!!')
         else:
             print(f'Time : {time[i]} s and Power : {power[i]} result : Power is good')
