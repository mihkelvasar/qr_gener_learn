import time
import qrcode

# refactoridea - manual calls each input as a separate function, type checking - yep
# refactoridea - Each separate function does it's own type and bounds checking - yep
# refactoridea - extend inputs parameter saving to all options of the package,
# including orientation, background and foreground image etc.
# refactoridea - add conversion counter using an external file, as a decorator function 

def int_checker(x):
    try:
        y = int(x)
        return y
    except:
        y = None
        return y
        
def manual_version():
    versiondata = input("Enter desired qr-code version between 1 and 40: ")
    versiondata1 = int_checker(versiondata)
    if versiondata1 == None:
        print("Error: input must be an integer! This function will reload")
        manual_version()
    elif versiondata1 < 1 or versiondata1 > 40:
        print("Error! Entered version out of bounds")
        pivot = input("Retry or Proceed with default settings? R/P: ").lower()
        match pivot:
            case "p": 
                versiondata = None
                print("Proceeding with default QR-code version")
                print("---------------------------------------")
                return versiondata
            case _: manual_version()
    else:
        print("input accepted and verified")
        print("---------------------------")
        return versiondata

def manual_ec():
    print("Enter desired Error Correction level in range from 0 to 3.")
    print("1 for level L. Up to 7% of errors can be corrected.")
    print("0 for level M. Up to 15% of errors can be corrected.")
    print("3 for level Q. Up to 25% of errors can be corrected.")
    print("2 for level H. Up to 30% of errors can be corrected.")
    ec_level = input("Enter desired level of Error Correction: ")
    ec_level1 = int_checker(ec_level)
    if ec_level1 == None:
        print("Error: input must be an integer! This function will reload")
        manual_ec()
    elif ec_level1 < 0 or ec_level1 > 3:
        print("Chosen Error correction level out of bounds")
        pivot = input("Retry or Proceed with default settings? R/P: ").lower()
        match pivot:
            case "p": 
                ec_level = 0
                print("Proceeding with default Error Correction level")
                print("---------------------------------------")
                return ec_level
            case _: manual_ec()
    else:
        print("input accepted and verified")
        print("---------------------------")
        return  ec_level

def manual_boxsize():
    print("Enter desired pixel size for the dots/pixels in the code.")
    man_box_size = input("Enter desired pixel size as integer: ")
    man_box_size1 = int_checker(man_box_size)
    if man_box_size1 == None:
        print("Error: input must be an integer! This function will reload")
        manual_boxsize()
    if man_box_size1 < 1:
        print("box size cannot be lower than 1")
        pivot = input("Retry or Proceed with default settings? R/P: ").lower()
        match pivot:
            case "p": 
                man_box_size = 10
                print("Proceeding with default box size")
                print("---------------------------------------")
                return man_box_size
            case _: manual_boxsize()
    else:
        print("input accepted and verified")
        print("---------------------------")
        return man_box_size

def manual_border():
    print("Enter desired border size in box sizes for the code image. Default is 4.")
    print("Example: in previous step you set the box size as 2, thus the width of the border will be multiplied by 2.")
    man_border = input("Enter desired border size as integer: ")
    man_border1 = int_checker(man_border)
    if man_border1 == None:
        print("Error: input must be an integer! This function will reload")
        manual_border()
    elif man_border1 < 0:
        print("border width cannot be lower than 0")
        pivot = input("Retry or Proceed with default settings? R/P: ").lower()
        match pivot:
            case "p": 
                man_border = 4
                print("Proceeding with default border size")
                print("---------------------------------------")
                return man_border
            case _: manual_border()
    else:
        print("input accepted and verified")
        print("---------------------------")
        return man_border

# problem - input is accepted as string and during execution interpreted as an int
# problem - adding typechecking for input variable is pointless, because it is a str
# problem - casting input as int is a problem because any other datatype will crash
# solution - try/except?
# problem - wall of text, add blank/dashed lines

def manual_settings():
    print("Enter parameters for manual conversion when prompted.")
    time.sleep(1)
    version = manual_version()
    error_correction = manual_ec()
    box_size = manual_boxsize()
    border = manual_border()
    manual_values = [version, error_correction, box_size, border]
    return manual_values
    # check for data type of elements in manual_values, are they still str?
    # does interpeting as int take place at dict(zip(x,y))?

#asks user to choose automatic and manual conversion settings. returns settings to global as a dict
# refactoridea - remove the unnecessary dict(zip(x)) for default_settings
def settings_setter():
    default_keys = ["version", "error_correction", "box_size", "border"]
    default_values = [None, 0, 10, 4]
    default_settings = dict(zip(default_keys, default_values))
    settings = None
    settings_choice = input("Manual or Automatic settings? M/A: ").lower()
    match settings_choice:
        case "a": 
            settings = default_settings
        case "m": 
            manual_values = manual_settings()
            settings = dict(zip(default_keys, manual_values))
        case _:
            print("no such option. try again.")
            settings_setter()
    return settings

# main menu
def outsideframe(): #This Works
    print("Welcome to Mike's QR Code converter.")
    time.sleep(1)
    print("These are your options for QR-code generations:")
    print("A: create QR code from text entered into cmd or in a text file.")
    print("B: batch processing, a list of links in a text file.")
    print("Q: quit program.")
    decider = input("A B or Q?   ").lower()
    match decider:
        case "a":
            text_to_qr()
        case "b":
            batch_to_qr()
        case "q":
            print("This program will now exit")
        case _:
            badchoice()
            outsideframe()

#in case of unlisted choice in main menu, a Married With Children joke
def badchoice(): #This Works
    print("Invalid response.The code will run again")
    time.sleep(2)
    print(""" "Welcome to Herb's World of Junk!" """)
    time.sleep(2)
    print(""" "If you'd like these instructions in Spanish, press 1" """)
    time.sleep(3)

def text_to_qr():
    linecounter = None
    conversion_params = settings_setter()
    targetdata = input("Enter string to be converted (or leave blank for text file prompt): ")
    if targetdata == "":
        targetfile = input("Enter name of file (with extension) containing target text: ")
    outputname = input("Enter name (w/o extension) of the output file. Can be left blank: ")
    if outputname == "":
        outputname = "text_to_qrcode"
    if targetfile != None:
        qr_convert(readfrom_file(targetfile), outputname, conversion_params, linecounter)
    else:
        qr_convert(targetdata, outputname, conversion_params, linecounter)

def batch_to_qr():
    conversion_params = settings_setter()
    targetdata = input("Enter name of the source file with extension: ")
    outputname = input("Enter name (w/o extension) for the the output files. Can be left blank: ")
    if outputname == None:
        outputname = "batch_to_qrcode"
    batch_read(targetdata, outputname, conversion_params)
        

def batch_read(filename, *args):
    with open(filename, 'r') as s:
        linecounter = 0
        f = s.readlines()
        for line in f:
            targetstring = line
            linecounter += 1
            outputname = args[0]
            settings = args[1]
            qr_convert(targetstring, outputname, settings, linecounter)


def readfrom_file(filename):
    with open(filename, 'r') as s:
        targetstring = s.read()
    return targetstring

def qr_convert(data, name, settings, linecounter):
    basic_back = (255, 195, 235)
    basic_fill = (55, 95, 35)

    fitmentdict0 = {"fit": False}
    fitmentdict1 = {"fit": True}

    if settings["version"] == None:
        fitmentdictn = fitmentdict1
    else:
        fitmentdictn = fitmentdict0

    qr_target = qrcode.QRCode(**settings)
    qr_target.add_data(data)

    try:
        qr_target.make(**fitmentdictn)
    except:
        print("Error: Chosen QR-code version incompatible with size of target data.")
        exce_choice = input("Use default parameters? Y/N").lower()
        match exce_choice:
            case "y": qr_target.make(**fitmentdict1)
            case _: print("This program will now exit")
    

    img = qr_target.make_image(back_color=basic_back, fill_color=basic_fill)
    
    if linecounter == None:
        img.save(f"{name}.png")
    else:
        img.save(f"{name}-{linecounter}.png")

    # refactoridea - instead of 3 fitmentdicts, just alter one dict
    # refactoridea - pass back and fill color values as dicts

if __name__=="__main__":
    outsideframe()