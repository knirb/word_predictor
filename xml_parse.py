import xml.etree.ElementTree as ET
import os
f = open('blogs_detagged.txt','w+')
path = 'blogs/'
badCount = 0
goodCount = 0
for filename in os.listdir(path):
    try:
        fileLocation = path + filename
        tree = ET.parse(fileLocation)
        root = tree.getroot()
        for child in root:
            if child.tag == 'post':
                f.write(str(child.text))
        goodCount += 1
    except:
        badCount += 1
print('good: ' + str(goodCount))
print('bad: ' + str(badCount))
f.close()
