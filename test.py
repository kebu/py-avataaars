import tempfile
import pathlib

import pytest

import py_avataaars as pa

attrs = dict(
    style=pa.AvatarStyle,
    skin_color=pa.SkinColor,
    hair_color=pa.HairColor,
    facial_hair_type=pa.FacialHairType,
    facial_hair_color=dict(
        facial_hair_color=pa.FacialHairColor,
        facial_hair_type=pa.FacialHairType.BEARD_MAJESTIC,
    ),
    top_type=pa.TopType,
    hat_color=dict(
        hat_color=pa.ClotheColor,
        top_type=pa.TopType.HAT,
    ),
    mouth_type=pa.MouthType,
    eye_type=pa.EyesType,
    nose_type=pa.NoseType,
    eyebrow_type=pa.EyebrowType,
    accessories_type=pa.AccessoriesType,
    clothe_type=pa.ClotheType,
    clothe_color=pa.ClotheColor,
    clothe_graphic_type=pa.ClotheGraphicType,
)


@pytest.fixture(scope="session")
def image_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("img.png")
    avatar = pa.PyAvataaar(mouth_type=pa.MouthType.SMILE, )
    avatar.render_png_file(str(fn))
    return fn


def test_create_avataaar(image_file):
    assert image_file.exists()


def test_create_all():
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
                avatar = pa.PyAvataaar(**attributes)
                avatar_file = pathlib.Path(tmp_dir_name).joinpath(f'{attr_type.name.lower()}.png')
                avatar.render_png_file(str(avatar_file))
                assert avatar_file.exists()


@pytest.mark.skip
def test_create_all_locally():
    output_dir = pathlib.Path(__file__).parent.joinpath('out')

    for attr, value in attrs.items():
        print(f"Rendering {attr}")
        attr_types_dir = output_dir.joinpath(attr)
        attr_types_dir.mkdir(parents=True, exist_ok=True)
        attributes = {}
        if isinstance(value, dict):
            new_value = value.pop(attr)
            attributes.update(value)
            value = new_value

        for attr_type in value:
            attributes.update({
                attr: attr_type,
            })
            avatar = pa.PyAvataaar(**attributes)
            avatar.render_png_file(str(attr_types_dir.joinpath(f'{attr_type.name.lower()}.png')))
            avatar.render_svg_file(str(attr_types_dir.joinpath(f'{attr_type.name.lower()}.svg')))
