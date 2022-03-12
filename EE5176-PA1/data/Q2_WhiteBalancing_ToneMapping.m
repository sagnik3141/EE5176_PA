load('bayer1.mat', 'bayer1');
load('RawImage1.mat', 'RawImage1');
load('bayer2.mat', 'bayer2');
load('RawImage2.mat', 'RawImage2');
load('bayer3.mat', 'bayer3');
load('RawImage3.mat', 'RawImage3');

RGB1 = implemented_demosaic(RawImage1, bayer1, 'cubic');
RGB2 = implemented_demosaic(RawImage2, bayer2, 'cubic');
RGB3 = implemented_demosaic(RawImage3, bayer3, 'cubic');

RGB1_wb_gray = uint8(white_balance_gray(double(RGB1)));
RGB1_wb_gray_histeq = histeq(RGB1_wb_gray);
RGB1_wb_gray_gamma5 = uint8(255*imadjust(double(RGB1_wb_gray)/255,[0 1],[0 1],0.5));
RGB1_wb_gray_gamma7 = uint8(255*imadjust(double(RGB1_wb_gray)/255,[0 1],[0 1],0.7));
RGB1_wb_gray_gamma9 = uint8(255*imadjust(double(RGB1_wb_gray)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB1);
title('Original RGB');
subplot(2,3,2), imshow(RGB1_wb_gray);
title('White Balanced');
subplot(2,3,3), imshow(RGB1_wb_gray_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB1_wb_gray_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB1_wb_gray_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB1_wb_gray_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 1 using Gray Assumption');

RGB2_wb_gray = uint8(white_balance_gray(double(RGB2)));
RGB2_wb_gray_histeq = histeq(RGB2_wb_gray);
RGB2_wb_gray_gamma5 = uint8(255*imadjust(double(RGB2_wb_gray)/255,[0 1],[0 1],0.5));
RGB2_wb_gray_gamma7 = uint8(255*imadjust(double(RGB2_wb_gray)/255,[0 1],[0 1],0.7));
RGB2_wb_gray_gamma9 = uint8(255*imadjust(double(RGB2_wb_gray)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB2);
title('Original RGB');
subplot(2,3,2), imshow(RGB2_wb_gray);
title('White Balanced');
subplot(2,3,3), imshow(RGB2_wb_gray_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB2_wb_gray_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB2_wb_gray_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB2_wb_gray_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 2 using Gray Assumption');

RGB3_wb_gray = uint8(white_balance_gray(double(RGB3)));
RGB3_wb_gray_histeq = histeq(RGB3_wb_gray);
RGB3_wb_gray_gamma5 = uint8(255*imadjust(double(RGB3_wb_gray)/255,[0 1],[0 1],0.5));
RGB3_wb_gray_gamma7 = uint8(255*imadjust(double(RGB3_wb_gray)/255,[0 1],[0 1],0.7));
RGB3_wb_gray_gamma9 = uint8(255*imadjust(double(RGB3_wb_gray)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB3);
title('Original RGB');
subplot(2,3,2), imshow(RGB3_wb_gray);
title('White Balanced');
subplot(2,3,3), imshow(RGB3_wb_gray_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB3_wb_gray_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB3_wb_gray_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB3_wb_gray_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 3 using Gray Assumption');

RGB1_wb_spec_highlight = uint8(white_balance_spec_highlight(double(RGB1), 814, 830));
RGB1_wb_spec_highlight_histeq = histeq(RGB1_wb_spec_highlight);
RGB1_wb_spec_highlight_gamma5 = uint8(255*imadjust(double(RGB1_wb_spec_highlight)/255,[0 1],[0 1],0.5));
RGB1_wb_spec_highlight_gamma7 = uint8(255*imadjust(double(RGB1_wb_spec_highlight)/255,[0 1],[0 1],0.7));
RGB1_wb_spec_highlight_gamma9 = uint8(255*imadjust(double(RGB1_wb_spec_highlight)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB1);
title('Original RGB');
subplot(2,3,2), imshow(RGB1_wb_spec_highlight);
title('White Balanced');
subplot(2,3,3), imshow(RGB1_wb_spec_highlight_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB1_wb_spec_highlight_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB1_wb_spec_highlight_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB1_wb_spec_highlight_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 1 using Specular Highlight');

RGB2_wb_spec_highlight = uint8(white_balance_spec_highlight(double(RGB2), 280, 1165));
RGB2_wb_spec_highlight_histeq = histeq(RGB2_wb_spec_highlight);
RGB2_wb_spec_highlight_gamma5 = uint8(255*imadjust(double(RGB2_wb_spec_highlight)/255,[0 1],[0 1],0.5));
RGB2_wb_spec_highlight_gamma7 = uint8(255*imadjust(double(RGB2_wb_spec_highlight)/255,[0 1],[0 1],0.7));
RGB2_wb_spec_highlight_gamma9 = uint8(255*imadjust(double(RGB2_wb_spec_highlight)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB2);
title('Original RGB');
subplot(2,3,2), imshow(RGB2_wb_spec_highlight);
title('White Balanced');
subplot(2,3,3), imshow(RGB2_wb_spec_highlight_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB2_wb_spec_highlight_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB2_wb_spec_highlight_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB2_wb_spec_highlight_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 2 using Specular Highlight');

RGB3_wb_spec_highlight = uint8(white_balance_spec_highlight(double(RGB3), 675, 175));
RGB3_wb_spec_highlight_histeq = histeq(RGB3_wb_spec_highlight);
RGB3_wb_spec_highlight_gamma5 = uint8(255*imadjust(double(RGB3_wb_spec_highlight)/255,[0 1],[0 1],0.5));
RGB3_wb_spec_highlight_gamma7 = uint8(255*imadjust(double(RGB3_wb_spec_highlight)/255,[0 1],[0 1],0.7));
RGB3_wb_spec_highlight_gamma9 = uint8(255*imadjust(double(RGB3_wb_spec_highlight)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB3);
title('Original RGB');
subplot(2,3,2), imshow(RGB3_wb_spec_highlight);
title('White Balanced');
subplot(2,3,3), imshow(RGB3_wb_spec_highlight_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB3_wb_spec_highlight_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB3_wb_spec_highlight_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB3_wb_spec_highlight_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 3 using Specular Highlight');

RGB1_wb_neutral = uint8(white_balance_neutral(double(RGB1), 435, 2000));
RGB1_wb_neutral_histeq = histeq(RGB1_wb_neutral);
RGB1_wb_neutral_gamma5 = uint8(255*imadjust(double(RGB1_wb_neutral)/255,[0 1],[0 1],0.5));
RGB1_wb_neutral_gamma7 = uint8(255*imadjust(double(RGB1_wb_neutral)/255,[0 1],[0 1],0.7));
RGB1_wb_neutral_gamma9 = uint8(255*imadjust(double(RGB1_wb_neutral)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB1);
title('Original RGB');
subplot(2,3,2), imshow(RGB1_wb_neutral);
title('White Balanced');
subplot(2,3,3), imshow(RGB1_wb_neutral_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB1_wb_neutral_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB1_wb_neutral_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB1_wb_neutral_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 1 using Neutral Pixel');

RGB2_wb_neutral = uint8(white_balance_neutral(double(RGB2), 715, 445));
RGB2_wb_neutral_histeq = histeq(RGB2_wb_neutral);
RGB2_wb_neutral_gamma5 = uint8(255*imadjust(double(RGB2_wb_neutral)/255,[0 1],[0 1],0.5));
RGB2_wb_neutral_gamma7 = uint8(255*imadjust(double(RGB2_wb_neutral)/255,[0 1],[0 1],0.7));
RGB2_wb_neutral_gamma9 = uint8(255*imadjust(double(RGB2_wb_neutral)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB2);
title('Original RGB');
subplot(2,3,2), imshow(RGB2_wb_neutral);
title('White Balanced');
subplot(2,3,3), imshow(RGB2_wb_neutral_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB2_wb_neutral_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB2_wb_neutral_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB2_wb_neutral_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 2 using Neutral Pixel');

RGB3_wb_neutral = uint8(white_balance_neutral(double(RGB3), 565, 1550));
RGB3_wb_neutral_histeq = histeq(RGB3_wb_neutral);
RGB3_wb_neutral_gamma5 = uint8(255*imadjust(double(RGB3_wb_neutral)/255,[0 1],[0 1],0.5));
RGB3_wb_neutral_gamma7 = uint8(255*imadjust(double(RGB3_wb_neutral)/255,[0 1],[0 1],0.7));
RGB3_wb_neutral_gamma9 = uint8(255*imadjust(double(RGB3_wb_neutral)/255,[0 1],[0 1],0.9));
figure;
subplot(2,3,1), imshow(RGB3);
title('Original RGB');
subplot(2,3,2), imshow(RGB3_wb_neutral);
title('White Balanced');
subplot(2,3,3), imshow(RGB3_wb_neutral_histeq);
title('Histogram Equalized');
subplot(2,3,4), imshow(RGB3_wb_neutral_gamma5);
title('Gamma = 0.5');
subplot(2,3,5), imshow(RGB3_wb_neutral_gamma7);
title('Gamma = 0.7');
subplot(2,3,6), imshow(RGB3_wb_neutral_gamma9);
title('Gamma = 0.9');
sgtitle('Raw Image 3 using Neutral Pixel');

function RGB_white_balanced_neutral = white_balance_neutral(RGB, X, Y)
    R_val = RGB(X, Y, 1);
    G_val = RGB(X, Y, 2);
    B_val = RGB(X, Y, 3);

    S_R = (R_val+G_val+B_val)/(3*R_val);
    S_G = (R_val+G_val+B_val)/(3*G_val);
    S_B = (R_val+G_val+B_val)/(3*B_val);

    R_c = RGB(:,:,1)*S_R;
    G_c = RGB(:,:,2)*S_G;
    B_c = RGB(:,:,3)*S_B;

    RGB_white_balanced_neutral = cat(3, R_c, G_c, B_c);
end

function RGB_white_balanced_spec = white_balance_spec_highlight(RGB, specular_highlight_X, specular_highlight_Y)
    R = RGB(specular_highlight_X, specular_highlight_Y, 1);
    G = RGB(specular_highlight_X, specular_highlight_Y, 2);
    B = RGB(specular_highlight_X, specular_highlight_Y, 3);
    
    R_ch = RGB(:,:,1)*(255/R);
    G_ch = RGB(:,:,2)*(255/G);
    B_ch = RGB(:,:,2)*(255/B);

    RGB_white_balanced_spec = cat(3, R_ch, G_ch, B_ch);
end

function RGB_white_balanced_gray = white_balance_gray(RGB)
    total_sum = sum(RGB, 'all');
    sum_R = sum(RGB(:,:,1), 'all');
    sum_G = sum(RGB(:,:,2), 'all');
    sum_B = sum(RGB(:,:,3), 'all');

    R_channel = RGB(:,:,1)*(total_sum/(3*sum_R));
    G_channel = RGB(:,:,2)*(total_sum/(3*sum_G));
    B_channel = RGB(:,:,3)*(total_sum/(3*sum_B));

    RGB_white_balanced_gray = cat(3, R_channel, G_channel, B_channel);
end

function RGB = implemented_demosaic(raw_img, bayer, method)
    red_channel = interpolation(raw_img, bayer, 1, method);
    green_channel = interpolation(raw_img, bayer, 2, method);
    blue_channel = interpolation(raw_img, bayer, 3, method);

    RGB = cat(3, red_channel, green_channel, blue_channel);
end

function channel = interpolation(raw_img, bayer, channel_num, method)
    channel = raw_img(bayer==channel_num);
    [x, y] = meshgrid(1:size(raw_img, 2), 1:size(raw_img, 1));

    xv = x(bayer == channel_num);
    yv = y(bayer == channel_num);

    channel = uint8(griddata(xv, yv, double(channel), x, y, method));
    channel = reshape(channel, size(raw_img));
end