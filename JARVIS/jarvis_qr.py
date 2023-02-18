import cv2
import qrcode

qr_dict = {
    1:'https://www.youtube.com/channel/UClizmtAimxjyiPt8UXAB32w',
    2:'streamlit作成アプリURL',
    3:'githunbのURL',
    4:'SNS等々',
    5:'コピペで'
}
url = qr_dict[1]

img = qrcode.make(url)
img.save('JARVIS/image/qr_image/result.png')

print_img = cv2.imread('JARVIS/image/qr_image/result.png')
cv2.imshow('qr_image', print_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
