Multi-Paradigm Programming

GMIT Autumn/Winter Assignment
-----------------------------

////////
The Shop
////////

-----------------------------

Introduction
------------
The brief was to create a shop simulation demonstrating an understanding of both 'Procedural' and 'Object-Orientated' programming. The initial development of the programs was carried out in lectures with Dr. Dominic Carr after which we were requested to add additional functionality and bring the programs to completion. The Procedural approach was to be completed in both the `c` and `Python` programming languages while we had a choice for the object-orientated version between `Java` and `Python`.

-----------------------------

Contents of repositry
---------------------
The repositry contains the following:
* c - folder containing files in c programming language
    * shop.c - shop application in c (Procedural Programming)
* python - folder containing files in python programming language
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

-----------------------------

Installation and running
------------------------
Full details on running the applictions can be found in the report.pdf document, but the following is a quick start guide:

The `c` program needs compiling before running. The following command will compile the file:

gcc -g shop.c -o out

To run the program we can then use the following:

./out

The `Python` files require a python environment and the appropriate packages imported. The easiest way to do this is with `Anaconda` which is available from here - https://docs.anaconda.com/anaconda/install/. Alternatively you can install the latest version of python manually and import the packages listed in the requirements.txt file.
The programs can then be run from Terminal (or the command line) by simply typing `python` followed by the filename.

-----------------------------

Credits
-------
The bulk of the project came from lecture with Dr. Dominic Carr. Further online research provided solutions to individual problems and issues along the way. A list of specific online resources can be found at the end of the report.

-----------------------------

Contact
-------
caoimhinvallely@gmail.com




