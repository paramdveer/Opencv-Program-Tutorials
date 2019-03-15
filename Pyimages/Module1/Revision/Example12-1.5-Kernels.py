"""
Kernels:
Well if we think of an image as a big matrix, then we can think of a kernel or convolutional matrix as a tiny matrix
that is used for blurring, sharpening, edge detection, and other image processing functions
Essentially, this tiny kernel sits on top of the big image and slides from left to right and up to down,
applying a mathematical operation at each (x, y)-coordinate in the original image. Again, by applying kernels to images
we are able to blur and sharpen them, similar to if we were editing an image in Photoshop
Objective:
1>    A high level understanding of what kernels are and what they can be used to accomplish.
2>    An understanding of the term convolution and how we convolve images with kernels.

Kernels can be an arbitrary size of M \times N pixels, provided that both M and N are odd integers.
Why do both M and N need to be odd?
we use odd kernel sizes — to always ensure there is a valid (x, y)-coordinate at the center of the kernel.

Convolution:
convolution requires three components
    1> An input image.
    2> A kernel matrix that we are going to apply to the input image.
    3> An output image to store the output of the input image convolved with the kernel.
Process of Convolution:
1>    Select an (x, y)-coordinate from the original image.
2>    Place the center of the kernel at this (x, y) coordinate.
3>    Multiply each kernel value by the corresponding input image pixel value — and then take the sum of all
      multiplication operations. (More simply put, we’re taking the element-wise multiplication of the input image
      region and the kernel, then summing the values of all these multiplications into a single value.
      The sum of these multiplications is called the kernel output.)
4>    Use the same (x, y)-coordinate from Step 1, but this time store the kernel output in the same (x, y)-location as
      the output image.



"""