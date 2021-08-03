from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
# cv2读取图片,openev是BGR
img = cv2.imread('1.jpg')
cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#BGR转RGB
pilimg = Image.fromarray(cv2img)

# PIL图片上打印汉字
draw = ImageDraw.Draw(pilimg)

fontStyle = ImageFont.truetype("simhei.ttf", 80, encoding="utf-8")

draw.text((50, 50), "池塘骤雨", (255, 0, 0), font=fontStyle)

# PIL图片转cv2 图片
cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

cv2.imshow("yyy", cv2charimg)

cv2.imwrite('bjj04.jpg',cv2charimg)
#保存图片
cv2.waitKey (0)
cv2.destroyAllWindows()
