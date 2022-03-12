load('bayer1.mat', 'bayer1');
load('RawImage1.mat', 'RawImage1');
load('kodim19.mat', 'raw');
kodim_raw = uint8(raw);
load('kodim_cfa.mat', 'cfa');
kodim_cfa = cfa;

RGB_bilinear = implemented_demosaic(RawImage1, bayer1, 'linear');
figure, imshow(RGB_bilinear);
title('Bilinear Interpolation');

RGB_bicubic = implemented_demosaic(RawImage1, bayer1, 'cubic');
figure, imshow(RGB_bicubic);
title('Bicubic Interpolation')

RGB_builtin = demosaic(RawImage1, 'rggb');
figure, imshow(RGB_builtin);
title('MATLAB Demosaic Function');

RGB_kodim = implemented_demosaic(kodim_raw, kodim_cfa, 'cubic');

RGB_kodim_medfilt = median_filter(RGB_kodim, 15);
figure;
subplot(1,3,1), imshow(RGB_kodim);
title('Demosaiced Image');
subplot(1,3,2), imshow(RGB_kodim_medfilt);
title('Median Filtered');
subplot(1,3,3), imshow('kodim19.png');
title('Reference Image');

function RGB_out = median_filter(RGB, filter_size)
    YCBCR = rgb2ycbcr(RGB);
    Y = YCBCR(:,:,1);
    CB = YCBCR(:,:,2);
    CR = YCBCR(:,:,3);
    CB = medfilt2(CB, [filter_size filter_size], 'symmetric');
    CR = medfilt2(CR, [filter_size filter_size], 'symmetric');
    YCBCR = cat(3, Y, CB, CR);
    RGB_out = ycbcr2rgb(YCBCR);
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