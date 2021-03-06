from pyspark import SparkContext, SparkConf
from pyspark import SparkFiles
import os, zipfile

## CONSTANTS

APP_NAME = "My Spark Application"

conf = SparkConf().setAppName(APP_NAME)
sc = SparkContext(conf=conf)

##getDirectory() - returns root directory for distributed files
##get(filename) - returns absolute path to the file

#with open(SparkFiles.get('iris.txt')) as test_file:
#    print(test_file.read())

print(SparkFiles.getRootDirectory())

files = os.listdir(SparkFiles.getRootDirectory())
for file in files:
      #do some stuff
    print("######")
    print(file)

          

##########
#Try to unzip
###########

dir_name = SparkFiles.getRootDirectory()
print "#####" + dir_name + "#########"
extension = ".zip"

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file



## For Iris example
##files = os.listdir(SparkFiles.getRootDirectory() + "/files")
## For UCI example
files = os.listdir(SparkFiles.getRootDirectory() + "/uci")
for file in files:
      #do some stuff
    print("######")
    print(file)        
    
    #print SparkFiles.get()


## More UCI
files = os.listdir(SparkFiles.getRootDirectory() + "/uci/test")
for file in files:
      #do some stuff
    print("######")
    print(file)        
    
    #print SparkFiles.get()
    
##with open(SparkFiles.get('test.yml')) as test_file:
##    logging.info(test_file.read())

#files = os.listdir(os.curdir)
#for file in files:
#      #do some stuff
#      print(file)
