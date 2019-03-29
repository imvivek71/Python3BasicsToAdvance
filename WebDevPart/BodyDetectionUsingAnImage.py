
import cv2, requests, base64
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaXJzdG5hbWUiOiJWaXZlayIsInVzZXJuYW1lIjoiaW12aXZlayIsImVtYWlsIjoidml2ZWtnb3N3YW1pNzFAZ21haWwuY29tIn0.VbwwpbhAx99zWOFWhp-1Htr1e_0z_NO-1gt13FGdLb0"
secret = "9cdcee1d4dd07b4f206742c048792eb9"


imgPath  =("vivek.jpeg")

img = open(imgPath, 'rb')
img = img.read()

img_enc = base64.b64encode(img)
img_enc = img_enc.decode('utf-8')

re = requests.post('http://api.giscle.ml/body_detection', data={'image': img_enc}, headers={'token': token})

if re.ok:
    print(re.json())
    r = re.json()
    if r['data']['total_person'] > 6:
        print('Warning more than 6 person')
    frame = cv2.imread(imgPath)
    for key in r['data'].keys():
        if key != 'total_person':
            x, y, h, w = (r['data'][str(key)])
            x, y, h, w = int(x), int(y), int(h), int(w)
            cv2.rectangle(frame, (x, y), (x + h, y + w), (255, 0, 0))
    while True:
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
