# Email template creator. Takes a csv file with contact information and generates an html file with mailto links for each contact row of csvfile
# Raven Agape

import csv
# Open CSV file to retrieve email list information of email, cc, bcc, customer name, vendor name
print "Mailto link generartor-- takes a csv file and generates an html filel with mailto links"

Cname = raw_input("Customer Name: ")

Fname = raw_input("CSV Filename: ")
g = open(Fname)
csv_progress = csv.reader(g)
#  open file to set up as html document to hold Mailto links
q=Cname+"Mailto.html"
file = open(q, "w")
# Write html header info
file.write("<html>")
file.write("<body>")
file.write("<H3>")
file.write(Cname)
file.write(" Pre-Assessment Emails </h3>")
# Read in each row of csv, parse into Mailto statement format and write out as html mailto link
for nrow in csv_progress:
    zmail=nrow[0]
    zcc=nrow[1]
    zbcc=nrow[2]
    customer=nrow[3]
    vendor=nrow[4]
    cleanvend=nrow[5]
    zcc2=nrow[6] #Modify by customer preference on who gets cc'd
    zcc3=nrow[7]  #Modify by customer preference on who gets cc'd
    file.write("<a href=mailto:")
    file.write(zmail)
    file.write("?cc=")
    file.write(zcc)
    file.write(",")
    file.write(zcc2)
    file.write(",")
    file.write(zcc3)
    file.write("&bcc=")
    file.write(zbcc)
    file.write("&subject=")

    file.write(customer)
    file.write("%20is%20requesting%20a%20cyber%20risk%20assessment%20on%20")
    file.write(vendor)
    file.write("&body=Were%20excited%20to%20continue%20working%20with%20")
    file.write(vendor)
    file.write(".%20%0D%0DAs%20part%20of%20our%20ongoing%20relationship%20we%20would%20like%20to%20get%20a%20more%20thorough%20understanding%20of%20your%20security%20practices%20and%20programs.%20%20With%20that%20said,%20I%20would%20like%20to%20welcome%20you%20to%20the%20")
    file.write(customer)
    file.write("%20Vendor%20Security%20Assessment%20program.%20%20The%20purpose%20of%20this%20program%20is%20to%20minimize%20the%20risk%20posed%20to%20")
    file.write(customer)
    file.write("%20by%20our%20vendors.%20%20%0D%0DThis%20assessment%20is%20completed%20by%20you,%20our%20vendor,%20and%20should%20reflect%20the%20controls%20within%20your%20organization%20and%20any%20subcontractors.%20%0D%0DWhen%20answering%20the%20questions,%20consider%20the%20context%20of%20the%20product%20or%20service%20being%20used%20by%20")
    file.write(customer)
    file.write(".%20A%20control%20which%20is%20in%20place%20in%20")
    file.write("other%20areas%20of%20your%20organization,%20but%20is%20not%20enforced%20for%20the%20product%20or%20service%20used%20by%20us,%20should%20be%20identified%20as%20missing.%20%0D%0DThis520agency%20has%20been%20retained%20to%20perform%20this%20assessment.%20They%20will%20be%20reaching%20out%20to%20you%20directly%20to%20initiate%20the%20process.%20%0D%0DUpon%20completion,%20your%20organization%20will%20be%20able%20to%20share%20this%20assessment%20with%20other%20companies%20if%20future%20assessment%20requests%20are%20received.%20%20We%20are%20hopeful%20this%20will%20save%20your%20organization%20the%20time%20and%20effort%20that%20is%20typically%20required%20to%20fulfill%20multiple%20assessment%20requests.%20%0D%0DThanks,>")
    file.write(cleanvend)
    file.write("</a>")
    file.write("<br><br><br>")
# close out html file
file.write("</body>")

file.write("</html>")

file.close()
