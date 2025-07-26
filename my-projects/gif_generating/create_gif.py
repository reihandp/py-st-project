
import imageio.v3 as iio  # using version 3 of the imageio library.

filenames = [
    rf"C:\Users\reiha\OneDrive\Desktop\gif_generating\image_sample\nyan-cat{i}.png"
    for i in range(1, 4)
]
images = []

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('nyan-cat.gif', images, duration = 250, loop = 0)
