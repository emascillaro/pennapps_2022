import csv
from pandas import *

def GetMaterialTypes():
    data = read_csv('material_sustainability.csv')
    materials = data['Material'].tolist()
    for i in range(len(materials)):
        materials[i] = materials[i].lower()
    return materials

def MaterialsInItem(material_list, tag_string):

    material_content = []
    n = 0
    while n < len(material_list):
        item_present = tag_string.find(material_list[n])
        if item_present >= 0:
            material_content.append(material_list[n])
        n+=1
    return material_content
