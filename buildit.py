import os
import sys
import shutil, errno
from os.path import expanduser


home = expanduser("~")
file_dir = raw_input("Enter directory name: \n")
temp_dir ="app-prototype"
   
print "Moving project files..."
print ""
print ""
try:
    shutil.copytree(temp_dir, home+"/"+temp_dir)
except OSError as exc: # python >2.5
    if exc.errno == errno.ENOTDIR:
        shutil.copy(temp_dir, home+"/"+temp_dir)
    else: raise
print "Renaming project files..."
print ""
print ""
os.rename(home+"/"+temp_dir,home+"/"+file_dir)
print "Project Files moved to: "+home+"/"+file_dir
print ""
print ""

with open(home+"/"+file_dir+'/package.json', 'w+') as file:
    file.write('{\n')
    project_name = raw_input("Enter project name: \n")
    file.write('"name":"'+project_name+'",\n')
    
    file_version = raw_input("Enter file version, example(0.0.0): \n")
    file.write('"version":"'+file_version+'",\n')
    
    file_description = raw_input("Enter project description: \n")
    file.write('"description":"'+file_description+'",\n')    
    
    file.write('"main":"index.html",\n')
    
    file_author = raw_input("Enter Author full name: \n")
    file.write('"author":"'+file_author+'"\n')
    
    file.write('}\n')
    
    print ""
    print "Package created successfully!"
    print ""
    print "Do you want to create a run script for application?\n"
    print "1) Yes\n"
    print "2) No\n"
    answer = raw_input("Enter number: ")
    print ""
    
    if answer == "1":
        print "Which platform ?\n"
        print "1) Linux"
        print "2) Windows"
        print "3) Mac OS"
        system_type = raw_input("Enter number: ")
        print ""
        if system_type == "1":
            nw_dir = raw_input("Enter node-webkit dir (full path ex(/home/user/nw))\n")
            with open(home+"/"+file_dir+'/run.sh', 'w+') as file:
                file.write(nw_dir+"/nw "+home+"/"+file_dir)  
        elif system_type == "2":
            print "Not Aviable !"
        elif system_type == "3":
            print "Not Aviable !"
        else:
            print "Wrong answer 1"
        print "Instalation is complete, you are ready to make some magic!"
        print "You can run your app from "+home+"/"+file_dir+" by executing run.sh file or using full path to nw (/home/user/nw /home/user/projectName/)!"
    else :
        print "Instalation is complete, you are ready to make some magic!"
        print "Your project is in "+home+"/"+file_dir+" directory!"
        
        
        
    
    
    

