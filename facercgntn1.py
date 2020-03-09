import face_recognition
import cv2
import PIL.Image
import PIL.ImageDraw
known_image = face_recognition.load_image_file("s1.jpeg")
unknown_image = face_recognition.load_image_file("s2.jpeg")
face_locations = face_recognition.face_locations(unknown_image) # detects all the faces in image
t = len(face_locations)
print(len(face_locations))
print(face_locations)
k=[]
biden_encoding = face_recognition.face_encodings(known_image)[0]
# storing the encodings of faces in unknown image in a list
for i in range(t) :		
	unknown_encoding = face_recognition.face_encodings(unknown_image)[i]
	k.append(unknown_encoding)
	#k.append()	
r = face_recognition.compare_faces(k, biden_encoding,tolerance=0.45)
print(r)
if(True in r):
	print("Present")
else :
	print("Not present")	
	
	



