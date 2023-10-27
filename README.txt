----------------------------------------------Instructions for usage----------------------------------------------


					Windows 10

1. Install Python and Git
Install Python:
https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
Make sure the Python executable is added to the PATH so that it can be launched from anywhere in your system.

Install Git:
https://gitforwindows.org/
Make sure to check "Git from the command line" in PATH settings during installation

2. Install dependancies
#This will install the python packages you need
python -m pip install requests regex PyMuPDF

#Run the following line, and copy the output:
python -m site --user-site
cd %Output of above%
#Into here ^, remove the %'s
mkdir lbrytools
git clone https://github.com/belikor/lbrytools/

3. Download and start lbrynet
#Download and extract the latest lbrynet release from here: https://github.com/lbryio/lbry-sdk/releases
#Then run it by opening a command prompt at this folder (you can type CMD into folder path in file explorer to open a terminal, or use cd to navigate to the directory) and run: 
lbrynet start

4. Run the Python file
#Download the python file from the Github at https://github.com/ratufacturing/fossea_archive/blob/main/fossea_archive.py, and open a terminal in the folder you download it to. Run it with
python fossea_archive.py
#Enter the download directory- where you want your files to go. For example:
C:\Users\%Username%\Documents\LBRYDL
#Choose whether you want to import the BLC Guncad list, answers other than yes/y will default to no
#Choose if you want to use a supplementary file (should probably be .txt). This should recognize any @username as long as they're seperated on different lines or with semicolons or similar.
#Make sure you give it the absolute path, something like:
C:/Users/%Username%/Documents/LBRYDL/extra_channels.txt



					Ubuntu:

1. Install Python and Git
Should both already by installed, but if not:
sudo apt update
sudo apt install git
sudo apt install python3

2. Install dependancies
#This will install the python packages you need
pip install requests regex PyMuPDF

#Run the following line, and copy the output:
python3 -m site --user-site
cd %Output of above%
#Into here ^, remove the %'s
mkdir lbrytools
git clone https://github.com/belikor/lbrytools/

3. Download and start lbrynet
#Download and extract the latest lbrynet appimage release from here: https://github.com/lbryio/lbry-sdk/releases
#Then navigate to your extracted folder and run: 
./lbrynet start
#If you're having trouble with wallet things and are having connection issues, it's worth checking to see if it's a hashlib error- I was having issues but fixed it with this: https://stackoverflow.com/a/72509045

4. Run the Python file
#Download the python file from the Github at https://github.com/ratufacturing/fossea_archive/blob/main/fossea_archive.py, and open a terminal in the folder you download it to. Run it with:
python3 fossea_archive.py
#Enter the download directory- where you want your files to go. For example:
/home/%Username%/LBRYDL
#Choose whether you want to import the BLC Guncad list, answers other than yes/y will default to no
#Choose if you want to use a supplementary file (should probably be .txt). This should recognize any @username as long as they're seperated on different lines or with semicolons or similar.
#Make sure you give it the absolute path, something like:
/home/%Username%/LBRYDL/extra_channels.txt

