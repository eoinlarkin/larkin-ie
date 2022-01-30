# Image Blending:


Convert Image to Grayscale
`magick image.png -colorspace gray image_grey.png`

Apply tint:
`magick rose_grey.jpg   -fill "rgba(0,71,143,0.50)" -tint 100 duotone_$color.jpg`

# Image Resizing:

`magick portfolio-magic-square-game.png -resize 200x200 portfolio-01-resize.png`