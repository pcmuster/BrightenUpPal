import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from skimage import io, exposure

image_path = input("Enter the file path of your image: ")
try:
    image = io.imread(image_path)
except FileNotFoundError:
    print("File not found. Make sure the file path is correct.")
    exit()

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.4)

image_ax = ax.imshow(image)
ax_slider = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor='green')
slider = Slider(ax_slider, label='Brightness', valmin=0.5, valmax=2.0, valinit=1.0)

ax_contrast_slider = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor='blue')
contrast_slider = Slider(ax_contrast_slider, label='Contrast', valmin=0.5, valmax=2.0, valinit=1.0)

ax_red_slider = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='red')
red_slider = Slider(ax_red_slider, label='Red Channel', valmin=0.0, valmax=2.0, valinit=1.0)

ax_green_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='green')
green_slider = Slider(ax_green_slider, label='Green Channel', valmin=0.0, valmax=2.0, valinit=1.0)

ax_blue_slider = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='blue')
blue_slider = Slider(ax_blue_slider, label='Blue Channel', valmin=0.0, valmax=2.0, valinit=1.0)

def update(val):
    brightness = slider.val
    contrast = contrast_slider.val
    red_factor = red_slider.val
    green_factor = green_slider.val
    blue_factor = blue_slider.val

    updated_image = exposure.adjust_gamma(image, gamma=1, gain=brightness)
    updated_image = exposure.adjust_gamma(updated_image, gamma=contrast, gain=1)

    # Needed to convert to float
    updated_image = updated_image.astype(float)

    updated_image[..., 0] *= red_factor
    updated_image[..., 1] *= green_factor
    updated_image[..., 2] *= blue_factor

    updated_image = np.clip(updated_image, 0, 255).astype(np.uint8)

    image_ax.set_data(updated_image)
    fig.canvas.draw_idle()

slider.on_changed(update)
contrast_slider.on_changed(update)
red_slider.on_changed(update)
green_slider.on_changed(update)
blue_slider.on_changed(update)

reset_button_ax = plt.axes([0.8, 0.01, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')

def reset(event):
    slider.reset()
    contrast_slider.reset()
    red_slider.reset()
    green_slider.reset()
    blue_slider.reset()

reset_button.on_clicked(reset)

plt.show()