# Angela R. Ayala
# Reference: https://stackoverflow.com/questions/58489007/how-to-add-salt-and-pepper-noise-to-all-images-in-a-folder-in-python
#           https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv
#           https://www.geeksforgeeks.org/python-noise-function-in-wand/
# Types of noise to add:
#                       'gaussian'
#                       'impulse'
#                       'laplacian'
#                       'multiplicative_gaussian'
#                       'poisson'
#                       'random'
#                       'uniform'

from wand.image import Image
import glob
import sys

image_list = []

if __name__ == '__main__':
    noise_type = sys.argv[1]
    score = sys.argv[2]

# open files
for filename in glob.glob('/Users/ayala/Documents/4COMP_195 CS Senior Project/Data Sets/Emergency_Vehicles_test_file/obj/*.jpg'):
    img = Image.open(filename)

    # adding noise
    if noise_type == "gaussian":
        img.noise("gaussian", attenuate=score)
    elif noise_type == "impulse":
        img.noise("impulse", attenuate=score)
    elif noise_type == "laplacian":
        img.noise("laplacian", attenuate=score)
    elif noise_type == "multiplicative_gaussian":
        img.noise("multiplicative_gaussian", attenuate=score)
    elif noise_type == "poisson":
        img.noise("poisson", attenuate=score)
    elif noise_type == "random":
        img.noise("random", attenuate=score)
    elif noise_type == "uniform":
        img.noise("uniform", attenuate=score)
    else:
        img.noise("gaussian", attenuate=score)

    # save image back inside the loop
    imgNumber == 0
    filename = "images/file_%d.jpg" % imgNumber
    img.save(filename)
    imgNumber += 1