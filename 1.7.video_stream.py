import cv2

cap = cv2.VideoCapture(0) # 0 => pc kamerası, 1 => usb'ye bağlı kamera, 2 => 

# video'yu kaydetmek için
fourcc = cv2.VideoWriter_fourcc(*'XVID') # 4 byte'lık video codec kodu alarak int veri döndürür.
out = cv2.VideoWriter('img/output.avi', fourcc, 20.0, (640,480)) # video adı, codec code, fps, video size

while True:
    ret, frame = cap.read() # kameradan o anki görüntü okunuyor. ret => kamera çalışıp çalışmadığını döndürür.

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # frame genişliğini döndürür
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # frame yüksekliğini döndürür

    out.write(frame)
    cv2.imshow("camera",frame) # görüntü ekrana bastırılıyor.

    if cv2.waitKey(30) & 0xFF == ord('q'): # 30 ms'de bir görüntü alınıyor ve q'ya basılırsa döngüden çıkılıyor.
        break

cap.release() # kamera serbest bırakılıyor.
out.release() # kayıt çıktısı serbest bırakılıyor.
cv2.destroyAllWindows()