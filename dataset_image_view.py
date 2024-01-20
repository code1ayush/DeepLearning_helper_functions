# Let's view the images of our datasets
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

# let's make a function
def view_random_image(target_dir,target_class):
  #set up target directory
  target_folder = target_dir+target_class

  # get random image path
  random_image = random.sample(os.listdir(target_folder),1)

  # read in the image and plot it using matplotlib
  img=mpimg.imread(target_folder+"/"+random_image[0])  # mpimg.imread is used for reading the image
  plt.figure(figsize=(5,3))
  plt.imshow(img)                                      #for showing the image
  plt.title(target_class)
  plt.axis("off");

  print(f"image shape:{img.shape}")
  return img