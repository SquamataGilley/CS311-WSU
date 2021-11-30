import gspread
from oauth2client.service_account import ServiceAccountCredentials

    # this is just defining the scope of the spreadsheet, it wont change
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # to use this Package you will have to go through with setting up a google Service account and making a new
    # project and getting a JSON file from it. It is tedious but once it is done, you wonthave to do it again
    # So, without an active JSON file this script will not work. Ill link a page on how to create the afformentioned
    # tools.
    
# https://www.codepoc.io/blog/gcp/5993/how-to-create-service-account-in-google-cloud-and-download-private-key-json-file          

# add the credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name(r'D:\HDD - Desktop\TEST-8f64c21af662.json', scope)

# This just logs in with all the information on the JSON file
client = gspread.authorize(creds)
sheet = client.open('Form Submission')
sheet_instance = sheet.get_worksheet(0)

# this is the most simple of all the packages we use. For instance, were gonna call the information in cell 1,1
    # be mindful, the coordinates are backwards. X goes in the right column and Y goes in the left
def SpreadSheet():
    cellAA = sheet_instance.cell(1,1)
    print(cellAA)
    # this print function will include information we dont want like what cell it is from. we just want the data
    # so we'll do this. it will only get the information in the cell now
    cellAA_Updated = str(cellAA.value)
    print(cellAA_Updated)

    # At my work we need one whole row to be group together, like a family for one iteration. So we use this method
    # so for this spreadsheet we'll assign the row to a stored and called variable. Were still getting the cell 1,1
def NewSpreadSheet():
    row = int(storedRow)
    global newCellAA
    newCellAA = sheet_instance.cell(row , 1)
    newCellAA_Updated = str(newCellAA.value)
    
    # in order to keep track of what row we want to run we use a simple integer storing method
    # this will save the row in case of a crash or error
def saved_row_int():
    # saves the new row value to the .txt file
    Stored_Int_Filename = r'D:\HDD - Desktop\Row_Stored.int'
    f = open(Stored_Int_Filename, "w")
    integer = Row_Scan
    f.write(str(integer))
    f.close()

    # this body of code gets the stored integer from our text file, this is called every time it runs
    # in testing we have to go in and change this number back to 1 so it actually runs when we test again
file_object = open(r'D:\HDD - Desktop\Row_Stored.int', "r")
stored_integer = file_object.read()
storedRow = stored_integer

    # this is a torn down version of our loop used for major automation but it encapsulates functionality
Infinite_Loop = 1
while Infinite_Loop == 1:
    
    # Scans current row to see if any values are present
    Row_Scan = storedRow
    Current_Row_Scan = sheet_instance.cell(Row_Scan , 1)
    Current_Row = str(Current_Row_Scan.value)
 
    # This conditional tests to see if the current row has no values in it, if it doesnt the script stops
    # Logical deduction would lead you to believe that an empty cell has "None" as its value and you would be correct
    if Current_Row == "None":
        saved_row_int()
        print("The script no longer moves down the spreadsheet and saved the row")
        break
    
    # This else section holds all the functions that will run, ive commented out the ones that are not mentioned
        # in this file
    else:
        # I add these print functions a lot throughout the script for debugging, to see where something
            # stopped working
        print("we are on row " + str(starting_int))
        # this is our only callable function and even then it wont run due to us not having an active JSON file
            # but as I mentioned prior, this is all functionable and is a passive script on our Ubuntu based machine
            # on site
        NewSpreadSheet()
        
        # Calls the PDF Maker Function above
        ###PDF_creator()
        
        # Calls the Email function above
        ###Email_Loop()

        # This is where we add one to the row since were done with this one and move on to the next
        starting_int +=1
        saved_row_int()
        print("The clients have been emailed and has saved the current row")

        
