from image_capture import capture_image
from clothing_tag import image_to_text_string
from material_data import GetMaterialTypes, MaterialsInItem


capture_image()
tag_string = image_to_text_string()
print(f"tag string: {tag_string}")

material_list = GetMaterialTypes()
print(f"Materials In Item: {MaterialsInItem(material_list, tag_string)}")