import yaml
import os
import asyncio

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'conf.yaml')

async def conf_load():
    with open(CONFIG_PATH, 'r') as conf:
        conf = yaml.safe_load(conf.read())

    db_info = conf["database"]
    for k, v in db_info.items():
        os.environ[k] = v


if __name__ == "__main__":
    asyncio.run(conf_load())
