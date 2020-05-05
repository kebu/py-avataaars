import enum
import uuid

from cairosvg import svg2png
from jinja2 import Environment, PackageLoader


class AvatarEnum(enum.Enum):
    def __str__(self):
        return self.name.lower().title()


class AvatarStyle(AvatarEnum):
    CIRCLE = 1
    TRANSPARENT = 2


class SkinColor(AvatarEnum):
    TANNED = '#FD9841'
    YELLOW = '#F8D25C'
    PALE = '#FFDBB4'
    LIGHT = '#EDB98A'
    BROWN = '#D08B5B'
    DARK_BROWN = '#AE5D29'
    BLACK = '#614335'


class HairColor(AvatarEnum):
    AUBURN = '#A55728'
    BLACK = '#2C1B18'
    BLONDE = '#B58143'
    BLONDE_GOLDEN = '#D6B370'
    BROWN = '#724133'
    BROWN_DARK = '#4A312C'
    PASTEL_PINK = '#F59797'
    PLATINUM = '#ECDCBF'
    RED = '#C93305'
    SILVER_GRAY = '#E8E1E1'


class TopType(AvatarEnum):
    NO_HAIR = 10
    EYE_PATCH = 20
    HAT = 30
    HIJAB = 40
    TURBAN = 50
    WINTER_HAT1 = 60
    WINTER_HAT2 = 70
    WINTER_HAT3 = 80
    WINTER_HAT4 = 90
    LONG_HAIR_BIG_HAIR = 100
    LONG_HAIR_BOB = 110
    LONG_HAIR_BUN = 120
    LONG_HAIR_CURLY = 130
    LONG_HAIR_CURVY = 140
    LONG_HAIR_DREADS = 150
    LONG_HAIR_FRIDA = 160
    LONG_HAIR_FRO = 170
    LONG_HAIR_FRO_BAND = 180
    LONG_HAIR_NOT_TOO_LONG = 190
    LONG_HAIR_SHAVED_SIDES = 200
    LONG_HAIR_MIA_WALLACE = 210
    LONG_HAIR_STRAIGHT = 220
    LONG_HAIR_STRAIGHT2 = 230
    LONG_HAIR_STRAIGHT_STRAND = 240
    SHORT_HAIR_DREADS_01 = 250
    SHORT_HAIR_DREADS_02 = 260
    SHORT_HAIR_FRIZZLE = 270
    SHORT_HAIR_SHAGGY_MULLET = 280
    SHORT_HAIR_SHORT_CURLY = 290
    SHORT_HAIR_SHORT_FLAT = 300
    SHORT_HAIR_SHORT_ROUND = 310
    SHORT_HAIR_SHORT_WAVED = 320
    SHORT_HAIR_SIDES = 330
    SHORT_HAIR_THE_CAESAR = 340
    SHORT_HAIR_THE_CAESAR_SIDE_PART = 350


class FacialHairColor(AvatarEnum):
    AUBURN = '#A55728'
    BLACK = '#2C1B18'
    BLONDE = '#B58143'
    BLONDE_GOLDEN = '#D6B370'
    BROWN = '#724133'
    BROWN_DARK = '#4A312C'
    PLATINUM = '#ECDCBF'
    RED = '#C93305'


class FacialHairType(AvatarEnum):
    DEFAULT = 10
    BEARD_MEDIUM = 20
    BEARD_LIGHT = 30
    BEARD_MAJESTIC = 40
    MOUSTACHE_FANCY = 50
    MOUSTACHE_MAGNUM = 60


class ClotheType(AvatarEnum):
    BLAZER_SHIRT = 10
    BLAZER_SWEATER = 20
    COLLAR_SWEATER = 30
    GRAPHIC_SHIRT = 40
    HOODIE = 50
    OVERALL = 60
    SHIRT_CREW_NECK = 70
    SHIRT_SCOOP_NECK = 80
    SHIRT_V_NECK = 90


class ClotheGraphicType(AvatarEnum):
    BAT = 10
    CUMBIA = 20
    DEER = 30
    DIAMOND = 40
    HOLA = 50
    PIZZA = 60
    RESIST = 70
    SELENA = 80
    BEAR = 90
    SKULL_OUTLINE = 100
    SKULL = 110


class ClotheColor(AvatarEnum):
    BLACK = '#262E33'
    BLUE_01 = '#65C9FF'
    BLUE_02 = '#5199E4'
    BLUE_03 = '#25557C'
    GRAY_01 = '#E6E6E6'
    GRAY_02 = '#929598'
    HEATHER = '#3C4F5C'
    PASTEL_BLUE = '#B1E2FF'
    PASTEL_GREEN = '#A7FFC4'
    PASTEL_ORANGE = '#FFDEB5'
    PASTEL_RED = '#FFAFB9'
    PASTEL_YELLOW = '#FFFFB1'
    PINK = '#FF488E'
    RED = '#FF5C5C'
    WHITE = '#FFFFFF'


class MouthType(AvatarEnum):
    DEFAULT = 10
    CONCERNED = 20
    DISBELIEF = 30
    EATING = 40
    GRIMACE = 50
    SAD = 60
    SCREAM_OPEN = 70
    SERIOUS = 80
    SMILE = 90
    TONGUE = 100
    TWINKLE = 110
    VOMIT = 120


class EyesType(AvatarEnum):
    DEFAULT = 10
    CLOSE = 20
    CRY = 30
    DIZZY = 40
    EYE_ROLL = 50
    HAPPY = 60
    HEARTS = 70
    SIDE = 80
    SQUINT = 90
    SURPRISED = 100
    WINK = 110
    WINK_WACKY = 120


class EyebrowType(AvatarEnum):
    DEFAULT = 10
    DEFAULT_NATURAL = 20
    ANGRY = 30
    ANGRY_NATURAL = 40
    FLAT_NATURAL = 50
    RAISED_EXCITED = 60
    RAISED_EXCITED_NATURAL = 70
    SAD_CONCERNED = 80
    SAD_CONCERNED_NATURAL = 90
    UNI_BROW_NATURAL = 100
    UP_DOWN = 110
    UP_DOWN_NATURAL = 120
    FROWN_NATURAL = 130


class AccessoriesType(AvatarEnum):
    DEFAULT = 10
    KURT = 20
    PRESCRIPTION_01 = 30
    PRESCRIPTION_02 = 40
    ROUND = 50
    SUNGLASSES = 60
    WAYFARERS = 70


class PyAvataaar(object):

    def __init__(
            self,
            style: AvatarStyle = AvatarStyle.CIRCLE,
            skin_color: SkinColor = SkinColor.LIGHT,
            hair_color: HairColor = HairColor.BROWN,
            facial_hair_type: FacialHairType = FacialHairType.DEFAULT,
            facial_hair_color: FacialHairColor = FacialHairColor.BLACK,
            top_type: TopType = TopType.SHORT_HAIR_SHORT_FLAT,
            hat_color: ClotheColor = ClotheColor.BLACK,
            mouth_type: MouthType = MouthType.SMILE,
            eye_type: EyesType = EyesType.DEFAULT,
            eyebrow_type: EyebrowType = EyebrowType.DEFAULT,
            accessories_type: AccessoriesType = AccessoriesType.DEFAULT,
            clothe_type: ClotheType = ClotheType.GRAPHIC_SHIRT,
            clothe_color: ClotheColor = ClotheColor.HEATHER,
            clothe_graphic_type: ClotheGraphicType = ClotheGraphicType.BAT,
    ):
        super().__init__()
        self.style = style
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.facial_hair_type = facial_hair_type
        self.facial_hair_color = facial_hair_color
        self.top_type = top_type
        self.hat_color = hat_color
        self.mouth_type = mouth_type
        self.eye_type = eye_type
        self.eyebrow_type = eyebrow_type
        self.accessories_type = accessories_type
        self.clothe_type = clothe_type
        self.clothe_color = clothe_color
        self.clothe_graphic_type = clothe_graphic_type

    @staticmethod
    def __unique_id(prefix: str = None) -> str:
        sub_values = [prefix, str(uuid.uuid4())]
        return "-".join(filter(None, sub_values))

    @staticmethod
    def __template_path(path: str, enum_type: AvatarEnum) -> str:
        return f"{path}{enum_type.name.lower()}.svg"

    def __render_svg(self):
        env = Environment(
            loader=PackageLoader('py_avataaars', 'templates'),
        )
        template = env.get_template('main.svg')
        rendered_template = template.render(
            unique_id=self.__unique_id,
            template_path=self.__template_path,
            style=self.style,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            top_type=self.top_type,
            hat_color=self.hat_color,
            mouth_type=self.mouth_type,
            eye_type=self.eye_type,
            eyebrow_type=self.eyebrow_type,
            accessories_type=self.accessories_type,
            facial_hair_type=self.facial_hair_type,
            facial_hair_color=self.facial_hair_color,
            clothe_color=self.clothe_color,
            clothe_type=self.clothe_type,
            clothe_graphic_type=self.clothe_graphic_type,
        )
        return rendered_template

    def render_png_file(self, output_file: str):
        svg2png(bytestring=self.__render_svg().encode(), write_to=output_file)

    def render_svg_file(self, output_file: str):
        with open(output_file, 'w') as file:
            file.write(self.__render_svg())
