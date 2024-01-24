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




# let's see by passing random images through it
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import random

target_class = random.choice(train_data_1.class_names)
target_dir = "10_food_classes_1_percent/train"+"/"+target_class
random_image = random.choice(os.listdir(target_dir))
random_img_path = target_dir+"/"+random_image
img = mpimg.imread(random_img_path)
plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.imshow(img)
plt.axis(False)
plt.title(f"orginal_image of {target_class}")
img = data_augmentation(tf.expand_dims(img,axis=0))
plt.subplot(1,2,2)
plt.imshow(tf.squeeze(img)/255.)
plt.axis(False)
plt.title(f"augmented image of {target_class}")