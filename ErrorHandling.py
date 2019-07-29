# error handling example
try:
    fp = open("test.txt", "r")
except FileNotFoundError:
    print("no such file :(")
else:
    data = fp.read()
    print(data)
    fp.close()
finally:
    print("done!")
