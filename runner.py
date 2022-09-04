from take_image_interface import CaptureImage, ShowFrame
from clothing_tag import ImageToTextString
from material_data import GetMaterialTypes, MaterialsInItem
from interface import CreateDisplay


tag_string = ImageToTextString()

material_list = GetMaterialTypes()
materials_present = MaterialsInItem(material_list, tag_string)
print(f"materials present: {materials_present}")

CreateDisplay(materials_present)