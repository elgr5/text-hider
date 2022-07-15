from PIL import Image



binary = "01101010"

text = binary.replace(" ", "")

textList = []

for bit in text:
    textList.append(bit)

im = Image.open('input.jpg')
pixelMap = im.load()

img = Image.new( im.mode, im.size)
pixelsNew = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i, j] = pixelMap[i, j]


for i in range(len(textList)):
    pixelList = list(pixelMap[i, 0])

    redValue = pixelList[0]

    if textList[i] == '1':
        if redValue % 2 == 1:
            pixelMap[i,0] = (redValue + 1, pixelList[1], pixelList[2], 255)
            pixelsNew[i,0] = pixelMap[i,0]
    elif textList[i] == '0':
        if redValue % 2 == 0:
            pixelMap[i,0] = (redValue + 1, pixelList[1], pixelList[2], 255)
            pixelsNew[i,0] = pixelMap[i,0]



im.close()
img.show()       
img.save("output.png") 
img.close()
