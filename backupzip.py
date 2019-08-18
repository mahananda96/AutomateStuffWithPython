import os, zipfile

def backup(folder):
    number=1
    while True:
        abs_path=os.path.abspath(folder)
        foldername=os.path.basename(abs_path)
        foldername=foldername+"_"+str(number)+".zip"
        if(not os.path.exists(foldername)):
            break
        number=number+1
    backupzip=zipfile.ZipFile(foldername,'w')
    print("Creating "+foldername)
    #print(abs_path)
    #print(filename)
    for folder,subfolder,file in os.walk(folder):
        print("Adding "+folder)
        backupzip.write(folder)
        for filename in file:
            print("Adding "+filename)
            backupzip.write(os.path.join(folder,filename))
        

backup('C:\\Example')
