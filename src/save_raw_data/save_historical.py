import json
from pathlib import Path
from time import sleep

from dataingest import GameIngest, PlayerIngest, SeasonIngest
from loguru import logger
from tqdm import tqdm

SAVE_PATH = Path("data/historical_pull_perposs/PLAYOFFS/")
CONFIG_PATH = Path("src/save_raw_data/ingest_ids_playoffs.json")

config = json.loads(CONFIG_PATH.read_text())

# Load season metadata
earliest_season = config.get("earliest_season")
last_season = config.get("latest_season")

seasons = list(range(earliest_season, last_season + 1))

# Load player metadata
player_ids = config.get("PLAYER_IDS")

# Load game metadata
game_ids = config.get("GAME_IDS")

# Load additional params
playoffs = config.get("playoffs")
permode = config.get("permode")


def get_seasons(seasons: list = seasons):
    total_tasks = len(seasons)
    progress_bar = tqdm(total=total_tasks, desc="Progress", unit="task")

    for season in seasons:
        if season < 2000:
            progress_bar.set_description(f"Getting {str(season)}")
            season_ingest = SeasonIngest(
                str(season), SAVE_PATH, playoffs=playoffs, permode=permode
            )
            season_ingest.save_player_games()
            if not playoffs:
                season_ingest.save_salaries()
            progress_bar.update(1)
            continue
        progress_bar.set_description(f"Getting {str(season)}")
        season_ingest = SeasonIngest(str(season), SAVE_PATH)
        season_ingest.save_all_nonsynergy()
        season_ingest.save_all_synergy()
        progress_bar.update(1)

    progress_bar.close()


def get_games(game_ids: dict = game_ids):
    for season, game_id_list in game_ids.items():
        logger.info(f"Getting {str(len(game_id_list))} Games for Season: {str(season)}")
        if int(season) < 2000:
            continue

        total_tasks = len(game_id_list)
        progress_bar = tqdm(total=total_tasks, desc="Seasons", unit="task")
        for game_id in game_id_list:
            game_ingest = GameIngest(game_id, SAVE_PATH)
            game_ingest.save_all()
            progress_bar.update(1)
            sleep(1)

        progress_bar.close()


def get_players(player_ids: list = player_ids):
    total_tasks = len(player_ids)
    progress_bar = tqdm(total=total_tasks, desc="Progress", unit="task")
    for player_id in player_ids:
        player_ingest = PlayerIngest(
            str(player_id), SAVE_PATH, playoffs=playoffs, permode=permode
        )
        player_ingest.save_all()
        progress_bar.update(1)
        sleep(1)

    progress_bar.close()


def main():
    logger.info("Getting Season Data")
    get_seasons(seasons)

    logger.info("Getting Player Data")
    get_players(player_ids)

    # logger.info("Getting Game Data")
    # get_games(game_ids)


if __name__ == "__main__":
    main()
