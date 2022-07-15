from PIL import Image

# get the image to reveal text

im = Image.open("output.png");

pixelMap = im.load()

# we have to get how many bytes the text are

bits = 18 * 8

# this variable will contain the result

result = ""

for i in range(bits):
    pixelList = list(pixelMap[i, 0])
    if pixelList[0] % 2 == 0:
        # if it's pair it's a 1 else a 0
        result += "1"
    else:
        result += "0"

# untie all bytes

binary = [result[i:i + 8] for i in range(0, len(result), 8)]

sentence = ""

# convert it into char

for i in range(len(binary)):
    sentence += chr(int(binary[i], 2))

print(sentence)