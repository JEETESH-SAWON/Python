import subprocess
 
imgPath = "image/test.jpg"
exeProcess = "hachoir-metadata"
process = subprocess.Popen([exeProcess,imgPath],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           universal_newlines=True)
Dic={}
 
for tag in process.stdout:
        line = tag.strip().split(':')
        Dic[line[0].strip()] = line[-1].strip()
 
for k,v in Dic.items():
    print(k,':', v)