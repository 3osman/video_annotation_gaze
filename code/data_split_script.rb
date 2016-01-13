=begin

Just to split data of raw gaze to required frame numbers
=end

ff = File.open("new_gaze_sub.txt", "w")


found_first = false
found_end = false
File.open("gaze.txt", "r") do |f|
  f.each_line do |line|
  	if line.include?"376080"
  		found_first = true
  		ff.write line
  	elsif line.include?"390320"
  		found_end = true
  		break
  	
  	elsif found_first && !found_end
  		ff.write line
  	end
    
  end
end


ff.close