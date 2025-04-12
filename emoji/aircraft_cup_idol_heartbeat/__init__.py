from datetime import datetime
from pathlib import Path

from pil_utils import BuildImage

from meme_generator import MemeArgsModel, add_meme
from meme_generator.exception import TextOverLength
from meme_generator.utils import make_jpg_or_gif

img_dir = Path(__file__).parent / "images"


def aircraft_cup_idol_heartbeat(images: list[BuildImage], texts: list[str], args: MemeArgsModel):
    frame = BuildImage.open(img_dir / "0.png")

    ta = "他"
    name = ta
    if texts:
        name = texts[0]
    elif args.user_infos:
        info = args.user_infos[0]
        ta = "他" if info.gender == "male" else "她"
        name = info.name or ta

    text = f"{name}の❤️最愛"
    #{name}挚爱❤️👩‍❤️‍💋‍👨{name}愛のカップ。
    try:
        frame.draw_text(
            (53, 140, 811, 280),
            text,
            max_fontsize=100,
            min_fontsize=20,
            valign="bottom",
        )
    except ValueError:
        raise TextOverLength(name)

    def make(imgs: list[BuildImage]) -> BuildImage:
        img = imgs[0].convert("RGBA").circle().resize((920, 920))
        return frame.copy().paste(img, (340, 340), alpha=True, below=True)

    return make_jpg_or_gif(images, make)


add_meme(
    "aircraft_cup_idol_heartbeat",
    aircraft_cup_idol_heartbeat,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    keywords=["偶像心跳"],
    date_created=datetime(2024, 12, 21),
    #time 2024年12月21日 21:31:25
    #By Anyliew
    date_modified=datetime(2024, 12, 21),
)
