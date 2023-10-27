import lbrytools as lbryt
import hashlib
import time
import fitz
import re
import os

def main():
    text = "0"
    
    #Download path selection and BLC list import
    while True:
        try:
            ddir = input("Enter the absolute path to the download directory: ") 
            #Check for valid input
            if ddir == "" or not os.path.isdir(ddir):
                continue

            useBLC = input("Import the BLC Guncad list? ")
            if useBLC == "y" or useBLC == "Y" or useBLC == "yes" or useBLC == "Yes":
                #Download the current file and read in the text to the chosen directory
                sourcePDF = lbryt.download_single(uri="@blacklotuscoalition:3/Odysee-list", ddir=ddir)
                #Use textract to get the data from the pdf
                readPDF = fitz.open(sourcePDF["download_path"])
                for i in readPDF:
                    text = text + i.get_text()
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
            
            useSupp = input("Use a second file? ")
            if useSupp == "y" or useSupp == "Y" or useSupp == "yes" or useSupp == "Yes":
                suppFile = input("Enter the absolute path to the supplementary file: ")
                text = text + open(suppFile,'r').read()
            elif text == "0":
                print("No inputs given, closing...")
                return
            else:
                print("No secondary file chosen.")

            skipVideo = input("Skip downloading video files? ")
            if skipVideo == "y" or skipVideo == "Y" or useSupp == "yes" or useSupp == "Yes":
                downloadVideos = False
            else:
                downloadVideos = True
            break
        except KeyboardInterrupt:
            return
        except:
            print("Error, please try again:")
            continue
    
    channels = re.findall(r"(@[^\\:;/]+)", text)

    #Clean  channel list
    for i in channels:
        if "\\" in i or "https" in i:
            channels.remove(i)

    #Iterate through each channel
    for i in channels:
        print(f"Now downloading channel: {str(i)} \n")
        #Find all claims of the channel
        claimIds = []

        #Get the channel's claims
        try:
            channelClaims = lbryt.list_ch_claims(i, claim_id=True, title=True)
        except:
            print("Error loading channel's claims, skipping...")
            continue
        
        for i in channelClaims['claims']:

            #If it's a report, ignore 
            if i['value_type'] != 'repost':

                if downloadVideos == True:
                    claimIds.append(i["claim_id"])
                
                elif downloadVideos == False:
                    if i['value']['stream_type'] != 'video':
                        claimIds.append(i["claim_id"])

        #Iterate through each claim we've chosen to download, and pass them to the lbrynet daemon
        for i in claimIds:
            try:
                lbryt.download_single(cid=i, ddir=ddir, own_dir=True)
            except KeyboardInterrupt:
                return
            except:
                pass

if __name__ == "__main__":
    main()
