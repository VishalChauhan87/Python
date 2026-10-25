with open("log.txt","r") as f:
    content=f.read()

if ("python" in content):
    print("yes python is in content")

else:
    print("no python is not in the content")