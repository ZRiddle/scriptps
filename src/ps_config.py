import os
import configparser
from dataclasses import dataclass
import json

DEFAULT_CONFIG_FILENAME = "config.ini"
HOME_DIR = os.path.expanduser('~')


@dataclass
class PsConfig:
    template_folder: str
    output_folder: str
    settings_file: str = "settings.csv"
    orders_file: str = "resources/1234_fulfillment.csv"
    address_separator: str = "·"
    name_layer: str = "Name"
    address_layer: str = "Address"

    def __post_init__(self):
        """Validate files and paths exist"""
        assert os.path.exists(self.template_folder), f"Template folder doesn't exist! {self.template_folder}"
        assert os.path.exists(self.settings_file), f"Settings file doesn't exist! {self.settings_file}"
        assert os.path.exists(self.orders_file), f"Orders file doesn't exist! {self.orders_file}"
        if not os.path.exists(self.append_home_dir(self.output_folder)):
            os.mkdir(self.append_home_dir(self.output_folder))

    @classmethod
    def from_file(cls, filename=DEFAULT_CONFIG_FILENAME) -> "PsConfig":
        """initialize from a .ini file"""
        parser = configparser.ConfigParser()
        parser.read(filename)
        section = parser["DEFAULT"]
        return cls(
            template_folder=cls.append_home_dir(section["template_folder"]),
            output_folder=section["output_folder"],
            settings_file=cls.append_home_dir(section.get("settings_file", cls.settings_file)),
            orders_file=cls.append_home_dir(section.get("orders_file", cls.orders_file)),
            address_separator=section.get("address_separator", cls.address_separator),
            name_layer=section.get("name_layer", cls.name_layer),
            address_layer=section.get("address_layer", cls.address_layer),
        )

    @classmethod
    def append_home_dir(cls, path):
        return os.path.join(HOME_DIR, path)

    def load_settings(self) -> dict:
        with open(self.settings_file, "r") as f:
            return json.load(f)

    def __repr__(self):
        return (
            f"----- Settings -----\n"
            f"| Template Folder  | {self.template_folder}\n"
            f"| Output Folder    | {self.output_folder}\n"
            f"| Settings File    | {self.settings_file}\n"
            f"| Orders File      | {self.orders_file}\n"
            f"| Addr Separator   | {self.address_separator}\n"
            f"| Name Layer       | {self.name_layer}\n"
            f"| Addr Layer       | {self.address_layer}\n"
            f"--------------------\n"
        )
