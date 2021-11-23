import fpdf

# Just some user inputs to assign the font and size
uFont = str(input('What font would you like? (Courier, Helvetica, Times) '))
uSize = int(input('What font size would you like? (1-99) '))
# defining a function to call our PDF creator
def PDF_Creator():
    # Setting Up the PDF format
    pdf = fpdf.FPDF(format = 'letter', unit = 'pt')
    pdf.add_page()
    pdf_style = 'B'
    pdf.set_font(uFont, size = uSize)

    # To first set up a text box you have to give it coordinates, in points (ex: (100, 100))
    
    pdf.set_xy(72, 72)
    # Starting first text box, there are a few types of text boxes but the one I
    # Use most is multi_cell which allows for line breaks
        # The first parameter is the width, I use 0 so it will stop at the margin
        # The second parameter is height, Ill just be using the users font size + 1
        # The third is the text that is placed, here will be a quick exerpt from my favorite movie, First Blood
    first_blood = 'Rambo : They drew first blood, not me.\nTrautman : Look Johnny, let me come in and get you the hell out of there!\nRambo : They drew first blood...'
    pdf.multi_cell(0, (uSize + 1), txt = first_blood)

    # Next is a basic line drawing function, just give it coordinates and itll draw a line
        # the first and second parameters are x1 and y1
        # the third and fourth parameters are x2 and y2
    pdf.line(65, 125, 400, 125)

    # Here are some shape drawing functions as well
        # here is an ellipse, first and second parameters are the starting X and Y
        # third and fourth parameters are the width and height and the fifth is the style of the ellipse and this one is filled
    pdf.ellipse(72, 175, 250, 100, style = 'F')
        # here is a rectangle, first and second parameters are the starting X and Y
        # third and fourth parameters are the width and height and the fifth is the style of the rectangle and this one is filled
    pdf.rect(72, 300, 250, 100, style = 'F')

    # Here I will drop a .png onto the pdf as well
    troll_path = r'D:\HDD - Desktop\troll.png'
        # the first and last parameters are just the file path
        # the second and third parameters are the starting X and Y
    pdf.image(troll_path, 72, 450, link = troll_path )
    
    # Simply outputs to your desktop a pdf of the information 
    pdf.output(r'D:\HDD - Desktop\FirstBlood.pdf')
    pdf.close()
    
# Calls the previously defined function
PDF_Creator()
    
    
