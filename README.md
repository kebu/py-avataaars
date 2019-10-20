# py-avataaars - Python component for Avataaars

Python port of https://github.com/fangpenlin/avataaars

## Features
* SVG based
* Light weight
* Easy to use

## Usage

Basic usage:

```python
from py_avataaars import PyAvataaar

avatar = PyAvataaar()
avatar.render_png_file('<output_file.png>')
```

Specify each part of avatar:
```python
import py_avataaars as pa
avatar = pa.PyAvataaar(
    style=pa.AvatarStyle.CIRCLE,
    skin_color=pa.SkinColor.LIGHT,
    hair_color=pa.HairColor.BROWN,
    facial_hair_type=pa.FacialHairType.DEFAULT,
    facial_hair_color=pa.FacialHairColor.BLACK,
    top_type=pa.TopType.SHORT_HAIR_SHORT_FLAT,
    hat_color=pa.ClotheColor.BLACK,
    mouth_type=pa.MouthType.SMILE,
    eye_type=pa.EyesType.DEFAULT,
    eyebrow_type=pa.EyebrowType.DEFAULT,
    accessories_type=pa.AccessoriesType.DEFAULT,
    clothe_type=pa.ClotheType.GRAPHIC_SHIRT,
    clothe_color=pa.ClotheColor.HEATHER,
    clothe_graphic_type=pa.ClotheGraphicType.BAT,
)
avatar.render_png_file('<output_file.png>')
```
