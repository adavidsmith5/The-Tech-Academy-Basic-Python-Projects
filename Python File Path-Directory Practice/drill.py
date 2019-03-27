import os
directory = 'C:\\Users\\6420 i7\\Documents\\GitHub\\The-Tech-Academy-Basic-Python-Projects'
files = os.listdir(directory)
txtFiles=[]
time=[]
drillSolution = {}


def completeDrill():
    findTxtFiles()
    getTimeStamps()
    createFileDictionary()
    printFiles()

def findTxtFiles():
    for file in files:
        if file.endswith('.txt'):
            txtFiles.append(os.path.join(directory,file))

            
def getTimeStamps():
    for file in txtFiles:
        time.append(os.path.getmtime(file))
    

def createFileDictionary():
    i=0
    while i < len(txtFiles):
        drillSolution[txtFiles[i]]=time[i]
        i+=1

def printFiles():
    for item in drillSolution:
        print("{}: {}".format(item,drillSolution[item]))




if __name__ == "__main__":
    completeDrill()
