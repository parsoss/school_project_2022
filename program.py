import os
import glob
import pathlib
import sys

isdanger = 0
isexist = 0

file_dir = input("검사를 원하는 파일의 경로와 이름을 입력해주십시오. (확장명 포함)")

path = pathlib.Path(file_dir)

filename = path.name
fn = filename.strip(path.suffix)

print('상위 경로:', path.parent)
print('파일 이름:', fn)

p = path.suffix

print("파일 확장명: "+ p)

if p == ".vbs":
    print("윈도우가 만든 스크립트 언어이며, 막강한 권한을 가지고 있어 바이러스로 자주 이용되니 주의하셔야 됩니다.")
elif p == ".exe":
    print("윈도우에서 실행되는 실행파일을 의미합니다. 바이러스를 가지고 있을 가능성이 있으니 주의하셔야 합니다.")
elif p==".mp4" or p==".mkv":
    print("동영상을 실행하는 확장자 입니다.")
elif p == ".mp3":
    print("디지털 오디오를 플레이하는 확장자 입니다.")
elif p == ".bmp":
    print("비트맵 디지털 그림을 저장하는 데 쓰이는 그림 파일 포맷입니다.")
elif (p ==".jpg") or (p==".png"):
    print("이미지 파일입니다.")
elif (p==".gif"):
    print("움직이는 이미지 입니다.")
elif (p==".zip") or (p==".7z") or (p==".apk") or (p==".rar") or (p==".tar"):
    print("압축된 파일입니다. 압축을 해제하고 다시 시도해 주십시오.")
    sys.exit(0)
elif (p==".hwp"):
    print("한글파일입니다.")
elif(p==".pdf"):
    print("pdf 파일입니다.")
elif(p==".css"):
    print("css 스타일 시트 파일입니다.")
elif(p==".html"):
    print("웹 사이트를 실행하는 html 파일입니다.")
elif(p==".js"):
    print("자바스크립트 실행 파일입니다.")
elif(p==".c"):
    print("c언어 파일입니다.")
elif(p==".cpp"):
    print("c++파일입니다.")
elif(p=="ppt"):
    print("프레전테이션(파워포인트) 파일입니다.")
elif(p==".bat") or (p==".cmd"):
    print("윈도우 cmd 실행파일입니다.")

files = glob.glob(file_dir)
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
    with open(str(i)+".txt", "r", encoding="utf-8") as f:
        file_ne[i] = f.read().replace('\n', ' ')

asdf = 0
with open(str(fn)+".txt", "r", encoding="utf-8") as fne:
        asdf = fne.read().replace('\n', ' ')

newasdf= 0
        
for i in range (1, 5):
    if(file_ne[i] in asdf):
        isdanger = 1
        print(file_ne[i])
        newasdf = asdf.strip(file_ne[i])
        fin = open(fn+".txt", "rt", encoding="utf-8")
        with open(fn+".txt", "rt", encoding="utf-8") as file:
            x = file.read()

        with open(fn+".txt", "wt", encoding="utf-8") as file:
            x = x.replace(asdf,"f")
            fin.write(x)


if(isdanger):
    print("위험합니다")
else:
    print("안전합니다.")
    
ff = glob.glob(str(path.parent)+"/"+str(fn)+".txt")
for name in ff:
    if not os.path.isdir(name):
        src = os.path.splitext(name)
        os.rename(name, src[0] + path.suffix)
