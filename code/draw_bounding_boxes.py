'''
process face data by moving point to center 
'''

#from PIL import Image, ImageFont, ImageDraw
import collections
d = {}
dd = {}
with open("../detectors/new_face_sub.txt", "r") as ins:
	for line in ins:
		key = int(line.split(".")[0])
		value = line.partition(" ")[2].split("\r")[0].replace("\n","")
		if key in d:
			d[key].append(value)
		else:
			d[key] = []
			d[key].append(value)

k = 0
#print(d)
f = open('../detectors/processed_face.txt','w')
for new_ind in range(9402,9758):
	key = new_ind
	#print new_ind
	#print(fn)
	#print d[str(new_ind)]
	print("==================")
	#i =0 
	for box in d[new_ind]:
		#i = i + 1
		top_x = float(box.split(" ")[0])
		top_y = float(box.split(" ")[1])
		w=float(box.split(" ")[2])
		h=float(box.split(" ")[3])
		center_x = top_x + w/2
		center_y = top_y + h/2
		if w!=0 and h!=0:
			value = str(center_x) +','+str(center_y)+','+str(w)+','+str(h)
			#bottom_x = int(box.split(" ")[2]) + top_x
			#bottom_y = int(box.split(" ")[3]) + top_y
			if key in dd:

				dd[key].append(value)
			else:
				dd[key] = []
				dd[key].append(value)

	#print(i)

#try:


#	import os  
#	for fn in os.listdir('.'):
#		if os.path.isfile(fn) and fn != "draw_bounding_boxes.py":

			#im = Image.open(fn)
			#dr = ImageDraw.Draw(im, 'RGBA')

#			new_ind = int(fn.split(".")[0].split("frame")[1]) + 9401
#			key = new_ind
			#print new_ind
#			print(fn)
#			#print d[str(new_ind)]
#			print("==================")
#			i =0 
#			for box in d[str(new_ind)]:
#				i = i + 1
#				top_x = box.split(" ")[0]
#				top_y = box.split(" ")[1]
#				value = top_x +','+top_y+','+box.split(" ")[2]+','+box.split(" ")[3]
				#bottom_x = int(box.split(" ")[2]) + top_x
				#bottom_y = int(box.split(" ")[3]) + top_y
#				if key in dd:
#
#					dd[key].append(value)
#				else:
#					dd[key] = []
#					dd[key].append(value)

#			print(i)
				#dr.rectangle(((top_x,top_y),(bottom_x,bottom_y)), fill=(255, 255, 255, 0), outline = "blue")
			#im.save("out/"+fn.split(".")[0]+"_out.png")

#except: 
#	pass
#od = collections.OrderedDict(sorted(dd.items()))
od = collections.OrderedDict(sorted(dd.items()))
for k, v in dd.items():
	for val in v:
		f.write(str(k)+','+val+'\n') # python willprint k, v
#print od

f.close()

