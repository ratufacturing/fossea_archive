## ----------------------------------------------Instructions for usage----------------------------------------------


# Windows 10

1. Install Python and Git
	* Install Python:
 		* https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
	* Make sure the Python executable is added to the PATH so that it can be launched from anywhere in your system.

	* Install Git:
		* https://gitforwindows.org/
	* Make sure to check "Git from the command line" in PATH settings during installation

2. Install dependancies
	* This should install all the required Python packages you need
<br/>`python -m pip install pip3 install git+https://github.com/ratufacturing/lbrytools/`

3. Download and start lbrynet
	* Download and extract the latest lbrynet release from here: https://github.com/lbryio/lbry-sdk/releases
	* Then run it by opening a command prompt at this folder (you can type CMD into folder path in file explorer to open a terminal, or use cd to navigate to the directory) and run: 
<br/>`lbrynet start`

4. Run the Python file
	* Download the Python file from the Github at https://github.com/ratufacturing/fossea_archive/blob/main/fossea_archive.py, and open a terminal in the folder you download it to. Run it with
<br/>`python fossea_archive.py`
	* Enter the download directory- where you want your files to go. For example:
<br/>`C:\Users\%Username%\Documents\LBRYDL`
	* Choose whether you want to import the BLC Guncad list, answers other than yes/y will default to no
	* Choose if you want to use a supplementary file (should probably be .txt). This should recognize any @username as long as they're seperated on different lines or with semicolons or similar.
	* Make sure you give it the absolute path, something like:
<br/>`C:/Users/%Username%/Documents/LBRYDL/extra_channels.txt`



# Ubuntu:

1. Install Python, Git, and unzip
<br/>`sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip unzip -y`

2. Install the required Python libraries
<br/>`pip3 install git+https://github.com/ratufacturing/lbrytools/ --break-system-packages`
	* Newer Ubuntu versions want you to install packages properly, but this is easier and works fine. Set up a venv if you care.

 3. Download and start lbrynet 
	* Run one at a time:
	* The "> /dev/null 2>&1 &" modification will run it as a slient background process. Remove it and run in a different window for troubleshooting
	* Give it ~5-20 mins for lbrynet to finish thinking about blockchain things the first time you run this or it’ll complain about the JSONs it’s getting
```
mkdir ~/LBRY && cd $_

wget https://github.com/lbryio/lbry-sdk/releases/download/v0.113.0/lbrynet-linux.zip

wget https://raw.githubusercontent.com/ratufacturing/fossea_archive/refs/heads/main/fossea_archive.py

unzip lbrynet-linux.zip

~/LBRY/lbrynet start > /dev/null 2>&1 &
```

4. Run the Python file
	* Download the Python file from the Github at https://github.com/ratufacturing/fossea_archive/blob/main/fossea_archive.py, and open a terminal in the folder you download it to. Run it with:
<br/>`python3 fossea_archive.py`

	* Enter the download directory- where you want your files to go. For example: (replace "%Username" with your linux username)
<br/>`/home/%Username%/LBRYDL`

	* Choose whether you want to import the BLC Guncad list, answers other than yes/y will default to no
	* Choose if you want to use a supplementary file (should probably be .txt). This should recognize any @username as long as they're seperated on different lines or with semicolons or similar.
	* Make sure you give it the absolute path, something like:
<br/>`/home/%Username%/LBRYDL/extra_channels.txt`
	* If you're having trouble with connection issues, it's worth checking to see if it's a hashlib error- I was having issues but fixed it with this: https://stackoverflow.com/a/72509045
