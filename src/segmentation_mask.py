import json
from PIL import Image, ImageDraw

def create_mask(annotations, image_width, image_height):
  """
  Creates a binary mask image from annotations, assigning unique indices to labels.

  Args:
      annotations: A dictionary containing annotation data.
      image_width: Width of the image.
      image_height: Height of the image.

  Returns:
      A PIL image representing the binary mask with unique labels.
  """
  mask = Image.new('L', (image_width, image_height), 0)
  draw = ImageDraw.Draw(mask)
  label_index = 1  # Start index at 1 (0 is background)
  for region in annotations.values():
    if region["shape_attributes"]["name"] != "polygon":
      continue  # Only handle polygons for now
    points = list(zip(region["shape_attributes"]["all_points_x"], region["shape_attributes"]["all_points_y"]))
    label = region["region_attributes"].get("label", None)  # Get label if available
    fill_value = label_index if label else 0  # Assign index based on label or 0 for background
    draw.polygon(points, fill=fill_value, outline=None)
    label_index += 1  # Increment index for next label
  return mask

def process_annotations(annotations_file, image_folder):
  """
  Processes annotations from a JSON file and creates binary mask images.

  Args:
      annotations_file: Path to the JSON file containing annotations.
      image_folder: Path to the folder containing images.
  """
  with open(annotations_file, 'r') as f:
    annotations_data = json.load(f)

  for filename, image_data in annotations_data.items():
    image_path = f"{image_folder}/{filename}"
    image = Image.open(image_path)
    image_width, image_height = image.size

    mask = create_mask(image_data["regions"], image_width, image_height)
    mask_filename = f"{image_folder}/mask_{filename}"
    mask.save(mask_filename)

if __name__ == "__main__":
  annotations_file = "data/labels.json"  # Replace with json file path
  image_folder = "data/Rooms/test"  # Replace with image folder path
  process_annotations(annotations_file, image_folder)