x=int(input("lütfən doğulduğunuz ayın rəqəmini qeyd edin məs:4"))
z=int(input("lütfən doğulduğunuz günün rəqəmini qeyd edin məs:25"))

if x==1:
    if z<20:
        burc="oğlaq"
    elif z>20:
        burc="dolça"
elif x==2:
    if z<20:
        burc="dolça"
    elif z>20:
        burc="balıq"
elif x==3:
    if z<20:
        burc="balıq"
    elif z>20:
        burc="qoç"
elif x==4:
    if z<20:
        burc="qoç"
    elif z>20:
        burc="buğa"
elif x==5:
    if z<20:
        burc="buğa"
    elif z>20:
        burc="əkizlər"
elif x==6:
    if z<20:
        burc="əkizlər"
    elif z>20:
        burc="xərçəng"
elif x==7:
    if z<20:
        burc="xərçəng"
    elif z>20:
        burc="şir"
elif x==8:
    if z<20:
        burc="şir"
    elif z>20:
        burc="qız"
elif x==9:
    if z<20:
        burc="qız"
    elif z>20:
        burc="tərəzi"
elif x==10:
    if z<20:
        burc="tərəzi"
    elif z>20:
        burc="əqrəb"
elif x==11:
    if z<20:
        burc="əqrəb"
    elif z>20:
        burc="oxatan"
elif x==12:
    if z<20:
        burc="oxatan"
    elif z>20:
        burc="oğlaq"

print("sizin bürcünüz ="+" "+burc)
