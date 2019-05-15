import xml.etree.ElementTree as ET
import os
f = open('blogs_detagged_test.txt','w+')
path = 'fixed_blogs/'
badCount = 0
goodCount = 0
#TODO : Add some marker that a new post has started
def main():
    for filename in os.listdir(path):
        #try:
        parser = ET.XMLParser(encoding="utf-8")
        fileLocation = path + filename
        #fixXML(fileLocation)
        tree = ET.parse(fileLocation, ET.XMLParser(encoding="utf-8"))
        root = tree.getroot()
        for child in root:
            if child.tag == 'post':
                f.write(str(child.text))
        #    goodCount += 1
        #except:
        #    badCount += 1
            #print(filename)
            #break
    #print('good: ' + str(goodCount))
    #print('bad: ' + str(badCount))
    f.close()

if __name__ == '__main__':
    main()
