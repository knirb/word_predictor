import os
ss = open('blogs_detagged_test.txt', 'w')
def main():
    #f = open('blogs_detagged_test.txt','w+')
    path = 'blogs/'
    good = 0
    bad = 0
    for filename in os.listdir(path):

        try:
            fixXML(path,filename)
            good += 1
        except:
            bad += 1
        if good == 100:
            break
    print('good: ' + str(good))
    print('bad: ' + str(bad))

    ss.close()
def fixXML(filePath, fileName):
    s = open(filePath + fileName)
    print(fileName)
    skipStrings = ['<Blog>\n','</Blog>', '<post>\n', '</post>\n', '\n']
    for line in s.readlines():
        if line not in skipStrings and line[0:6] != '<date>':
            ss.write(line)
    s.close()

if __name__ == '__main__':
    main()
