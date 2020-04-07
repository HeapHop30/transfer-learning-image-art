from Project import Project
from logger import logging
from comet_ml import Experiment
from PIL import Image
import matplotlib.pyplot as plt

from data_processing.transformations import preprocessing, postprocessing

project = Project()

hyperparams = {}

# # --- Set up Comet ml experiment
# experiment = Experiment(project_name=project.name)
# experiment.log_parameters(hyperparams)

 # --- Import images
images = {
    'content_img': Image.open(fp=str(project.content_img_path)),
    'style_img': Image.open(fp=str(project.style_img_path))
}
# plt.imshow(images['style_img'])
# plt.show()

# --- Preprocessing images
images['content_img'] = preprocessing(images['content_img'])
images['style_img'] = preprocessing(images['style_img'])

print(images['content_img'].size())
print(images['style_img'].size())


plt.imshow(postprocessing(images['style_img']))
plt.show()



