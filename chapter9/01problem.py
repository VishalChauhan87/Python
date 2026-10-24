with open("poem.txt", "r") as f:
    c = f.read()

if("Twinkle" in c):
    print("Twinkle is present in c")
else:
    print("Twinkle is not present in c")