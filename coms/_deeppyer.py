from PIL import Image, ImageOps, ImageEnhance
from io import BytesIO
from enum import Enum
import aiohttp, asyncio, math, argparse

class DeepfryTypes(Enum):
    """
    Enum for the various possible effects added to the image.
    """
    RED = 1
    BLUE = 2


class Colours:
    RED = (254, 0, 2)
    YELLOW = (255, 255, 15)
    BLUE = (36, 113, 229)
    WHITE = (255,) * 3


async def deepfry(img: Image, type=DeepfryTypes.RED) -> Image:
    img = img.copy().convert('RGB')

    if type not in DeepfryTypes:
        raise ValueError(f'Unknown deepfry type "{type}", expected a value from deeppyer.DeepfryTypes')

    # Crush image to hell and back
    img = img.convert('RGB')
    width, height = img.width, img.height
    img = img.resize((int(width ** .75), int(height ** .75)), resample=Image.LANCZOS)
    img = img.resize((int(width ** .88), int(height ** .88)), resample=Image.BILINEAR)
    img = img.resize((int(width ** .9), int(height ** .9)), resample=Image.BICUBIC)
    img = img.resize((width, height), resample=Image.BICUBIC)
    img = ImageOps.posterize(img, 4)

    # Generate red and yellow overlay for classic deepfry effect
    r = img.split()[0]
    r = ImageEnhance.Contrast(r).enhance(2.0)
    r = ImageEnhance.Brightness(r).enhance(1.5)

    if type == DeepfryTypes.RED:
        r = ImageOps.colorize(r, Colours.RED, Colours.YELLOW)
    elif type == DeepfryTypes.BLUE:
        r = ImageOps.colorize(r, Colours.BLUE, Colours.WHITE)

    # Overlay red and yellow onto main image and sharpen the hell out of it
    img = Image.blend(img, r, 0.75)
    img = ImageEnhance.Sharpness(img).enhance(100.0)

    return img

