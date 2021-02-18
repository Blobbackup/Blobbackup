# Installation

There are a few different ways that you can install BlobBackup.

## Installing a Release 

If you are looking to install a release version, you can either 
download the latest version directly from our 
[home page](https://blobbackup.com) or from the 
[Github releases](https://github.com/bimbashrestha/blobbackup/releases)
page. 

### Mac

Once you download the Mac version, just open the dmg file and 
copy the BlobBackup app into your Applications folder. You will
have to right click > open the application if you're using 
BlobBackup for the first time as the binary has not been 
code signed.

### Windows

Once you download the Windows version, just open the executable 
and follow the instructions on screen to setup your application. 
You may see a blue window warning you about opening apps from 
an unknown publisher. You can click "more info" and run anyway 
if you see this. The binary has not been code signed.

### Linux

```
# After unzipping the downloaded version

chmod +x BlobBackup/BlobBackup
BlobBackup/BlobBackup

# Or alternatively if you want BlobBackup to run in the background
BlobBackup/BlobBackup&
```

## Installing from Source

To test a source version, you will need to have a python 3.7 
environment set up. The source will likely compile with most 
python 3.X versions but it has not been tested with anything 
other than 3.7. 

Miniconda is a great enviornment management tool and is what 
we use when developing BlobBackup. We create a miniconda 
python 3.7 environment like this and activate it before following 
the other steps.

```
conda create -n py37 python=3.7
conda activate py37
```

First clone the repo.

```
git clone https://github.com/bimbashrestha/blobbackup
```

Install the dependencies.

```
pip install -r requirements.txt

# on windows, also install this
pip install pywin32
```

Run the application.

```
cd src
python application.py
```

Currently, there is no way to install BlobBackup as a pip package 
on your python environment. We package all releases with pyinstaller 
anyway so this hasn't been a priority to set up. 

