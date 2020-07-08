import tempfile

import pytest

from py_avataaars import *


@pytest.fixture(scope="session")
def image_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("img.png")
    avatar = PyAvataaar(mouth_type=MouthType.SMILE, )
    avatar.render_png_file(str(fn))
    return fn


def test_create_avataaar(image_file):
    assert image_file.exists()


def test_create_all():
    attrs = dict(
        style=AvatarStyle,
        skin_color=SkinColor,
        hair_color=HairColor,
        facial_hair_type=FacialHairType,
        facial_hair_color=dict(
            facial_hair_color=FacialHairColor,
            facial_hair_type=FacialHairType.BEARD_MAJESTIC,
        ),
        top_type=TopType,
        hat_color=dict(
            hat_color=ClotheColor,
            top_type=TopType.HAT,
        ),
        mouth_type=MouthType,
        eye_type=EyesType,
        nose_type=NoseType,
        eyebrow_type=EyebrowType,
        accessories_type=AccessoriesType,
        clothe_type=ClotheType,
        clothe_color=ClotheColor,
        clothe_graphic_type=ClotheGraphicType,
    )

    with tempfile.TemporaryDirectory() as tmp_dir_name:
        for attr, value in attrs.items():
            print(f"Rendering {attr}")
            attributes = {}
            if isinstance(value, dict):
                new_value = value.pop(attr)
                attributes.update(value)
                value = new_value

            for attr_type in value:
                attributes.update({
                    attr: attr_type,
                })
                avatar = PyAvataaar(**attributes)
                avatar_file = os.path.join(tmp_dir_name, f'{attr_type.name.lower()}.png')
                avatar.render_png_file(avatar_file)
                assert os.path.exists(avatar_file)


@pytest.mark.skip
def test_create_all_locally():
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')

    attrs = dict(
        style=AvatarStyle,
        skin_color=SkinColor,
        hair_color=HairColor,
        facial_hair_type=FacialHairType,
        facial_hair_color=dict(
            facial_hair_color=FacialHairColor,
            facial_hair_type=FacialHairType.BEARD_MAJESTIC,
        ),
        top_type=TopType,
        hat_color=dict(
            hat_color=ClotheColor,
            top_type=TopType.HAT,
        ),
        mouth_type=MouthType,
        eye_type=EyesType,
        nose_type=NoseType,
        eyebrow_type=EyebrowType,
        accessories_type=AccessoriesType,
        clothe_type=ClotheType,
        clothe_color=ClotheColor,
        clothe_graphic_type=ClotheGraphicType,
    )

    for attr, value in attrs.items():
        print(f"Rendering {attr}")
        attr_types_dir = os.path.join(output_dir, attr)
        os.makedirs(attr_types_dir, exist_ok=True)
        attributes = {}
        if isinstance(value, dict):
            new_value = value.pop(attr)
            attributes.update(value)
            value = new_value

        for attr_type in value:
            attributes.update({
                attr: attr_type,
            })
            avatar = PyAvataaar(**attributes)
            avatar.render_png_file(os.path.join(attr_types_dir, f'{attr_type.name.lower()}.png'))
            avatar.render_svg_file(os.path.join(attr_types_dir, f'{attr_type.name.lower()}.svg'))
