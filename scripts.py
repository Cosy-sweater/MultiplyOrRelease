import sys
import os


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def create_default_config():
    from dataclasses import asdict
    import tomli_w
    from defaults import AppConfig

    with open(resource_path("app_config.toml"), "w") as f:
        f.write(tomli_w.dumps(asdict(AppConfig())))
