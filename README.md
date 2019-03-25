# Mailto-Mail-Merge
Generates HTML file with Mailto links based on customized body text and addresses from a file
Mailto Script Readme File


This script takes in a CSV file of contact data between customer and third party. It outputs a formatted HTML file with Mailto hyperlinks. These links contain text-based mail merge emails with inserted names, and completed cc, and bcc fields based on the CSV file. Here are the steps to implement this.

1) Create the CSV from the “VendorList” template where:
•	Column A: Vendor (3rd Party) Contact Email
•	Column B: Customer Business Contact Email
•	Column C: Customer Success Representative Contact Email
•	Column D: Customer Name with any spaces in name replaced with %20
•	Column E: Vendor Name with any spaces replaced with %20
•	Column F: Vendor Name (with spaces if it is in name)
•	Column G: Additional CC
•	Column H: Additional CC

2) Run script 
•	Open a terminal window from “Applications>Utilities on your mac laptop.
•	Make a directory by typing mkdir mailto 
•	Open a finder window and copy the mailto.py file and your csv into the mailto directory you created

•	Run the script by typing python mailto.py
•	Use customer name and CSV file name as inputs when asked. i.e. “MyCompany” and VendorList.CSV. 
•	The script will output a file of the format CUSTOMERNAMEmailto.html

3) Spot check file by opening file from Chrome and clicking on a mailto link. If you have a mail client enabled on your computer the link should open it and display a ready to send email with everything filled out.

4) Email customer with the html file attached and explain they simply need to click on a link then click “send” from within their mail program.

