import applescript
from appscript import app, mactypes

DEFAULT_PHOTOSHOP_LOCATION = "/Applications/Adobe Photoshop 2022/Adobe Photoshop 2022.app"

_QUIT_SCRIPT = """
tell application "Adobe Photoshop 2022"
    quit
end tell
"""

_CLOSE_FILE_SCRIPT = """
tell application "Adobe Photoshop 2022"
    close current document saving no
end tell
"""


def close_current_doc():
    """Close current doc without saving"""
    return applescript.AppleScript(_CLOSE_FILE_SCRIPT).run()


def open_photoshop(filename: str = None, ps_filepath: str = DEFAULT_PHOTOSHOP_LOCATION, ending: str = ".psd"):
    """Opens photoshop and optionally opens a specific file"""
    print(f"Opening file: {filename + ending}")
    ps = app(ps_filepath)
    if filename:
        ps.open(mactypes.Alias(filename + ending))
    return ps


def quit_photoshop():
    return applescript.AppleScript(_QUIT_SCRIPT).run()


class ScriptBuilder:
    """class for building AppleScript scripts for PS automation"""

    def __init__(self, save_filename: str, save_path: str):
        self.script = self._script_init(save_filename, save_path)

    def _script_init(self, save_filename: str, save_path: str):
        return f"""
set save_filepath to ((path to home folder as text) & "{save_path.replace('/', ':')}:{save_filename}") as text
tell application "Adobe Photoshop 2022"
    activate
    -- make docRef the active document
    set docRef to the current document
"""

    def edit_layer(self, text_layer_name: str, new_text: str):
        self.script += f"""
    set textLayer to layer "{text_layer_name}" of docRef
    set contents of text object of textLayer to "{new_text}"
"""

    def _add_close(self):
        self.script += """
    set myOptions to {class:PNG save options}
    save current document in file save_filepath as PNG with options myOptions with copying
end tell"""

    def run(self):
        self._add_close()
        applescript.AppleScript(self.script).run()

    def __repr__(self):
        return self.script
