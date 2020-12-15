import pandas as pd 
import numpy as np
import xml.etree.ElementTree as ET 
import os

def createDatabase(directory, itemDictionary):
    
    x = 0
    
    for folder in os.listdir(directory):
        
        if folder != "monsters.xml":
            for fileName in os.listdir(directory+f'/{folder}'):
                if fileName.endswith('xml') == False:
                    for fileMisc in os.listdir(directory+f'/{folder}/{fileName}'):
                        fileDirectory = directory + f'/{folder}/{fileName}/{fileMisc}'
                        itemDictionary = parseXML(fileDirectory, monsterGroup= fileName, itemDictionary = itemDictionary)      
                else:
                    fileDirectory = directory + f'/{folder}/{fileName}'
                    itemDictionary = parseXML(fileDirectory, monsterGroup= folder, itemDictionary = itemDictionary)
    return(itemDictionary)

def parseXML(fileDirectory, monsterGroup, itemDictionary):
    t=0
    root = ET.parse(fileDirectory).getroot()
    name = root.get('name')
    race = root.get('race')
    experience = root.get('experience')
    speed = root.get('speed')
    for type_tag in root.findall('health'):
        HP = type_tag.get('max')
    for items in root.findall('loot'):
        for item in items.findall('item'):
            if item.get('name') not in itemDictionary:
                itemDictionary[item.get('name')] = 1
            else:
                t = itemDictionary[item.get('name')]
                itemDictionary.update({item.get('name'): t+1})
    return itemDictionary
    
itemDictionary = {}

l = createDatabase(r'C:\Users\hhams\Desktop\Tibia_MG\monster', itemDictionary)

print(l)


# for item in l:
#     itemDictionary[item] = 0

