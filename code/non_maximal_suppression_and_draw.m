%code for performing non maximal suppression on upper body data and drawing
%on images to check

%shape = rectangles 
%BorderColor = custom
%CustomBorderColor = uint8([255 0 0])
%lineWidth = 5
selectedBboxes = {};
for i=9402:9757
    disp(size(processedupper(processedupper(:,1)==i,2:5)))
    [selectedBbox, selectedScore, index] = selectStrongestBbox(processedupper(processedupper(:,1)==i,2:5), processedupper(processedupper(:,1)==i,6),'OverlapThreshold',0.2, 'RatioType','min');
    selectedBboxes{i-9401} = selectedBbox;
end
shapeInserter = vision.ShapeInserter('Shape','Rectangles','BorderColor','Custom', 'CustomBorderColor', uint8([255 0 0]),'LineWidth', 3);


for i=1:353
    index = sprintf('%04d',i); 
   % disp(index);
    path = strcat('/home/osman/Dropbox/HCID Master/2nd Year - Aalto/Research Project/data/subdata/new_data_app/frames/frame_',index,'.jpg');
    disp(path);
    I = imread(path);
   % x = 300;
   % y = 250;
   % w = 550;
   % h = 550;
    % [x y width height].
   % for j=1:size(detections(i+1))
    
    w = selectedBboxes{i}(:,3);
    h = selectedBboxes{i}(:,4);
    or_x = selectedBboxes{i}(:,1) - w/2;
    or_y = selectedBboxes{i}(:,2) - h/2;
   % or_x = detections(i+1).x(:) - (detections(i+1).w(:)/2);
    %or_y = detections(i+1).y(:) - (detections(i+1).h(:)/2);
    %rectangle = int32([or_x or_y detections(i+1).w(:) detections(i+1).h(:)]);
    rectangle = int32([or_x or_y w h]);

    J = step(shapeInserter, I, rectangle);
    %end
    imwrite(J,strcat('/home/osman/Dropbox/HCID Master/2nd Year - Aalto/Research Project/data/subdata/new_data_app/frames/sedit_image_',index,'.jpg'));
end