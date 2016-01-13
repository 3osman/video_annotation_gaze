'''
process gaze data by moving point to center 
'''
d = {}
d_fix = {}
fixation_data = []
frames_fixation = []
f_found = False
dd = {}
import collections
with open("../detectors/new_gaze_sub.txt", "r") as ins:
	for line in ins:
		key = line.split(" ")[1].split(".")[0]
		value = line.partition(" ")[2].partition(" ")[2].partition(" ")[2].split("\r")[0]
		if line.split(" ")[0] == "F_Begin":
			f_found = True
			if key not in frames_fixation:
				frames_fixation.append(key)
			fixation_data.append(value)
		elif line.split(" ")[0] == "F_End":
			f_found = False
			if key not in frames_fixation:
				frames_fixation.append(key)
			fixation_data.append(value)
			#print frames_fixation
			
			sum_x = 0
			sum_y = 0
			for ob in fixation_data:
				sum_x = sum_x + int(ob.split(" ")[0].split(".")[0])
				sum_y = sum_y + int(ob.split(" ")[1].split(".")[0])
			#print sum_x/len(fixation_data)
			#print sum_y/len(fixation_data)
			for fr in frames_fixation:
				#print fr
				if fr in d_fix:
					#print str(sum_x/len(fixation_data))+" "+str(sum_y/len(fixation_data))
					d_fix[fr].append(str(sum_x/len(fixation_data))+" "+str(sum_y/len(fixation_data)))
				else:
					#print str(sum_x/len(fixation_data))+" "+str(sum_y/len(fixation_data))

					d_fix[fr] = []
					d_fix[fr].append(str(sum_x/len(fixation_data))+" "+str(sum_y/len(fixation_data)))
			fixation_data = []
			#print "========================"

			frames_fixation = []
		elif f_found:
			
			if key not in frames_fixation:
				frames_fixation.append(key)
			fixation_data.append(value)
		else:
			if key in d:
				d[key].append(value)
			else:
				d[key] = []
				d[key].append(value)

import os  
try:
	for fn in range(9402,9758):
		#if os.path.isfile(fn) and fn != "gaze.py":

			#im = Image.open(fn)
			#dr = ImageDraw.Draw(im, 'RGBA')

		new_ind = fn*40
		print new_ind
		print "========================="
		#print(new_ind/40)
	
		#print new_ind
		#print fn
		#print d[str(new_ind)]
		#print "=================="
		if str(new_ind) in d:
			for box in d[str(new_ind)]:

				x = (int(box.split(" ")[0].split(".")[0]) * 768) / 1280
				y = (int(box.split(" ")[1].split(".")[0]) * 576) / 1024
			
				#dr.rectangle(((x-5,y-5),(x+5,y+5)), fill=(255, 255, 255, 0), outline = "green")
		if str(new_ind) in d_fix:		
			for box in d_fix[str(new_ind)]:

				x = (int(box.split(" ")[0].split(".")[0]) * 768) / 1280
				y = (int(box.split(" ")[1].split(".")[0]) * 576) / 1024

				value = str(x) +','+str(y)
				new_indc = new_ind/40
				if new_indc in dd:

					dd[new_indc].append(value)
				else:
					dd[new_indc] = []
					dd[new_indc].append(value)
					#dr.rectangle(((x-5,y-5),(x+5,y+5)), fill=(255, 255, 255, 0), outline = "yellow")
			#number = "%03d"%int(fn.split(".")[0].split("frame")[1].split("_")[0])
			#im.save("out/img"+number+".png")
except Exception:
	pass
od = collections.OrderedDict(sorted(dd.items()))

f = open('../detectors/processed_gaze.txt','w')
for k, v in od.items():
	for val in v:
		f.write(str(k)+','+val+'\n') # python willprint k, v
#print od

f.close()



