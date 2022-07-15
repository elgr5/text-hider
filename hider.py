from PIL import Image

# set the binary text
binary = "01101010"

# remove the space between each bytes

text = binary.replace(" ", "")

# each bytes will be put in this array

textList = []

# increment each bytes

for bit in text:
    textList.append(bit)

# open the image and load it

im = Image.open('input.jpg')
pixelMap = im.load()

# we create a new image

img = Image.new( im.mode, im.size)
pixelsNew = img.load()

# copy the imported image to the new image

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i, j] = pixelMap[i, j]


# loop how many bits we need

for i in range(len(textList)):


    # by default, pixelMap[x, y] return a tuple, by define `pixelList = list(pixelMap[x, y])`, we can get (R, G, B)

    pixelList = list(pixelMap[i, 0])

    # we get the red value

    redValue = pixelList[0]

    # check if the bits == 1, and if the red value is odd, increment + 1 to be pair

    if textList[i] == '1':
        if redValue % 2 == 1:
            pixelMap[i,0] = (redValue + 1, pixelList[1], pixelList[2], 255)
            pixelsNew[i,0] = pixelMap[i,0]
    else:
        if redValue % 2 == 0:
            pixelMap[i,0] = (redValue + 1, pixelList[1], pixelList[2], 255)
            pixelsNew[i,0] = pixelMap[i,0]


# closes images and save the output image
im.close()  
img.save("output.png") 
img.close()
