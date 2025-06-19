from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif
from meme_generator.tags import MemeTags

img_dir = Path(__file__).parent / "images"


def kurogames_songlun_finger(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.jpg")

    ta = "她"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"原来{name}是鸣潮玩家\n是潮批啊~\n原来你也喜欢玩鸣潮"
    try:
        frame.draw_text(
            (3, 350, 482, 606),
            text,
            max_fontsize=120,
            min_fontsize=35,
            lines_align="center",
            font_families=["FZShaoEr-M11S"],
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((300, 300))
        return frame.copy().paste(img, (100, 40), alpha=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "kurogames_songlun_finger",
    kurogames_songlun_finger,
    min_images=1,
    max_images=1,
    min_texts=1,
    max_texts=1,
    keywords=["松伦指","松伦哥指", "李松伦指","潮批"],
    tags=MemeTags.wuthering_waves,
    date_created=datetime(2025, 6, 20),
    date_modified=datetime(2025, 6, 20),
)
