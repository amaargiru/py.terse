import json


class Configurator:

    def __init__(self):
        # Hard coded values if config file doesn't exist
        self.alpha: int = 42
        self.bravo: float = 3.14
        self.charlie: str = "8.8.8.8"
        self.delta: list = ["Lorem", "ipsum", "dolor", "sit", "amet"]
        self.echo: dict = {"Winter": "is coming"}

    def read_config_file(self, config_file_name: str = "config.json"):
        try:
            with open(config_file_name) as conf_file:
                for k, v in json.loads(conf_file.read()).items():
                    setattr(self, k, v)
        except Exception as e:
            print(f"Error was detected while reading {config_file_name}: {str(e)}. Hard coded values will be applied")

    def save_config_file(self, config_file_name: str = "config.json"):
        try:
            conf_items = {k: v for k, v in vars(self).items() if isinstance(v, (int, float, str, list, dict))}
            with open(config_file_name, "w") as conf_file:
                json.dump(conf_items, conf_file, sort_keys=False, indent=2)
        except Exception as e:
            print(f"Error was detected while saving {config_file_name}: {str(e)}")
