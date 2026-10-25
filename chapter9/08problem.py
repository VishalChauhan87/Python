with open("file.txt", "r") as f:
    content1=f.read()

with open("poem.txt", "r") as f:
    content2=f.read()

if(content1==content2):
    print("yes these file are identical")

else:
    print("NO these file are not identical")



    # if we want to cler any data from any of the file .

   # with open("log.txt", "w") as f :
    #    f.write("")
