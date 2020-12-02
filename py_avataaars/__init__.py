import enum
import pathlib
import re
import uuid
from collections import Counter
from io import BytesIO

from cairosvg import svg2png
from jinja2 import Environment, PackageLoader
from jinja2.ext import Extension
from jinja2.lexer import Token


class AvatarEnum(enum.Enum):

    def __new__(cls, *args, **kwargs):
        value = len(cls.__members__)
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, main_value):
        self.main_value = main_value

    def __str__(self):
        return self.name.lower().title()


class AvatarStyle(AvatarEnum):
    TRANSPARENT = 'TRANSPARENT'
    CIRCLE = 'CIRCLE'


class SkinColor(AvatarEnum):
    BLACK = '#614335'
    TANNED = '#FD9841'
    YELLOW = '#F8D25C'
    PALE = '#FFDBB4'
    LIGHT = '#EDB98A'
    BROWN = '#D08B5B'
    DARK_BROWN = '#AE5D29'


class HairColor(AvatarEnum):
    BLACK = '#2C1B18'
    AUBURN = '#A55728'
    BLONDE = '#B58143'
    BLONDE_GOLDEN = '#D6B370'
    BROWN = '#724133'
    BROWN_DARK = '#4A312C'
    PASTEL_PINK = '#F59797'
    PLATINUM = '#ECDCBF'
    RED = '#C93305'
    SILVER_GRAY = '#E8E1E1'


class TopType(AvatarEnum):
    NO_HAIR = 'NO_HAIR'
    EYE_PATCH = 'EYE_PATCH'
    HAT = 'HAT'
    HIJAB = 'HIJAB'
    TURBAN = 'TURBAN'
    WINTER_HAT1 = 'WINTER_HAT1'
    WINTER_HAT2 = 'WINTER_HAT2'
    WINTER_HAT3 = 'WINTER_HAT3'
    WINTER_HAT4 = 'WINTER_HAT4'
    LONG_HAIR_BIG_HAIR = 'LONG_HAIR_BIG_HAIR'
    LONG_HAIR_BOB = 'LONG_HAIR_BOB'
    LONG_HAIR_BUN = 'LONG_HAIR_BUN'
    LONG_HAIR_CURLY = 'LONG_HAIR_CURLY'
    LONG_HAIR_CURVY = 'LONG_HAIR_CURVY'
    LONG_HAIR_DREADS = 'LONG_HAIR_DREADS'
    LONG_HAIR_FRIDA = 'LONG_HAIR_FRIDA'
    LONG_HAIR_FRO = 'LONG_HAIR_FRO'
    LONG_HAIR_FRO_BAND = 'LONG_HAIR_FRO_BAND'
    LONG_HAIR_NOT_TOO_LONG = 'LONG_HAIR_NOT_TOO_LONG'
    LONG_HAIR_MIA_WALLACE = 'LONG_HAIR_MIA_WALLACE'
    LONG_HAIR_SHAVED_SIDES = 'LONG_HAIR_SHAVED_SIDES'
    LONG_HAIR_STRAIGHT = 'LONG_HAIR_STRAIGHT'
    LONG_HAIR_STRAIGHT2 = 'LONG_HAIR_STRAIGHT2'
    LONG_HAIR_STRAIGHT_STRAND = 'LONG_HAIR_STRAIGHT_STRAND'
    SHORT_HAIR_DREADS_01 = 'SHORT_HAIR_DREADS_01'
    SHORT_HAIR_DREADS_02 = 'SHORT_HAIR_DREADS_02'
    SHORT_HAIR_FRIZZLE = 'SHORT_HAIR_FRIZZLE'
    SHORT_HAIR_SHAGGY_MULLET = 'SHORT_HAIR_SHAGGY_MULLET'
    SHORT_HAIR_SHORT_CURLY = 'SHORT_HAIR_SHORT_CURLY'
    SHORT_HAIR_SHORT_FLAT = 'SHORT_HAIR_SHORT_FLAT'
    SHORT_HAIR_SHORT_ROUND = 'SHORT_HAIR_SHORT_ROUND'
    SHORT_HAIR_SHORT_WAVED = 'SHORT_HAIR_SHORT_WAVED'
    SHORT_HAIR_SIDES = 'SHORT_HAIR_SIDES'
    SHORT_HAIR_THE_CAESAR = 'SHORT_HAIR_THE_CAESAR'
    SHORT_HAIR_THE_CAESAR_SIDE_PART = 'SHORT_HAIR_THE_CAESAR_SIDE_PART'


class FacialHairType(AvatarEnum):
    DEFAULT = 'DEFAULT'
    BEARD_MEDIUM = 'BEARD_MEDIUM'
    BEARD_LIGHT = 'BEARD_LIGHT'
    BEARD_MAJESTIC = 'BEARD_MAJESTIC'
    MOUSTACHE_FANCY = 'MOUSTACHE_FANCY'
    MOUSTACHE_MAGNUM = 'MOUSTACHE_MAGNUM'


class ClotheType(AvatarEnum):
    BLAZER_SHIRT = 'BLAZER_SHIRT'
    BLAZER_SWEATER = 'BLAZER_SWEATER'
    COLLAR_SWEATER = 'COLLAR_SWEATER'
    GRAPHIC_SHIRT = 'GRAPHIC_SHIRT'
    HOODIE = 'HOODIE'
    OVERALL = 'OVERALL'
    SHIRT_CREW_NECK = 'SHIRT_CREW_NECK'
    SHIRT_SCOOP_NECK = 'SHIRT_SCOOP_NECK'
    SHIRT_V_NECK = 'SHIRT_V_NECK'


class ClotheGraphicType(AvatarEnum):
    BAT = 'BAT'
    CUMBIA = 'CUMBIA'
    DEER = 'DEER'
    DIAMOND = 'DIAMOND'
    HOLA = 'HOLA'
    PIZZA = 'PIZZA'
    RESIST = 'RESIST'
    SELENA = 'SELENA'
    BEAR = 'BEAR'
    SKULL_OUTLINE = 'SKULL_OUTLINE'
    SKULL = 'SKULL'


class Color(AvatarEnum):
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
    DEFAULT = 'DEFAULT'
    CONCERNED = 'CONCERNED'
    DISBELIEF = 'DISBELIEF'
    EATING = 'EATING'
    GRIMACE = 'GRIMACE'
    SAD = 'SAD'
    SCREAM_OPEN = 'SCREAM_OPEN'
    SERIOUS = 'SERIOUS'
    SMILE = 'SMILE'
    TONGUE = 'TONGUE'
    TWINKLE = 'TWINKLE'
    VOMIT = 'VOMIT'


class NoseType(AvatarEnum):
    DEFAULT = 'DEFAULT'


class EyesType(AvatarEnum):
    DEFAULT = 'DEFAULT'
    CLOSE = 'CLOSE'
    CRY = 'CRY'
    DIZZY = 'DIZZY'
    EYE_ROLL = 'EYE_ROLL'
    HAPPY = 'HAPPY'
    HEARTS = 'HEARTS'
    SIDE = 'SIDE'
    SQUINT = 'SQUINT'
    SURPRISED = 'SURPRISED'
    WINK = 'WINK'
    WINK_WACKY = 'WINK_WACKY'


class EyebrowType(AvatarEnum):
    DEFAULT = 'DEFAULT'
    DEFAULT_NATURAL = 'DEFAULT_NATURAL'
    ANGRY = 'ANGRY'
    ANGRY_NATURAL = 'ANGRY_NATURAL'
    FLAT_NATURAL = 'FLAT_NATURAL'
    RAISED_EXCITED = 'RAISED_EXCITED'
    RAISED_EXCITED_NATURAL = 'RAISED_EXCITED_NATURAL'
    SAD_CONCERNED = 'SAD_CONCERNED'
    SAD_CONCERNED_NATURAL = 'SAD_CONCERNED_NATURAL'
    UNI_BROW_NATURAL = 'UNI_BROW_NATURAL'
    UP_DOWN = 'UP_DOWN'
    UP_DOWN_NATURAL = 'UP_DOWN_NATURAL'
    FROWN_NATURAL = 'FROWN_NATURAL'


class AccessoriesType(AvatarEnum):
    DEFAULT = 'DEFAULT'
    KURT = 'KURT'
    PRESCRIPTION_01 = 'PRESCRIPTION_01'
    PRESCRIPTION_02 = 'PRESCRIPTION_02'
    ROUND = 'ROUND'
    SUNGLASSES = 'SUNGLASSES'
    WAYFARERS = 'WAYFARERS'


class MinifyExtension(Extension):
    def __init__(self, environment):
        super(MinifyExtension, self).__init__(environment)

    def parse(self, parser):
        pass

    def filter_stream(self, stream):
        super_stream = super().filter_stream(stream)

        for token in super_stream:
            if token.type != 'data':
                yield token
                continue

            value = re.sub(r'\n', '', token.value)
            value = re.sub(r'(>)(\s+)(<)', r'\1\3', value)
            value = re.sub(r'\s+', r' ', value)
            value = re.sub(r'(")(\s+)(/>)', r'\1\3', value)

            yield Token(token.lineno, token.type, value)


class PyAvataaar(object):
    PREFIX = 'py-avataaars'

    def __init__(
            self,
            style: AvatarStyle = AvatarStyle.CIRCLE,
            background_color: Color = Color.RED,
            skin_color: SkinColor = SkinColor.LIGHT,
            hair_color: HairColor = HairColor.BROWN,
            facial_hair_type: FacialHairType = FacialHairType.DEFAULT,
            facial_hair_color: HairColor = HairColor.BLACK,
            top_type: TopType = TopType.SHORT_HAIR_SHORT_FLAT,
            hat_color: Color = Color.BLACK,
            mouth_type: MouthType = MouthType.SMILE,
            eye_type: EyesType = EyesType.DEFAULT,
            nose_type: NoseType = NoseType.DEFAULT,
            eyebrow_type: EyebrowType = EyebrowType.DEFAULT,
            accessories_type: AccessoriesType = AccessoriesType.DEFAULT,
            clothe_type: ClotheType = ClotheType.SHIRT_V_NECK,
            clothe_color: Color = Color.HEATHER,
            clothe_graphic_type: ClotheGraphicType = ClotheGraphicType.BAT,
            minify: bool = True,
            simplify: bool = True,
    ):
        super().__init__()
        self.style = style
        self.background_color = background_color
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.facial_hair_type = facial_hair_type
        self.facial_hair_color = facial_hair_color
        self.top_type = top_type
        self.hat_color = hat_color
        self.mouth_type = mouth_type
        self.eye_type = eye_type
        self.nose_type = nose_type
        self.eyebrow_type = eyebrow_type
        self.accessories_type = accessories_type
        self.clothe_type = clothe_type
        self.clothe_color = clothe_color
        self.clothe_graphic_type = clothe_graphic_type
        self.minify = minify
        self.simplify = simplify

    @staticmethod
    def __unique_id(prefix: str = None) -> str:
        sub_values = [PyAvataaar.PREFIX, prefix, str(uuid.uuid4())]
        return "-".join(filter(None, sub_values))

    @staticmethod
    def __template_path(path: str, enum_type: AvatarEnum) -> str:
        return str(pathlib.PurePosixPath(path).joinpath(f"{enum_type.name.lower()}.svg"))

    @staticmethod
    def __template_name(context):
        template_name = getattr(context, '_TemplateReference__context', None) if context else None
        if template_name:
            name = template_name.name
        else:
            name = str(uuid.uuid4())
        name = name.replace('.svg', '').replace('/', '-').replace('\\', '-').replace('_', '-')
        return f'{PyAvataaar.PREFIX}-{name}'

    def __simplify_ids(self, rendered_template):
        id_list = re.findall(r'id="([a-zA-Z0-9-]+)"', rendered_template)
        id_list_multi = {key: value for key, value in Counter(id_list).items() if value > 1}
        if id_list_multi:
            print(f'WARING: file contains multiple same ids: {id_list_multi}')
        for idx, key in enumerate(sorted(id_list, reverse=True)):
            rendered_template = rendered_template.replace(key, f'x{idx}')
        return rendered_template

    def __render_svg(self):
        env = Environment(
            loader=PackageLoader('py_avataaars', 'templates'),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True,
            keep_trailing_newline=False,
            extensions=[MinifyExtension] if self.minify else []
        )
        template = env.get_template('main.svg')
        rendered_template = template.render(
            unique_id=self.__unique_id,
            template_path=self.__template_path,
            template_name=self.__template_name,
            style=self.style,
            background_color=self.background_color,
            skin_color=self.skin_color,
            hair_color=self.hair_color,
            top_type=self.top_type,
            hat_color=self.hat_color,
            mouth_type=self.mouth_type,
            eye_type=self.eye_type,
            nose_type=self.nose_type,
            eyebrow_type=self.eyebrow_type,
            accessories_type=self.accessories_type,
            facial_hair_type=self.facial_hair_type,
            facial_hair_color=self.facial_hair_color,
            clothe_color=self.clothe_color,
            clothe_type=self.clothe_type,
            clothe_graphic_type=self.clothe_graphic_type,
        )
        if self.simplify:
            return self.__simplify_ids(rendered_template)
        return rendered_template

    def render_png_file(self, output_file: str):
        svg2png(self.__render_svg(), write_to=output_file)

    def render_svg_file(self, output_file: str):
        with open(output_file, 'w') as file:
            file.write(self.__render_svg())

    def render_svg(self):
        return self.__render_svg()

    def render_png(self):
        output_file = BytesIO()
        svg2png(self.__render_svg(), write_to=output_file)
        return output_file.getvalue()

    @property
    def unique_id(self) -> str:
        return "".join([f'{y.value:02x}' for x, y in sorted(vars(self).items()) if isinstance(y, AvatarEnum)])

    @unique_id.setter
    def unique_id(self, value: str) -> None:
        if re.fullmatch(r"^[0-9a-fA-F]$", value or "") is not None:
            raise ValueError(f'Cannot parse unique id {value}')

        value_parts = [value[i:i + 2] for i in range(0, len(value), 2)]
        for idx, (key, param_value) in enumerate(
                {x: y for x, y in sorted(vars(self).items()) if isinstance(y, AvatarEnum)}.items()
        ):
            setattr(self, key, param_value.__class__(int(value_parts[idx], 16)))
