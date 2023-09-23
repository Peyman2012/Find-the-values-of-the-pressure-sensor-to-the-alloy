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
