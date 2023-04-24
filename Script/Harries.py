def harries():
    start = time.time()
    image = image = Image.open('C:/Users/acer/Pictures/Picture/horse1.jpg').convert("L").filter(ImageFilter.BLUR)
    image.show()
    image = cv2.imread('C:/Users/acer/Pictures/Picture/horse1.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (3,3))
    zeos = np.zeros_like(gray.shape)
    dst = cv2.cornerHarris(blur,2,3,0.04)
    zeos = np.zeros_like(gray.shape)
    # Threshold for an optimal value, it may vary depending on the image.
    image[dst>0.01*dst.max()]=[255,255,255]
    image[dst<0.01*dst.max()] = [0,0,0]
    stop = time.time()
    print("Harris improved: " + str(stop - start))
    return image
  
  
