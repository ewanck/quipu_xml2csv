Step one is to install the relevant libraries on your computer. You only have to do this the very first time you use these scripts then you can skip ahead to the conversion section below. 

Copy and paste the following commands into your terminal window (not including the $ -this represents a new line in terminal) Press enter after each command and give your computer password when prompted.


$ wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python

$ sudo easy_install pip

$ sudo pip install lxml


Conversion

-To convert an .xml file you first need to make sure the file is in this folder beside the .py script. 
-Then you need to open the settings.txt file using Text Edit or any other plain text editor (not Word!) 
-Change the filename here to the one you want to convert. At the moment you can only convert one file at a time.
-Make sure the whole folder is stored in your desktop and then copy/paste the following commands into a terminal window, pressing enter after each one.

$ cd Desktop/xml_converter
 
$ python xml2csv.py

-You should now find a new csv file in the csv folder.
-If there are any errors please copy and paste the error text and send in an email to me so I can see what went wrong.
