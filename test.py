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
        facial_hair_color=pa.HairColor,
        facial_hair_type=pa.FacialHairType.BEARD_MAJESTIC,
    ),
    top_type=pa.TopType,
    hat_color=dict(
        hat_color=pa.Color,
        top_type=pa.TopType.HAT,
    ),
    mouth_type=pa.MouthType,
    eye_type=pa.EyesType,
    nose_type=pa.NoseType,
    eyebrow_type=pa.EyebrowType,
    accessories_type=pa.AccessoriesType,
    clothe_type=pa.ClotheType,
    clothe_color=pa.Color,
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

