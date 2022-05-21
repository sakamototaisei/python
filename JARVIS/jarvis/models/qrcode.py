import qrcode


img = qrcode.make('https://www.youtube.com/channel/UClizmtAimxjyiPt8UXAB32w')

img.save('result.png')

print(img)