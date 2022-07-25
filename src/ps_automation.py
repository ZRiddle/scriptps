import applescript
from appscript import app, mactypes

PHOTOSHOP_FILEPATH = '/Applications/Adobe Photoshop 2022/Adobe Photoshop 2022.app'
DEFAULT_LAYER_NAME = "TextLayer"
DEFAULT_SAVE_PATH = "source/saves"

template_filename = "sample-ps-file.psd"
names = ["Billie Joe", "Cotton Eye Joe", "Randy McRanderson"]

CLOSE_SCRIPT = """
tell application "Adobe Photoshop 2022"
    close current document saving no
    quit
end tell
"""

EDIT_SCRIPT = """
set save_filepath to ((path to home folder as text) & "{save_path}:{save_filename}") as text
tell application "Adobe Photoshop 2022"
    activate
    -- make docRef the active document
    set docRef to the current document

    set textLayer to layer "{text_layer_name}" of docRef
    set contents of text object of textLayer to "{new_text}"
    set myOptions to {{class:PNG save options}}
    save current document in file save_filepath as PNG with options myOptions with copying
end tell
"""


def open_photoshop(ps_filepath: str, filename: str = None):
    """Opens photoshop and optionally opens a specific file"""
    ps = app(ps_filepath)
    if filename:
        ps.open(mactypes.Alias(filename))
    return ps


def close_photoshop():
    return applescript.AppleScript(CLOSE_SCRIPT).run()


def get_save_filename(new_text: str, template_filename: str) -> str:
    """Create a unique filename for saving"""
    return template_filename[:-4] + "_" + new_text.replace(" ", "_") + ".png"


def update_and_save_file(new_text: str, text_layer_name: str = DEFAULT_LAYER_NAME, save_path: str = DEFAULT_SAVE_PATH):
    applescript.AppleScript(
        EDIT_SCRIPT.format(
            new_text=new_text,
            text_layer_name=text_layer_name,
            save_filename=get_save_filename(new_text, template_filename),
            save_path=save_path.replace("/", ":"),
        )
    ).run()


if __name__ == "__main__":
    open_photoshop(PHOTOSHOP_FILEPATH, template_filename)

    for new_text in names:
        update_and_save_file(new_text, DEFAULT_LAYER_NAME, DEFAULT_SAVE_PATH)
