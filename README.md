
UML sequence diagram:
![UML](https://github.com/user-attachments/assets/d2f7bb42-8824-4668-9268-0fcf83eeeec1)

This program reads instructions and data from a text file then returns sorted data  
-the text files can be set in the main function 

How to send(input) and receive(output) data:

Input:  
-send a request through the request file   
-open request file  
-write f"{sort_type}\n" sort_type is 1, 2 or 3 for sorting by date, priority or both  
-the \n character is required to seperate sort type and data  
-write json.dumps(data) where data is a list containing task dicts to be sorted  
Example of txt file contents during a request:  

1  
[
{“name”: “walk dog”, “Priority”: “High”, “Date”: “05-27-2025”}, 
{“name”: “water plants”, “Priority”: “Medium”, “Date”: “05-20-2025”}
]

Output:  

-set a short timer to ensure sorting operation has time to complete  
-open response file and read the sorted data within  
-use json.loads(data) to convert the sorted data back to a python list of task dicts  
-open the file again and pass to empty contents so the function will run cleanly  
Example of txt file contents during a response:  

[
{“name”: “water plants”, “Priority”: “Medium”, “Date”: “05-20-2025”},
{“name”: “walk dog”, “Priority”: “High”, “Date”: “05-27-2025”} 
]


Requirements:  

-task dicts need to have the keys "Prority" and "Date" so the values can be accessed for sorting  
-change key names by changing "Date" in date_sort and "Priority" in priority_sort  
-dates must be in MM-DD-YYYY format so 5/3/2025 is 05-03-2025  
-the leading zero for single digit values is required for sorting   
