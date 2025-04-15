from warnings import catch_warnings
import source.constants as CONST
import argparse

# Add source/ to syspath
import sys, os
sys.path.append('./source/')

# Logging
import logging, coloredlogs
coloredlogs.install(level="DEBUG")
logger = logging.getLogger(__name__)

# download GTZAN dataset
def download_dataset() -> None:
    import subprocess
    tmp_zip = "Data.zip"
    url = "https://www.kaggle.com/api/v1/datasets/download/andradaolteanu/gtzan-dataset-music-genre-classification"

    try:
        subprocess.run(f"curl -L -o {tmp_zip} {url}", shell=True, executable="/bin/bash")
        subprocess.run(f"unzip -q {tmp_zip}", shell=True, executable="/bin/bash")
    except subprocess.CalledProcessError as e:
        print(f"subprocess.CalledProcessError: {e}")
        raise
    finally:
        if os.path.exists(tmp_zip): os.remove(tmp_zip)

# commandline args
def parse_args() -> dict:
    parser = argparse.ArgumentParser("luna-tune")
    parser.add_argument(f'-{CONST.DRIVER_ACTION}', help="Action for the driver to take.", type=str)
    args = parser.parse_args()
    return {
        CONST.DRIVER_ACTION: getattr(args, CONST.DRIVER_ACTION)
    }

# driver
if __name__ == "__main__":
    driver_args = parse_args()
    logger.info(f"Script arguments: {driver_args}")

    # if we have train argument we need to check for training data aswell
    if driver_args[CONST.DRIVER_ACTION] == CONST.TRAIN_ARGUMENT:
        if not os.path.isdir(CONST.DATA_FOLDER): 
            logger.warning(f"Did not find a {CONST.DATA_FOLDER} folder, downloading dataset into {CONST.DATA_FOLDER}")
            download_dataset()
        else:
            logger.info(f"Found data folder at: {CONST.DATA_FOLDER}")

    sys.exit(0)

