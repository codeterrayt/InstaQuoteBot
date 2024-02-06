from PIL import Image, ImageDraw, ImageFont
import time
import numpy as np


def current_milli_time():
    return round(time.time() * 1000)


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele + " "
    return str1


def GetFont(size, font_index):
    if font_index == 0: return ImageFont.truetype('font/VeganStylePersonalUse-5Y58.ttf', size)
    if font_index == 1: return ImageFont.truetype("font/heading.ttf", size)


background_color = (2, 48, 71)
author_font_color = (255, 183, 3)
ContentColor = (251, 133, 0)
galaxy_image_size = (1000, 1000)


def GenerateImage(author, content, path="", styleIndex=0, InstaAccountUserName="codeterrayt"):
    img = Image.new('RGB', (1080, 1080), color=background_color)  # 73, 109, 137
    writeText = ImageDraw.Draw(img)



    if styleIndex == 1:
        foreground_image = Image.open("templates/earth-with-bg.png")
        img.paste(foreground_image, (0, 0), foreground_image)
    else:
        foreground_image = Image.open("templates/earth.png")
        img.paste(foreground_image.resize(galaxy_image_size), (400, 600), foreground_image.resize(galaxy_image_size))

    InstagramLogo = Image.open("templates/insta.png")
    img.paste(InstagramLogo.resize((50,50)), (565, 930) , InstagramLogo.resize((50,50)))

    # d.text((220, 100), author+" Said", font=GetFont(70), fill=(255, 255, 0))
    if len(author) > 10: writeText.text((220, 100), author + " Said", font=GetFont(60, 1),
                                        fill=author_font_color)
    if len(author) < 10: writeText.text((220, 120), author + " Said", font=GetFont(70, 1),
                                        fill=author_font_color)

    writeText.text((620, 920),InstaAccountUserName, font=GetFont(35, 1),
                   fill= (255,255,255,50) )

    Splitcontent = content.split()
    CountWord = 0
    Start = 0
    End = 4
    MultiList = []

    for word in Splitcontent:
        if CountWord == 4:
            MultiList.append(Splitcontent[Start:End])
            Start = End
            End += CountWord
            CountWord = 0
        CountWord += 1

    SingleList = len(np.array(MultiList).flatten())

    MultiList.append(Splitcontent[SingleList:])

    y = 0
    for list in MultiList:
        for word in list:
            Sentence = listToString(list)
            writeText.text((110, 320 + y), Sentence, font=GetFont(60, 0), fill=ContentColor)
        x = 0
        y += 100

    # working but not satisfied

    # y = 0
    # start = 0
    # end = 28

    # for i in range(0,len(content) , 28):
    #     if end >= len(content):
    #         end = len(content)
    #     else:
    #         pass
    #     writeText.text((110, 340 + y), content[start:end], font=GetFont(60), fill=(255, 255, 0))
    #     start = end
    #     end += 28
    #     y += 100

    final_path = str(path) + "quotes" + str(current_milli_time()) + '.jpg'
    img.save(final_path)
    return final_path
