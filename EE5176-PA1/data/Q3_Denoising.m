load('bayer1.mat', 'bayer1');
load('RawImage1.mat', 'RawImage1');
load('bayer2.mat', 'bayer2');
load('RawImage2.mat', 'RawImage2');
load('bayer3.mat', 'bayer3');
load('RawImage3.mat', 'RawImage3');

addpath(pwd, 'bil_filter');

RGB1 = implemented_demosaic(RawImage1, bayer1, 'cubic');
RGB1 = double(RGB1)/255;
RGB1_bflt = denoise(RGB1, 1068, 1988, 1128, 2048);
figure;
subplot(1,2,1), imshow(RGB1);
title('Original');
subplot(1,2,2), imshow(RGB1_bflt);
title('Denoised');
sgtitle('Raw Image 1');

RGB2 = implemented_demosaic(RawImage2, bayer2, 'cubic');
RGB2 = double(RGB2)/255;
RGB2_bflt = denoise(RGB2, 705, 924, 765, 984);
figure;
subplot(1,2,1), imshow(RGB2);
title('Original');
subplot(1,2,2), imshow(RGB2_bflt);
title('Denoised');
sgtitle('Raw Image 2');

RGB3 = implemented_demosaic(RawImage3, bayer3, 'cubic');
RGB3 = double(RGB3)/255;
RGB3_bflt = denoise(RGB3, 1, 1, 60, 60);
figure;
subplot(1,2,1), imshow(RGB3);
title('Original');
subplot(1,2,2), imshow(RGB3_bflt);
title('Denoised');
sgtitle('Raw Image 3');

function RGB_out = denoise(RGB, X1, Y1, X2, Y2)
    R_ch = RGB(:,:,1);
    G_ch = RGB(:,:,2);
    B_ch = RGB(:,:,3);

    R_ch = process_channel(R_ch, X1, Y1, X2, Y2);
    G_ch = process_channel(G_ch, X1, Y1, X2, Y2);
    B_ch = process_channel(B_ch, X1, Y1, X2, Y2);

    RGB_out = cat(3, R_ch, G_ch, B_ch);
end

function ch_out = process_channel(ch, X1, Y1, X2, Y2)
    sigma_n = std(ch(X1:X2, Y1:Y2), 0, 'all');
    sigma_r = 1.95*sigma_n;
    sigma_s = 2.5;

    ch_out = bfilter2(ch, 5, [sigma_s sigma_r]);
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