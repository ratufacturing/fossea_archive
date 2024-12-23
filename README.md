## <center>Instructions for usage</center>


# Windows 10

1. Install Python and Git
* Install Python:
 	* https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
	* Make sure the Python executable is added to the PATH so that it can be launched from anywhere in your system.

* Install Git:
	* https://gitforwindows.org/
	* Make sure to check "Git from the command line" in PATH settings during installation

<br/>2. Install dependancies
* This should install all the required Python packages you need
<br/>`python -m pip install git+https://github.com/ratufacturing/lbrytools/`

<br/>3. Download and start lbrynet
* Download and extract the latest lbrynet release from here: https://github.com/lbryio/lbry-sdk/releases
* Then run it by opening a command prompt at this folder (you can type CMD into folder path in file explorer to open a terminal, or use cd to navigate to the directory) and run: 
<br/>`lbrynet start`


* Be aware that lbrynet will default to writing blob files to a %Appdata% directory. Blob files are the pieces of files that are passed around by the LBRY protocol, and are used for downloading, seeding, and reconstructing files
* This will cause your C: drive to fill up more quickly (since it needs to write the data twice). Blobfile write location is controlled by the lbrynet daemon, which we can configure by creating and using a config file:
<br/>`echo "data_dir: 'c:\Users\%Username%\LBRY\lbryblobs'" > "daemon_settings.yml"`
* This will configure lbrynet to search for and store blobfiles and other blockchain data at the location C:\Users\%Username%\LBRY\lbryblobs (you need to replace %Username%). Note that if you later restart it, you must point it at the same location (use the same config file/directory) or it will need to redownload everything.
* If you really don't want to keep the blobfiles around, use the save_blobs setting which permits deletion of blobfiles after download completion. Note that this is **not recommended**, as it will require redownloading blobfiles again if the script is rerun (very slow), and means you won't be able to seed, which is a bit of a dick move. Edit your .yml file and add a second line:
<br/>`save_blobs: false`
* To tell lbrynet you want to use your new configuration, use the --config= option instead when starting it:
<br/>`lbrynet start --config=c:\Users\%Username%\LBRY\daemon_settings.yml`
* Other configuration options can be found at https://lbry.tech/resources/daemon-settings.

<br/>4. Run the Python file
* Download the Python file from the Github at https://github.com/ratufacturing/fossea_archive/blob/main/fossea_archive.py, and open a terminal in the folder you download it to. Run it with
<br/>`python fossea_archive.py`
* Enter the download directory- where you want your files to go. For example:
<br/>`C:\Users\%Username%\LBRY`
* Choose whether you want to import the BLC Guncad list, answers other than yes/y will default to no
* Choose if you want to use a supplementary file (should probably be .txt). This should recognize any @username as long as they're seperated on different lines or with semicolons or similar.
* Make sure you give it the absolute path, something like:
<br/>`C:/Users/%Username%/LBRY/extra_channels.txt`



# Ubuntu:

1. Install Python, Git, and unzip
<br/>`sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip unzip -y`

<br/>2. Install the required Python libraries
<br/>`pip3 install git+https://github.com/ratufacturing/lbrytools/ --break-system-packages`
* Newer Ubuntu versions want you to install packages properly, but this is easier and works fine. Set up a venv if you care.

<br/>3. Download and start lbrynet 
* Run one at a time:
* The "> /dev/null 2>&1 &" modification will run it as a slient background process. Remove it and run in a different window for troubleshooting
* Give it ~5-20 mins for lbrynet to finish thinking about blockchain things the first time you run this or it’ll complain about the JSONs it’s getting
```
mkdir ~/LBRY && cd $_

wget https://github.com/lbryio/lbry-sdk/releases/download/v0.113.0/lbrynet-linux.zip

unzip lbrynet-linux.zip

~/LBRY/lbrynet start > /dev/null 2>&1 &
```

* Be aware that lbrynet will default to writing blob files to a .local directory. Blob files are the pieces of files that are passed around by the LBRY protocol, and are used for downloading, seeding, and reconstructing files
* This will cause your root drive to fill up more quickly (since it needs to write the data twice). Blobfile write location is controlled by the lbrynet daemon, which we can configure by creating and using a config file:
<br/>`printf "data_dir: '/home/%Username%/LBRY/lbryblobs'"> daemon_settings.yml`

* This will configure lbrynet to search for and store blobfiles and other blockchain data at the location /home/%Username%/LBRY/lbryblobs (you need to replace %Username%). Note that if you later restart it, you must point it at the same location (use the same config file/directory) or it will need to redownload everything.
* If you really don't want to keep the blobfiles around, use the save_blobs setting which permits deletion of blobfiles after download completion. Note that this is **not recommended**, as it will require redownloading blobfiles again if the script is rerun (very slow), and means you won't be able to seed, which is a bit of a dick move.
<br/>`printf "data_dir: '/home/%Username%/LBRY/lbryblobs'\nsave_blobs: false"> daemon_settings.yml`
* To tell lbrynet you want to use your new configuration, use the --config= option instead when starting it (can still make it silent by adding "> /dev/null 2>&1 &" to the end of the command):
<br/>`~/LBRY/lbrynet start --config=/home/%Username%/LBRY/daemon_settings.yml`
* Other configuration options can be found at https://lbry.tech/resources/daemon-settings.

<br/>4. Run the Python file
* Download the archival file from the Github using wget:
<br/>`wget https://raw.githubusercontent.com/ratufacturing/fossea_archive/refs/heads/main/fossea_archive.py`
* Make sure that your terminal is in the folder it's downloaded to before running it:
<br/>`python3 fossea_archive.py`
* To use: enter the download directory- where you want your files to go. For example: (replace "%Username" with your linux username)
<br/>`/home/%Username%/LBRYDL`

* Choose whether you want to import the BLC Guncad list, answers other than yes/y will default to no
* Choose if you want to use a supplementary file (should probably be .txt). This should recognize any @username as long as they're seperated on different lines or with semicolons or similar.
* Make sure you give it the absolute path, something like:
<br/>`/home/%Username%/LBRYDL/extra_channels.txt`
* If you're having trouble with connection issues, it's worth checking to see if it's a hashlib error- I was having issues but fixed it with this: https://stackoverflow.com/a/72509045

# Suggestions and more

* You should never run someone else's script without making sure that it's safe to do so, and isn't reporting to someone else. 
 
 	* I would reccomend taking a quick glance through it, it's pretty simple and I've tried to comment it well.
   
   * The lbrytools fork I created can also be found under my profile in another repo. I've personally gone through the originaly repo and it seems to be fine, you can check my commits to see what I've changed (only added a setup.py file and made a new folder to make it pip-able).
    
* I would highly reccomend using a VPN whenever doing any downloading (keeps your ISP from getting mad at you, keeps other entities off your ass. 
 
 	* I would reccomend ProtonVPN or AirVPN as VPNs that allow port forwarding. Please set up port forwarding and seed if you can, the LBRY network only stays alive with your help! Mullvad is also easy to use and one I trust.
     
* Setup a seedbox if you can. I'm going to try to make a Docker container if I get around to it (but it shouldn't be too hard if someone wants to beat me to it).
* I'm also going to try to make it runnable using CLI arguements at some point, which would allow setting it up as a service on Windows or Linux that runs in the background.
