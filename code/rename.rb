=begin
rename image files to algorithm convention 
=end
puts "Renaming files..."

#folder_path = "/home/papuccino1/Desktop/Test"
Dir.glob("./*").sort.each do |f|
	#puts f
	if f.include?"frame"
		img_num = f.split("frame")[1].split(".")[0];
		new_img_num = sprintf '%04d',img_num
		puts new_img_num
		File.rename(f, "./" + "frame_"+ new_img_num+".jpg")

	end

    #filename = File.basename(f, File.extname(f))
    #File.rename(f, filename.capitalize + File.extname(f))
end

puts "Renaming complete."