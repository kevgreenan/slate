import sys
import os
import subprocess
from git import Repo

#-- Context manager
class cd:
    """Context manager for changing the current working director"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

#-- set up Projects folders
numType = input("How many group folders do you want (ex. 'Python', 'Web', or 'C++')? ")
pathArray = ['initial'] * numType
path = r'Projects'
for i in range(0, len(pathArray)):
    pathArray[i] = raw_input("Enter subfolder name: ")
for i in range(0, len(pathArray)):
    newPath = os.path.join(path, pathArray[i])
    if not os.path.exists(newPath):
        os.makedirs(newPath)
        print("%s created." %pathArray[i])

#-- set up Git stuff
gitInstalled = 0
with cd("/usr/bin"):
    gitPath = r'git'
    if not os.path.exists(gitPath):
        gitInstalled = 0
    elif os.path.exists(gitPath):
        gitInstalled = 1
    else:
        path = r'/usr/bin'
        gitPath = os.path.join(path, gitPath)
        print("PathError:  the path, %s , is unable to be identified." %(gitPath))
if gitInstalled:
    input = raw_input("Do you want to clone your repos into a temporary folder? Y/n ")
    if input == "y" or input == "Y":
        path = r'temp_git_projects'
        if not os.path.exists(path):
            os.makedirs(path)
        with cd(path):

            #-- REPLACE THESE WITH YOUR OWN REPO URLs --#
            gitURLS = [
                r'https://github.com/kevgreenan/aboutme.git',
                r'https://github.com/kevgreenan/Constructor.git',
                r'https://github.com/kevgreenan/prython.git',
                r'https://github.com/kevgreenan/ConquerTech.git',
                r'https://github.com/kevgreenan/Cardio.git',
                r'https://github.com/kevgreenan/Faro.git',
                r'https://github.com/kevgreenan/cog.git',
                r'https://github.com/kevgreenan/GreenTrack.git',
                r'https://github.com/kevgreenan/mobile-template.git',
                r'https://github.com/kevgreenan/CSS-colors.git',
                r'https://github.com/kevgreenan/QuickBudget.git',
                r'https://github.com/kevgreenan/AssetTracker.git',
                r'https://github.com/kevgreenan/CarrotField.git'
            ]
            for i in range(0, len(gitURLS)):
                gitURL = gitURLS[i]
                repoName = gitURL[30:-4]
                newPath = repoName
                Repo.clone_from(gitURL, newPath)
                current = float(i + 1)
                total = float(len(gitURLS))
                progress = int((current/total)*100)
                print("%s%% comeplete: %s cloned." %(progress, repoName))

    else:
        print("do not clone the repos") # comment this out for release
