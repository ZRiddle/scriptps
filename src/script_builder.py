import applescript

DEFAULT_SAVE_PATH = "source/saves"


class ScriptBuilder:
    """class for building AppleScript scripts for PS automation"""

    def __init__(self, save_filename: str, save_path: str = DEFAULT_SAVE_PATH):
        self.script = self._script_init(save_filename, save_path)

    def _script_init(self, save_filename: str, save_path: str = DEFAULT_SAVE_PATH):
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
    set contents of text object of textLayer to "{new_text}
"""

    def _add_close(self):
        self.script += """
    set myOptions to {class:PNG save options}
    save current document in file save_filepath as PNG with options myOptions with copying
end tell"""

    def run(self):
        self._add_close()
        applescript.AppleScript(self.script).run()
