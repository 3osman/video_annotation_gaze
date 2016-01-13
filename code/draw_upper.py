'''
process upper body data by moving point to center, and ignore with lower score 
'''
#from PIL import Image, ImageFont, ImageDraw
import collections
d = {}
dd = {}
with open("../detectors/new_upper_sub.txt", "r") as ins:
	for line in ins:
		key = int(line.split(" ")[0])
		
		value = line.partition(" ")[2].split("\r")[0].split("\n")[0]
		if key in d:
			d[key].append(value)
		else:
			d[key] = []
			d[key].append(value)
import os  
f = open('../detectors/processed_upper.txt','w')
for new_ind in range(9402,9758):
	#new_ind = int(fn.split(".")[0].split("frame")[1].split("_")[0]) + 9401
	for box in d[new_ind]:
				#print int(box.split(" ")[4].split(".")[0])
				#print(float(box.split(" ")[5]))
		if float(box.split(" ")[5]) > -1:
			#print(float(box.split(" ")[5]))
			#print(new_ind)
			#print(int(fn.split(".")[0].split("frame")[1].split("_")[0]))
			top_x = int(box.split(" ")[0].split(".")[0])
			top_y = int(box.split(" ")[1].split(".")[0])
			bottom_x = int(box.split(" ")[2].split(".")[0])
			bottom_y = int(box.split(" ")[3].split(".")[0])

			w = str(bottom_x - top_x)
			h = str(bottom_y - top_y)
			center_x = int(box.split(" ")[0].split(".")[0]) + float(w)/2
			center_y = int(box.split(" ")[1].split(".")[0]) + float(h)/2
			score = str(2.0+float(box.split(" ")[5]))
			
				

			#if top_x > 0 and top_y > 0 and bottom_x > 0 and bottom_y > 0:
			value = str(center_x) +','+str(center_y)+','+w+','+h+","+score
		
			if new_ind in dd:

				dd[new_ind].append(value)
			else:
				dd[new_ind] = []
				dd[new_ind].append(value)
						#dr.rectangle(((top_x,top_y),(bottom_x,bottom_y)), fill=(255, 255, 255, 0), outline = "red")
			#print("==================")
#			im.save("out/"+fn.split(".")[0]+"_out.png")

#try:
#	for fn in os.listdir('.'):
#		if fn != "draw_upper.py" and fn!= "gaze_sub.txt" and os.path.isfile(fn):
			#print(fn)
			#im = Image.open(fn)
			#dr = ImageDraw.Draw(im, 'RGBA')
#			dddd = int(fn.split(".")[0].split("frame")[1].split("_")[0])
#			if(dddd==1):
#				print(int(fn.split(".")[0].split("frame")[1].split("_")[0]))
#			new_ind = int(fn.split(".")[0].split("frame")[1].split("_")[0]) + 9401
			
			#print new_ind
			#print fn
			#print d[str(new_ind)]
		
#			for box in d[new_ind]:
				#print int(box.split(" ")[4].split(".")[0])
				#print(float(box.split(" ")[5]))
#				if float(box.split(" ")[5]) > -1:
					#print(float(box.split(" ")[5]))
					#print(new_ind)
					#print(int(fn.split(".")[0].split("frame")[1].split("_")[0]))
#					top_x = int(box.split(" ")[0].split(".")[0])
#					top_y = int(box.split(" ")[1].split(".")[0])
#					bottom_x = int(box.split(" ")[2].split(".")[0])
#					bottom_y = int(box.split(" ")[3].split(".")[0])
#					w = str(bottom_x - top_x)
#					h = str(bottom_y - top_y)
					
						

#					if top_x > 0 and top_y > 0 and bottom_x > 0 and bottom_y > 0:
#						value = str(top_x) +','+str(top_y)+','+w+','+h
					
#						if new_ind in dd:

#							dd[new_ind].append(value)
#						else:
#							dd[new_ind] = []
#							dd[new_ind].append(value)
						#dr.rectangle(((top_x,top_y),(bottom_x,bottom_y)), fill=(255, 255, 255, 0), outline = "red")
			#print("==================")
#			im.save("out/"+fn.split(".")[0]+"_out.png")

#except: 
#	print(fn)

od = collections.OrderedDict(sorted(dd.items()))
for k, v in dd.items():
	for val in v:
		f.write(str(k)+','+val+'\n') # python willprint k, v
#print od

f.close()

