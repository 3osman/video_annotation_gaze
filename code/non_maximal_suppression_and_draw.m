%code for performing non maximal suppression on upper body data and drawing
%on images to check

%shape = rectangles 
%BorderColor = custom
%CustomBorderColor = uint8([255 0 0])
%lineWidth = 5
shapeInserter = vision.ShapeInserter('Shape','Rectangles','BorderColor','Custom', 'CustomBorderColor', uint8([255 0 0]),'LineWidth', 3);


for i=1:510
    index = sprintf('%04d',i); 
   % disp(index);
    path = strcat('/home/osman/Documents/CMOT ver1.3/Sequences/scrubs/frame_',index,'.jpg');
    disp(path);
    I = imread(path);
   % x = 300;
   % y = 250;
   % w = 550;
   % h = 550;
    % [x y width height].
   % for j=1:size(detections(i+1))
    or_x = all{i}(:,1);
    or_y = all{i}(:,2);
    w = all{i}(:,3);
    h = all{i}(:,4);
   % or_x = detections(i+1).x(:) - (detections(i+1).w(:)/2);
    %or_y = detections(i+1).y(:) - (detections(i+1).h(:)/2);
    %rectangle = int32([or_x or_y detections(i+1).w(:) detections(i+1).h(:)]);
    rectangle = int32([or_x or_y w h]);

    J = step(shapeInserter, I, rectangle);
    %end
    imwrite(J,strcat('/home/osman/Documents/CMOT ver1.3/Sequences/with_bounding/sedit_image_',index,'.jpg'));
end