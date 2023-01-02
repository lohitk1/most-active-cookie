# Most Active Cookie Project
Python code to find the most active cookie on a specific date in a cookie log file

## Problem Specifications

Given a cookie log file in the following format:
~~~
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
~~~
Write a command line program in your preferred language to process the log file and return the most active cookie for specified day. The example below shows how we'll execute your program.\
**Command:**
~~~
$ ./most_active_cookie cookie_log.csv -d 2018-12-09
~~~
**Output:**
~~~
AtY0laUfhglK3lC7
~~~
We define the most active cookie as one seen in the log the most times during a given day.\
**Assumptions:**\
● If multiple cookies meet that criteria, please return all of them on separate lines. \
**Command:**
~~~
$./most_active_cookie cookie_log.csv -d 2018-12-08
~~~
**Output:**
~~~
SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG
~~~
● You're only allowed to use additional libraries for testing, logging and cli-parsing. There are libraries for most languages which make this too easy (e.g pandas) and we’d like you to show off you coding skills.\
● You can assume -d parameter takes date in UTC time zone.\
● You have enough memory to store the contents of the whole file.\
● Cookies in the log file are sorted by timestamp (most recent occurrence is first line of the file).

## Build Executable
### Option 1 - Pybuilder Build
 - Make sure you have cloned the main branch
 - Install python3 on your system
 - Make sure you pip install pybuilder. Run command:
 ~~~
 pip install pybuilder
 ~~~
 - Publish project, run test files and create executable file using Pybuilder. Run command:
 ~~~
 pyb
 ~~~
  - The executable file should now be created in the root directory, which is the most-active-cookie directory. This usually takes some time.

**ALTERNATIVE APPROACH**
 - To save time and just create the executable file, first install pyinstaller. Run command:
 ~~~
 pip install pyinstaller
 ~~~
 - To create executable, run command:
 ~~~
 pyinstaller --name=most_active_cookie --onefile --distpath=./ --clean ./src/main/most_active_cookie.py
 ~~~

 ### Option 2 - Make Build
 - This is another approach to build the executable file
 - Install python3 on your system
 - Make sure you have cloned the make-build-system branch
 - Run command:
 ~~~
 make
 ~~~
  - This should install all dependencies, run unit tests and create executable file

## Run Executable
  - To run the executable, run command:
~~~
./most-active-cookie csv_file_name -d date-to-search
~~~
 - Example of this command:
~~~
./most_active_cookie cookie_log.csv -d 2018-12-08
~~~

## Explanation of Project Structure
 - The entire project was written in python3
 - The main function along with the command line parsing is included in the src/main/most_active_cookie.py file
 - The validation functions (all the error/exception handling functions) are located in the src/main/utils/validations.py file
  - The output/display functions are located in the src/main/utils/displays.py file
  - The actual calculation functions are found in the src/main/utils/calculations.py file
  - The unit tests for all the source files are located in the src/unittest folder
  - The cookie_logs are located in the src/logs folder

## Explanation of Project Calculations
 - Step 1: The command line arguments (cookie log's file name and date to search) are parsed with all the exception handling for the command line arguments taken care of by the argparse module and all the exception handling related to csv file validation and date to search validation taken care of by related functions.
 - Step 2: A dictionary/hashmap is created with the cookie strings and their corresponding frequencies that occur on the given date to search. Simultaneously the csv file's contents are validated.
 - Step 3: A list containing the most active cookies on the given date to search for is created from the dictionary that is created in the previous step.
 - Step 4: The contents of the list are sequentially printed out.
