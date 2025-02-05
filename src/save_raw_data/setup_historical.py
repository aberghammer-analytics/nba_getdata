import json
from pathlib import Path
from time import sleep

from loguru import logger
from nbastatpy.season import Season
from tqdm import tqdm
from typing_extensions import Dict, List

HISTORICAL_PARAMETER_PATH = Path("src/save_raw_data/historical_parameters.json")
OUTPUT_PATH = Path("src/save_raw_data/ingest_ids_playoffs.json")


def main():
    logger.info("Setting Up")
    historical_params = json.loads(HISTORICAL_PARAMETER_PATH.read_text())
    earliest_season = historical_params.get("earliest_season")
    last_season = historical_params.get("latest_season")

    seasons = list(range(earliest_season, last_season + 1))

    total_tasks = len(seasons)
    progress_bar = tqdm(total=total_tasks, desc="Progress", unit="task")

    game_ids: Dict = {}
    player_ids: List = []

    for season in seasons:
        progress_bar.set_description(f"Getting {str(season)}")
        season_ingest = Season(
            season,
            playoffs=historical_params.get("playoffs"),
            permode=historical_params.get("permode"),
        )
        df = season_ingest.get_player_games()
        game_ids[str(season)] = df["GAME_ID"].unique().tolist()
        player_ids.extend(df["PLAYER_ID"].astype(str).unique().tolist())
        progress_bar.update(1)
        sleep(1)
    progress_bar.close()

    historical_params["GAME_IDS"] = game_ids
    historical_params["PLAYER_IDS"] = list(set(player_ids))

    logger.info("Saving Data")
    with open(OUTPUT_PATH, "w") as json_file:
        json.dump(historical_params, json_file, indent=4)


if __name__ == "__main__":
    main()
