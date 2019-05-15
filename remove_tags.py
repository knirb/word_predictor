def main():
    #f = open('blogs_detagged_test.txt','w+')
    path = 'blogs/'
    fixXML(path, '1000866.female.17.Student.Libra.xml')
#for filename in os.listdir(path):
    #break
def fixXML(filePath, fileName):
    s = open(filePath + fileName)
    ss = open('fixed_blogs/' + fileName, 'w')
    skipStrings = ['<Blog>\n','</Blog>\n', '<post>\n', '</post>\n', '\n']
    for line in s.readlines():
        if line not in skipStrings and line[0:6] != '<date>':
            ss.write(line)
    s.close()
    ss.close()

if __name__ == '__main__':
    main()
