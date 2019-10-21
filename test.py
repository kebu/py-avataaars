import pytest

from py_avataaars import PyAvataaar


@pytest.fixture(scope="session")
def image_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("img.png")
    avatar = PyAvataaar()
    avatar.render_png_file(str(fn))
    return fn


def test_create_avataaar(image_file):
    assert image_file.exists()
