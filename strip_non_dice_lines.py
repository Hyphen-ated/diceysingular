import glob,os,re

reg = re.compile('^.*[Dd]ice[^a-zA-Z].*$')

os.chdir('./die/data/text/locale/di')
for file in glob.glob("*.csv"):
    f = open(file, 'r')
    content = f.readlines()
    f.close()
    f = open(file, 'w')
    first = True
    for line in content:
        if first or reg.match(line):
            f.write(line)
        first = False
    f.close()
    
