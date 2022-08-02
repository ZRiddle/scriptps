import click
import os
from typing import List, Dict

from psa.ps_config import PsConfig
from psa.script_builder import ScriptBuilder, open_photoshop, quit_photoshop, close_current_doc
from psa.order import load_orders, Order


@click.group()
def psa():
    """
    Entrypoint for photoshop automation cli

    :return:
    """


def print_header():
    print("""
    ██████╗ ███████╗ █████╗ 
    ██╔══██╗██╔════╝██╔══██╗
    ██████╔╝███████╗███████║
    ██╔═══╝ ╚════██║██╔══██║
    ██║     ███████║██║  ██║
    ╚═╝     ╚══════╝╚═╝  ╚═╝
      PhotoShop Automation
    """)


def run_script(order: Order, config: PsConfig, settings: Dict[str, bool]):
    is_address_single_line = settings.get(order.design, True)
    script = ScriptBuilder(order.get_filename(), config.output_folder)
    script.edit_layer(config.name_layer, order.name_on_label)
    script.edit_layer(config.address_layer, order.get_address_text(is_address_single_line, config.address_separator))
    return script.run()


def get_order_lookups(orders: List[Order]) -> Dict[str, List[Order]]:
    output = {}
    for order in orders:
        if order.design not in output:
            output[order.design] = []
        output[order.design].append(order)
    return output


@psa.command(name="run")
@click.option("-o", "--overwrite", is_flag=True, help="Overwrite existing files if present", default=True)
@click.option("-v", "--verbose", is_flag=True, help="verbosity", default=True)
def run(overwrite: bool = True, verbose: bool = True):
    _run()


def _run():
    print_header()
    config = PsConfig.from_file()
    print(config)
    settings = config.load_settings()

    orders: List[Order] = load_orders(config.orders_file)
    print(f"Loaded {len(orders)} orders")
    order_lookups = get_order_lookups(orders)
    print(f"Grouping orders by design...")

    print()
    for design, order_list in order_lookups.items():
        print(f"Design {design} - {len(order_list)} orders")
        open_photoshop(os.path.join(config.template_folder, design))

        for order in order_list:
            run_script(order, config, settings)
        print(f"  {len(order_list)} orders saved")
        close_current_doc()

    print("\nSuccess! Closing Photoshop.\n\n")
    quit_photoshop()


if __name__ == "__main__":
    _run()
