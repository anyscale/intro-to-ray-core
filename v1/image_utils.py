from PIL import Image
import matplotlib.pyplot as plt

# Load the image using Pillow
image_path = "debug_logs_annotated_cropped.png"
img = Image.open(image_path)

# Create a figure and axis without x and y axes
fig, ax = plt.subplots(figsize=(18, 12))
ax.axis("off")

# Display the image at full resolution
ax.imshow(img, extent=[0, img.width, 0, img.height])

# Add a legend outside the image using bbox_to_anchor with specific colors
legend_labels = [
    "Adding Task",
    "Executing Task",
    "Putting Object",
    "Reference Counting",
    "Deleting Object",
    "Finished Execution",
]
legend_colors = ["black" for _ in enumerate(legend_labels)]
legend_handles = [
    plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=color, markersize=10)
    for color in ["yellow", "orange", "green", "grey", "red", "green"]
]
legend = ax.legend(
    legend_handles,
    legend_labels,
    loc="upper left",
    bbox_to_anchor=(1, 1),
    frameon=False,
)

# Set legend label colors
for text, color in zip(legend.get_texts(), legend_colors):
    text.set_color(color)

# Show the plot (optional)
plt.show()

fig.savefig("debug_logs_with_legend.png", bbox_inches="tight", pad_inches=0)
