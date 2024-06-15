import time
import qrcode

# refactoridea - manual calls each input as a separate function, type checking - yep
# refactoridea - Each separate function does it's own type and bounds checking - yep
# refactoridea - manually select bg and fg colors
# refactoridea - add conversion counter using an external file, as a decorator function 
# refactoridea - reverse a qrcode parse qr code into a string and write to cmd or file
# refactoridea - rewrite all in JS (after figuring out tkinter and turning it into an exe)


inputacceptance = '''Input accepted and verified. 
---------------------------'''

def colorvaluechecker(x):
    for i in x:
        if i < 0 or i > 255:
            print("color value out of bounds!")
            return 1
        else:
            return 0

def colorsetter():
    chosencolors = None
    colors = None
    print("here you can select foreground and background colors different from base.")
    print('''A: proceed with default color scheme.
            B: specify foreground and background color.
            [any other]: reloads this section.  ''')
    colorchooser = input("A or B? ").lower()
    match colorchooser:
        case "a": 
            colors = chosencolors
        case "b": 
            colors = coloroptions()
        case _: colorsetter()
    return colors

def foregroundcolor():
    forecolor = ()
    forecolor1 = []
    print("Foreground color values")
    time.sleep(1)
    try:
        foreground = list((input("enter foreground color as RGB values separated by a comma: ")).split(","))
    except: 
        print(f'''{foreground} cannot be cast as a list separated by commas.
              Therefore you made an error in input. 
              This section will reload.''')
        foregroundcolor()

    for i in foreground:
        try:
            i1 = int(i)
            forecolor1.append(i1)
        except:
            print("elements in entered tuple are not numbers as they cannot be cast as ints. Rerun.")
            foregroundcolor()
    
    foreground = tuple(forecolor1)

    if colorvaluechecker(foreground) == 0:
        forecolor = foreground
        print(inputacceptance)
        return forecolor
    else:
        print("This section will run again.")
        foregroundcolor()       

def backgroundcolor():
    backcolor = ()
    backcolor1 = []
    print("Background color values")
    time.sleep(1)
    try:
        background = list((input("enter background color as RGB values separated by a comma: ")).split(","))
    except: 
        print(f'''{background} cannot be cast as a list separated by commas.
              Therefore you made an error in input.
              This section will reload.''')
        backgroundcolor()

    for i in background:
        try:
            i1 = int(i)
            backcolor1.append(i1)
        except:
            print("elements in entered tuple cannot be cast as ints. Rerun.")
            backgroundcolor()
    
    background = tuple(backcolor1)

    if colorvaluechecker(background) == 0:
        backcolor = background
        print(inputacceptance)
        return backcolor
    else:
        print("This section will run again.")
        backgroundcolor()

def coloroptions():
    print("colors are specified by RGB values inserted as a tuple")
    print("for example: '0, 0, 0' is black while '255, 255, 255' is for white")
    print("all other color values for 16,78 million shades fall in between these values")
    time.sleep(2)
    foreground = foregroundcolor()
    background = backgroundcolor()
    colors = foreground, background
    return colors

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
        print(inputacceptance)
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
        print(inputacceptance)
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
        print(inputacceptance)
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
        print(inputacceptance)
        return man_border

def manual_settings():
    print("Enter parameters for manual conversion when prompted.")
    time.sleep(1)
    version = manual_version()
    error_correction = manual_ec()
    box_size = manual_boxsize()
    border = manual_border()
    manual_values = [version, error_correction, box_size, border]
    return manual_values

#asks user to choose automatic and manual conversion settings.
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
    targetfile = None
    if targetdata == "":
        targetfile = input("Enter name of file (with extension) containing target text: ")
    outputname = input("Enter name (w/o extension) of the output file. Can be left blank: ")
    colors = colorsetter()
    if outputname == "":
        outputname = "text_to_qrcode"
    if targetfile != None:
        qr_convert(readfrom_file(targetfile), outputname, conversion_params, linecounter, colors)
    else:
        qr_convert(targetdata, outputname, conversion_params, linecounter, colors)

def batch_to_qr():
    conversion_params = settings_setter()
    targetdata = input("Enter name of the source file with extension: ")
    outputname = input("Enter name (w/o extension) for the the output files. Can be left blank: ")
    colors = colorsetter()
    if outputname == None:
        outputname = "batch_to_qrcode"
    batch_read(targetdata, outputname, conversion_params, colors)
        

def batch_read(filename, *args):
    with open(filename, 'r') as s:
        linecounter = 0
        f = s.readlines()
        for line in f:
            targetstring = line
            linecounter += 1
            outputname = args[0]
            settings = args[1]
            color = args[2]
            qr_convert(targetstring, outputname, settings, linecounter, color)


def readfrom_file(filename):
    with open(filename, 'r') as s:
        targetstring = s.read()
    return targetstring

def qr_convert(data, name, settings, linecounter, colors):
    
    if colors != None:
        basic_back = colors[1]
        basic_fill = colors[0]
    else:
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
        exce_choice = input("Use default parameters? Y/N: ").lower()
        match exce_choice:
            case "y": qr_target.make(**fitmentdict1)
            case _: print("This program will now exit")
    
    img = qr_target.make_image(back_color=basic_back, fill_color=basic_fill)
    
    if linecounter == None:
        img.save(f"{name}.png")
        print(f"qr-code named '{name}.png' saved successfully!")
    else:
        img.save(f"{name}-{linecounter}.png")
        print(f"qr-code named '{name}-{linecounter}.png' saved successfully!")

    # refactoridea - instead of 3 fitmentdicts, just alter one dict
    # refactoridea - pass back and fill color values as dicts
    # refactoridea - what if the sring length exceeds version 40 limit?

if __name__=="__main__":
    outsideframe()