secretNum = 9
guess = 0;
for i in range(1, 10):
    if secretNum == i:
        print("secret num is", i)
        break;
    else: print("not found")
if i != secretNum:
    print("Did not find secret number")
