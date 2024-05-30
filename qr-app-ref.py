import time
import qrcode

# refactor - manual calls each input as a sepatate function. 
# refactor - Each separate function does it's own type and bounds checking
# refactor - extend inputs parameter saving to all options of the package,
# including orientation, background and foreground image etc.
def manual_settings():
    print("Enter parameters for manual conversion when prompted.")
    time.sleep(1)
    version = input("Enter desired qr-code version between 1 and 40:" )
    error_correction = input("Enter desired error correction level between 0 and 3 (inclusive): ")
    box_size = input("Enter desired 'pixel' size in pixels: ")
    border = input("Enter desired border size (in multiples of 'pixel' size): ")
    manual_values = [version, error_correction, box_size, border]
    return manual_values

#asks user to choose automatic and manual conversion settings. returns settings to global as a dict
# refactor - remove the unnecessary dict(zip(x)) for default_settings
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

#in case of unlisted choice, it gives you an Married With Children joke
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
        targetfile = input("Enter name of file containing target text: ")
    outputname = input("Enter filename of the output file. Can be lefct blank: ")
    if outputname == "":
        outputname = "text_to_qrcode"
    if targetfile != None:
        qr_convert(readfrom_file(targetfile), outputname, conversion_params, linecounter)
    else:
        qr_convert(targetdata, outputname, conversion_params, linecounter)


def batch_to_qr():
    conversion_params = settings_setter()
    targetdata = input("Enter name of the source file with extension: ")
    outputname = input("Enter name for the the output files. Can be left blank: ")
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
    qr_target.make(**fitmentdictn)
    

    img = qr_target.make_image(back_color=basic_back, fill_color=basic_fill)
    
    if linecounter == None:
        img.save(f"{name}.png")
    else:
        img.save(f"{name}-{linecounter}.png")

if __name__=="__main__":
    outsideframe()