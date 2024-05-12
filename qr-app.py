
import qrcode
import qrcode.constants
import time

basic_back = (255, 195, 235)
basic_fill = (55, 95, 35)

def outsideframe(): #This Works
    print("Welcome to Mike's QR Code converter.")
    time.sleep(1)
    print("These are your options for QR-code generations:")
    print("A: let the app decide. M: choose settings. B: batch processing. Q: terminate program")
    decider = input("A M B or Q?   ").lower()
    match decider:
        case "a":
            baseqr_code()
        case "m":
            manual_qr_creation()
        case "b":
            batch_qr_creation()
        case "q":
            print("This program will now exit")
        case _:
            badchoice()
            outsideframe()

def badchoice(): #This Works
    print("Invalid response.The code will run again")
    time.sleep(2)
    print(""" "Welcome to Herb's World of Junk!" """)
    time.sleep(2)
    print(""" "If you'd like these instructions in Spanish, press 1" """)
    time.sleep(3)

def baseqr_code(): #This works
    targetstring = input("Enter string to be converted: ")
    

    basic_qr = qrcode.QRCode(
        version=None, 
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    basic_qr.add_data(targetstring)
    basic_qr.make(fit=True)

    img = basic_qr.make_image(back_color=basic_back, fill_color=basic_fill)
    filename = input("Enter filename without extension. Enter space for defaultname: ")
    
    if filename == " ":
        filename = "stringtoqr"
    
    img.save(f"{filename}.png")

    print(f"image named {filename} saved to working directory")

def batch_qr_conv(x, y, z):
    basic_qr = qrcode.QRCode(
        version=None, 
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    basic_qr.add_data(x)
    basic_qr.make(fit=True)

    filecounter = y
    filename = z
    img = basic_qr.make_image(back_color=basic_back, fill_color=basic_fill)
    img.save(f"{filename}-{filecounter}.png")


def batch_qr_creation(): 
    sourcefile = input("Enter name of source file:  ")
    filename = input("Enter filename without extension. Enter space for defaultname: ")
    if filename == " ":
        filename = "stringtoqr"

    with open(sourcefile, 'r') as s:
        linecounter = 0
        f = s.readlines()
        for line in f:
            targetstring = line
            linecounter += 1
            batch_qr_conv(targetstring, linecounter, filename)


#Manual conversion process
def manual_qr_code(settings):
    targetstring = input("Enter string to be converted: ")
    fitmentdict0 = {"fit": False}
    fitmentdict1 = {"fit": True}
    fitmentdictn = None

    if "version" in settings == None:
        fitmentdictn = fitmentdict1
    else:
        fitmentdictn = fitmentdict0

    manual_qr = qrcode.QRCode(**settings)
    manual_qr.add_data(targetstring)
    manual_qr.make(**fitmentdictn)

    img = manual_qr.make_image(back_color=basic_back, fill_color=basic_fill)
    filename = input("Enter filename without extension. Enter space for defaultname: ")
    
    if filename == " ":
        filename = "stringtoqr"
    
    img.save(f"{filename}.png")

    print(f"image {filename} saved to working directory")

#Manual conversion settings
def manual_qr_creation():
    print("This is for advanced users")
    print("in case of error in parameter, the code will use a default parameter")
    print("Versions: 1-40. Error correction: M, L, Q or S. Pixel Size: >=1. Border: >=4.")
    paramvalues = list(input("Insert parameters separated by a space: ").split(" "))
    paramkeys = ["version", "error_correction", "box_size", "border", ]

    paramvalues[0] = int(paramvalues[0])
    paramvalues[2] = int(paramvalues[2])
    paramvalues[3] = int(paramvalues[3])

    if paramvalues[0] < 1 or paramvalues[0] > 40:
        paramvalues[0] = None
    
    paramvalues[1] = paramvalues[1].upper()

    match paramvalues[1]:
        case "L": paramvalues[1] = 1 
        case "M": paramvalues[1] = 0
        case "Q": paramvalues[1] = 2 
        case "S": paramvalues[1] = 3
        case _ : paramvalues[1] = 0
    
    if paramvalues[2] < 1:
        paramvalues[2] = 1

    if paramvalues[3] < 4:
        paramvalues[3] = 4

    paramdict = dict(zip(paramkeys, paramvalues))
    manual_qr_code(paramdict)
#What error does the package produce when version too little for targetstring

#Refactor for single qrcode function which takes *args, **kwargs


if __name__=="__main__":
    outsideframe()

#Refactoring list
# One single qr_creation function which takes *args and **kwargs
# conditional assignments with the ternary operator
# main menu from match case to response:fn dictionary
# eliminate useless reassignments
# remove illogical argument names 
# in batch processing, read 5 at a time into a cache and then convert, timeit both solutions