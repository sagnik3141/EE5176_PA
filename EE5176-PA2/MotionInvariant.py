import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def main():
    ### Read Images ###
    img_fg = np.array(Image.open(r"data/redcar.png"))
    img_fg = img_fg/255.0
    img_bg = np.array(Image.open(r"data/background.png"))

if __name__=="__main__":
    main()