from datetime import datetime

now=datetime.now().time()
a=now.strftime("%H:%M:%S")
a=[int(i) for i in a.split(':')]
    
mint=a[1]

while 1:
    now=datetime.now().time()
    a=now.strftime("%H:%M:%S")
    a=[int(i) for i in a.split(':')]
    if(a[2]==0) and a[1]!=mint:
        print(now)
        mint=a[1]
