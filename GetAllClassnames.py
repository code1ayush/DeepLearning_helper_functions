# Get the class names programatically
import pathlib
import numpy as np
data_dir = pathlib.Path("pizza_steak/train/") # turn our training path to python path
class_names = np.array([item.name for item in data_dir.glob('*')])
print(class_names)



