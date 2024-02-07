import os
from pathlib import Path

from trdg import generators
from faker import Faker

from module.argparser import get_parser
from module.misc import langs


def generate(
        font_files: list,
        image_dir: Path,
        count: int = 10,
        language: str = "ru",
        size: int = 128,
        distorsion: int = 3,
        dist_orient: int = 2,
        blur: int = 3,
        random_blur: bool = True,
        bg_type: int = 3,
        skew: int = 0,
):
    faker_lang = langs[language]
    fake = Faker(faker_lang)
    fake_names = [fake.first_name() for _ in range(10)]

    gen = generators.GeneratorFromStrings(
        fake_names,
        language=language,
        fonts=font_files if font_files else None,
        count=count,
        size=size,
        distorsion_type=distorsion,
        distorsion_orientation=dist_orient,
        blur=blur,
        random_blur=random_blur,
        background_type=bg_type,
        image_dir=image_dir,
        skewing_angle=skew,
    )

    out_names = []
    for img, name in gen:
        if name in out_names:
            splitname = name.rsplit("_")[-1]
            if splitname == name:
                name += "_1"
            else:
                imgcount = int(splitname) + 1
                name += f"_{imgcount}"
        out_names.append(name)
        img.save(
            _out / f"{name}.jpg"
        )
    return


if __name__ == "__main__":
    _dir = Path(__file__).parent.resolve()
    _fonts = _dir / "fonts"
    _out = _dir / "output"
    _backgrounds = _dir / "backgrounds"

    for dir in (_fonts, _out, _backgrounds):
        if not os.path.exists(_dir / dir):
            os.mkdir(dir)

    parser = get_parser()
    args = parser.parse_args()
    fonts = []
    for root, _, filenames in os.walk(_fonts):
        for filename in filenames:
            fonts.append(os.path.join(root, filename))

    generate(
        font_files=fonts,
        image_dir=_backgrounds,
        count=args.count,
        language=args.language,
        size=args.size,
        distorsion=args.distorsion,
        dist_orient=args.distorsion_orientation,
        blur=args.blur,
        random_blur=args.no_random_blur,
        bg_type=args.background,
        skew=args.skewing_angle,
    )
