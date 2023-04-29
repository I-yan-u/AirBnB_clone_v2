#!/usr/bin/python3

classes = {
            'BaseModel': 1, 'User': 2, 'Place': 3,
            'State': 4, 'City': 5, 'Amenity': 6,
            'Review': 7
          }

for clss in classes:
	print(clss, type(clss))


print(type(classes.keys()))