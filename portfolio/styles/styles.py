import reflex as rx

from enum import Enum

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"

class EmSize(Enum):
    DEFAULT = "1em" 
    MEDIUM = "2em" 
    BIG = "4em" 

class Size(Enum):
    ZERO = "0"
    SMALL = "2" # 8px
    DEFAULT = "4" # 16px / 1em
    MEDIUM = "6" # 32px
    BIG = "8" # 48px
    BIG_NEW = "lg"
    MEDIUM_NEW = "md"

STYLESHEETS = [
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    rx.button: {
        "--cursor-button": "pointer"
    }
}