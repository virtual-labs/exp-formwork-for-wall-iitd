import os

def convert(name):
    return '''
    <img
        class="main-window-imgs"
        src="./src/images/{0}"
        title="{0}"
        alt="{0}"
    />
    '''.format(name)

def src(name :str,i :int):
    return name[0:name.find('.')] + ":this.allImgsDom[{0}],\n".format(i)

names = os.listdir("s://Users//Utkarsh//Documents//Project//CE5//src//images//temp")

imgs = ''
for name in names:
    imgs = imgs + name


srcs = ''
for i in range(len(names)):
    # srcs = srcs + convert(names[i])
    srcs = srcs + src(names[i],i+98)



# open("temp.txt","w").write()
open("temp2.txt","w").write(srcs)
print(srcs)

# 