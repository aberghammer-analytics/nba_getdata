from pathlib import Path

import pandas as pd
from loguru import logger
from nbastatpy.game import Game
from nbastatpy.player import Player
from nbastatpy.season import Season


class PlayerIngest(Player):
    def __init__(
        self,
        player: str,
        save_folder: Path,
        season_year: str = None,
        playoffs: bool = False,
        permode: str = "PERGAME",
    ):
        super().__init__(
            player=player, season_year=season_year, playoffs=playoffs, permode=permode
        )

        self.save_folder = (
            Path(save_folder)
            .joinpath("PLAYER")
            .joinpath(str(self.name).upper().replace(" ", "").replace("-", ""))
        )

        if not Path(self.save_folder).exists():
            logger.info(f"Creating folder: {str(save_folder)}")
            Path(self.save_folder).mkdir(parents=True, exist_ok=True)

    def save_combine_stats(self):
        df = self.get_combine_stats()[0]
        df.to_csv(
            self.save_folder.joinpath(f"{str(self.id)}_combine_stats.csv"), index=False
        )

    def save_common_info(self):
        df = pd.DataFrame(self.get_common_info(), index=[self.id])
        df.to_csv(
            self.save_folder.joinpath(f"{str(self.id)}_common_info.csv"), index=False
        )


class SeasonIngest(Season):
    def __init__(
        self,
        season_year: str,
        save_folder: Path,
        playoffs=False,
        permode: str = "PERGAME",
    ):
        super().__init__(season_year=season_year, playoffs=playoffs, permode=permode)

        self.season_id = self.season.upper().replace(" ", "").replace("-", "")
        self.save_folder = (
            Path(save_folder).joinpath("SEASON").joinpath(str(self.season_id))
        )

        if not Path(self.save_folder).exists():
            logger.info(f"Creating folder: {str(save_folder)}")
            Path(self.save_folder).mkdir(parents=True, exist_ok=True)

    def save_defense_player(self):
        df = self.get_defense_player()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_player_defense.csv"),
            index=False,
        )


if __name__ == "__main__":
    seasoningest = SeasonIngest("2019", "data/test/")
    seasoningest.save_defense_player()
