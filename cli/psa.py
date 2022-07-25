import click
from src.ps_automation import (
    open_photoshop,
    close_photoshop,
    update_and_save_file,
    PHOTOSHOP_FILEPATH,
    DEFAULT_LAYER_NAME,
    DEFAULT_SAVE_PATH,
)


@click.group()
def psa():
    """
    Entrypoint for photoshop automation cli

    :return:
    """


def parse_names(names):
    return [x.strip() for x in names.split(",")]


@psa.command(name="run")
@click.option("-t", "--template", help="template filepath")
@click.option("-f", "--namefile", help="filepath for csv with list of names")
@click.option("-l", "--layer", help=f"name of text layer to overwrite. default = {DEFAULT_LAYER_NAME}", default=DEFAULT_LAYER_NAME)
@click.option("-n", "--names", help="comma separated list of names to make. "
                                    "Ex: 'Bob Vance,Bob the Builder,Bobby Tables'")
@click.option("-s", "--savedir", help="directory to save files", default=DEFAULT_SAVE_PATH)
@click.option("-o", "--overwrite", is_flag=True, help="Overwrite existing files if present", default=True)
@click.option("-v", "--verbose", is_flag=True, help="verbosity", default=True)
def run(
    template: str,
    namefile: str = None,
    layer: str = DEFAULT_LAYER_NAME,
    names: str = None,
    savedir: str = None,
    overwrite: bool = True,
    verbose: bool = True,
):
    print()
    if verbose:
        print("=====================================")
        print("=     PhotoShop Automation Tool     =")
        print("=====================================")
        print("Settings:")
        print(f" -template file = {template}")
        print(f" -layer name    = {layer}")
        print(f" -save folder   = {savedir}")
        if namefile:
            print(f" -name file     = {namefile}")
        print(f" -overwrite     = {overwrite}")
        print("=====================================")
        print()

    # TODO - validate template file exists and throw error if it doesn't
    # TODO - validate save dir exists and create if it doesn't

    name_list = parse_names(names)
    print(f"Found {len(name_list)} names")

    print(f"Opening template file...")
    open_photoshop(PHOTOSHOP_FILEPATH, template)

    print("Creating files...")
    for new_text in name_list:
        update_and_save_file(new_text, layer, savedir)

    print(f"Closing PhotoShop...")
    close_photoshop()
    print(f"Complete! Files saved to ~/{savedir.replace(':', '/')}/")
    print()
