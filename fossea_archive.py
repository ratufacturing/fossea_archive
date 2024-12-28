import lbrytools as lbryt
import hashlib
import time
import re
import os
import pyexcel as pe
import argparse

def main():
    #CLI Arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument("-blc", "--use_blc_script", help="Option to automatically import and use the BLC Odysee spreadsheet into the list of channels to download. Defaults to True if passed.", type=str_to_bool, nargs='?', const=True, default=None)
    parser.add_argument("-ddir", "--download_directory", help="Set the download directory for completed files", type=str)
    parser.add_argument("-supp", "--secondary_file", help="Option to automatically import and use the a secondary txt or similar file into the list of channels to download. Pass 'none' to avoid use.", type=str)
    parser.add_argument("-novid", "--skip_video_files", help="Avoid downloading unzipped video files to save space. Defaults to True if passed.", type=str_to_bool, nargs='?', const=True, default=None)
    args = parser.parse_args()
    text = '0'

    #Download path selection and BLC list import
    while True:
        try:
            if args.download_directory:
                ddir = args.download_directory
            else:
                ddir = input("Enter the absolute path to the download directory: ") 
                #Check for valid input
                if ddir == "" or not os.path.isdir(ddir):
                    continue
            
            if args.use_blc_script is not None:
                if args.use_blc_script is True:
                    useBLC = "y" #This is a little hacky but works fine
                else:
                    useBLC = "false"
            else:
                useBLC = input("Import the BLC Guncad list? ")

            if useBLC.lower() in ['y', 'yes', 'true']:
                
                #Download the current file and read in the text to the chosen directory
                sourceODS = lbryt.download_single(uri="@blacklotuscoalition:3/The-New-Odysee-List-Spreadsheet", ddir=ddir)
                
                #Use pyexcel to get the data from the ods sheet
                odsBook = pe.get_book(file_name=sourceODS["download_path"])

                #Iterate through the sheets, rows, and cells in the ods doc
                for sheet in odsBook:
                    for row in sheet.to_array():
                        for cell in row:
                            #Check if there's a channel name in the cell we're looking at- if we added all the text, the string gets too big and causes a crash
                            if re.match(r".+.", str(cell)):
                                text += str(cell)
                                text += ";" #Lazy way to delineate channels since it causes the regex later to stop matching
                break
            else:
                print("Did not import the BLC list.")
                break
        except KeyboardInterrupt:
            return
        except:
            print("Error, please try again:")
            continue

    #Supplementary file selection and loading
    while True:
        try:
            if args.secondary_file:
                if args.secondary_file.lower() not in ['f', 'false', 'no', 'none', 'n']:
                    suppFile = args.secondary_file
                    text = text + open(suppFile,'r').read()
                    print('File imported:' + suppFile)
                else:
                    print("No secondary file chosen.")
            else:
                useSupp = input("Use a second file? ")
                if useSupp.lower() in ['y', 'yes', 'true']:
                    suppFile = input("Enter the absolute path to the supplementary file: ")
                    text = text + open(suppFile,'r').read()
                    print('File imported:' + suppFile)
                else:
                    print("No secondary file chosen.")
            
            if text == "0":
                print("No inputs given, closing...")
                return

            if args.skip_video_files is not None:
                if args.skip_video_files is True:
                    skipVideo = "y"
                else:
                    skipVideo = "n"
            else:
                skipVideo = input("Skip downloading video files? ")
            
            if skipVideo.lower() in ['y', 'yes', 'true']:
                downloadVideos = False
                print("Skipping downloading video files.")
            else:
                downloadVideos = True
                print("Downloading video files.")
            break
        except KeyboardInterrupt:
            return
        except:
            print("Error, please try again:")
            continue

    #Extract all matching channel names from the text string
    channels = re.findall(r"(@[^\\;/]+)", text)

    #Clean  channel list
    for i in channels:
        #Clean junk
        if "\\" in i or "https" in i or "dropdown" in i or "@Anon" in i or "@Me" in i:
            channels.remove(i)
        
        #Clean duplicates, using only the newest version (hopefully)
        else:
            for j in channels:
                if re.match(i + ":.+", j):
                    channels.remove(j)
    channels = sorted(set(channels))

    ###Download claims (actual work happens below \/)
    #Iterate through each channel
    for i in channels:
        print(f"Now downloading channel: {str(i)} \n")
        
        #Find all claims of the channel
        claimIds = []

        #Get the channel's claims
        try:
            channelClaims = lbryt.list_ch_claims(i, claim_id=True, title=True)
        except:
            print("Error loading channel claims, skipping...")
            continue
        
        for i in channelClaims['claims']:
            try:
                #If it's a repost, ignore 
                if i['value_type'] != 'repost':
    
                    if downloadVideos == True:
                        claimIds.append(i["claim_id"])
                    elif downloadVideos == False:
                        if i['value']['stream_type'] != 'video':
                            claimIds.append(i["claim_id"])
                            
            except KeyboardInterrupt:
                return
            except:
                print("Error loading claims, skipping...")
                continue                

        #Iterate through each claim we've chosen to download, and pass them to the lbrynet daemon
        for i in claimIds:
            try:
                lbryt.download_single(cid=i, ddir=ddir, own_dir=True)
            except KeyboardInterrupt:
                return
            except:
                pass

#This bit was added to help with CLI arguement parsing
def str_to_bool(value):
    #Convert string to boolean.
    if value.lower() in ('true', '1', 'y', 'yes'):
        return True
    elif value.lower() in ('false', '0', 'n', 'no'):
        return False
    else:
        raise argparse.ArgumentTypeError(f"Invalid boolean value: {value}. Use 'true' or 'false'.")

if __name__ == "__main__":
    main()
