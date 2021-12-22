--------------------------------
** Multi-Paradigm Programming **

  GMIT Autumn/Winter Assignment
--------------------------------

\\\\\\\\
////////
THE SHOP
\\\\\\\\
////////

------------
Introduction
------------
The brief was to create a shop simulation demonstrating an understanding of both 'Procedural' and 'Object-Orientated' programming. The initial development of the programs was carried out in lectures with Dr. Dominic Carr after which we were requested to add additional functionality and bring the programs to completion. The Procedural approach was to be completed in both the `C` and `Python` programming languages while we had a choice for the object-orientated version between `Java` and `Python`.


---------------------
Github repositry
---------------------
All of the code along with a full commit history is available at https://github.com/Caoimhinv/Multi-Paradigm-Assignment

The repositry contains the following:
* c - folder containing files in C programming language:
    * shop.c - shop application in C (Procedural Programming)
* python - folder containing files in python programming language:
    * shop.py - shop application in python (Procedural Programming)
    * shopOOP.py - shop application in python (Object-Orientated Programming)
* .DS_Store - file that stores custom attributes of the containing folder
* .gitignore - list of files for git to ignore
* customer1.csv - file from which to read in customer name, budget, and shopping list
* customer2.csv - file from which to read in customer name, budget, and shopping list
* customer3.csv - file from which to read in customer name, budget, and shopping list
* readme.txt - this document
* report.pdf - report on the assignment and my findings
* stock.csv - file from which to read in shop float and shop stock

------------------------
Installation and running
------------------------
Full details on the functionality of the applications can be found in the report.pdf document, but the following is a quick start guide for compiling and running:

The `C` program needs compiling before running. Navigate to the appropriate folder in Terminal (or whatever command line interface you are using), and type in the following code to compile the file:

gcc -g shop.c -o out

To run the program we can then use the following:

./out

The `Python` files require a python environment and the appropriate packages imported. The easiest way to do this is with `Anaconda` which is available from here - https://docs.anaconda.com/anaconda/install/. Alternatively you can install the latest version of python manually from https://www.python.org/downloads/.
The programs can then be run from Terminal by typing `python` followed by the filename as follows:

python shop.py

You can then follow the onscreen prompts.

-------
Credits
-------
The bulk of the project came from lecture with Dr. Dominic Carr. Further online research provided solutions to individual problems and issues along the way. A list of specific online resources can be found at the end of the report.

-------
Contact
-------
caoimhinvallely@gmail.com




