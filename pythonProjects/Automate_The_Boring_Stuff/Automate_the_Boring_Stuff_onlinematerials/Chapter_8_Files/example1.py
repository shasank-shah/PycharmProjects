import os
var1 = os.path.join('usr', 'bin', 'spam')
print (var1)

myfiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in  myfiles:
    print (os.path.join('C:', 'bin'), filename)

var2 = os.listdir()
print (var2)

print (os.path.join("D:", "Shasank"))
var3 = os.path.join("D:\\", "Shasank")
var4 = os.path.normcase(var3)
print (var3)
print (var4)

var5 = os.listdir(var4)
print (var5)

for name in var5:
    print (name)
    if (str.lower(name) == "cts"):
        var6 = os.path.join(var3, name)
        print (var6)
        var7 = os.path.isdir(var6)
        if (var7):
            var8 = os.listdir(var6)
            print (var8)
            for filename in var8:
                print (filename)
                var9 = os.path.join(var6, filename)
                print (var9)
                var10 = os.path.isfile(var9)
                if (var10):
                    print (var10)
                    #exit ()

print (os.getcwd())

new_folder_name = "Sample"
print (var6)
#exit ()
#os.makedirs(os.path.join(var6, new_folder_name))

var11 = os.path.basename(var6)
print (var11)

var12 = os.path.dirname(var11)
print (var11)