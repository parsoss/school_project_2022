import os
import glob
import pathlib
import sys
from google.colab import drive
import chardet

isdanger = 0
isexist = 0

file_dir = input("검사를 원하는 파일의 경로와 이름을 입력해주십시오. (확장명 포함)  ")

path = pathlib.Path(file_dir)

filename = path.name
fn = filename.strip(path.suffix)

print('상위 경로:', path.parent)
print('파일 이름:', fn)

p = path.suffix

print("파일 확장명: "+ p)
rawdata = open(file_dir, 'rb').read()
result = chardet.detect(rawdata)
enc = result['encoding']

files = glob.glob("/content/gdrive/My Drive/학교_진로발표/"+str(fn)+".txt")
print("/content/gdrive/My Drive/학교_진로발표/"+str(fn)+".txt")
for name in files:
    if not os.path.isdir(name):
        src = os.path.splitext(name)
        os.rename(name, src[0]+'.txt')
        isexist = 1
        
        
if(isexist == 0):
    print("파일이 존재하지 않습니다.")
    sys.exit(0)        
        
        
        
file_ne=[0, 0, 0, 0, 0, 0, 0]
i=0
for i in range (1, 5):
    with open("/content/gdrive/My Drive/학교_진로발표/"+str(i)+".txt", "r", encoding=enc) as f:
        file_ne[i] = f.read().replace('\n', ' ')

asdf = 0
with open("/content/gdrive/My Drive/학교_진로발표/"+str(fn)+".txt", "r", encoding=enc) as fne:
        asdf = fne.read().replace('\n', ' ')

newasdf= 0
isdanger = 0
for i in range (1, 5):
    if(file_ne[i] in asdf):
        isdanger = 1
        print(file_ne[i])
        print("바이러스가 발견되었습니다. 치료를 시작합니다.")
        os.remove("/content/gdrive/My Drive/학교_진로발표/"+str(fn)+".txt")
        print("치료가 완료되었읍니다")
if(not isdanger):
    print("안전합니다.")
    
ff = glob.glob("/content/gdrive/My Drive/학교_진로발표/"+str(path.parent)+"/"+str(fn)+".txt")
for name in ff:
    if not os.path.isdir(name):
        src = os.path.splitext(name)
        os.rename(name, src[0] + path.suffix)
