import time
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

    def save_defense_team(self):
        df = self.get_defense_team()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_team_defense.csv"), index=False
        )

    def save_lineup_details(self):
        df = self.get_lineup_details()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_lineup_details.csv"),
            index=False,
        )

    def save_lineups(self):
        df = self.get_lineups()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_lineups.csv"),
            index=False,
        )

    def save_opponent_shooting(self):
        df = self.get_opponent_shooting()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_opponent_shooting.csv"),
            index=False,
        )

    def save_player_clutch(self):
        df = self.get_player_clutch()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_player_clutch.csv"),
            index=False,
        )

    def save_player_games(self):
        df = self.get_player_games()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_player_games.csv"),
            index=False,
        )

    def save_player_hustle(self):
        df = self.get_player_hustle()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_player_hustle.csv"),
            index=False,
        )

    def save_player_matchups(self):
        df = self.get_player_matchups()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_player_matchups.csv"),
            index=False,
        )

    def save_player_shot_locations(self):
        df = self.get_player_shot_locations()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_player_shot_locations.csv"),
            index=False,
        )

    def save_player_shots(self):
        df = self.get_player_shots()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_player_shots.csv"),
            index=False,
        )

    def save_player_stats(self):
        df = self.get_player_stats()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_player_stats.csv"),
            index=False,
        )

    def save_salaries(self):
        df = self.get_salaries()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_salaries.csv"),
            index=False,
        )

    def save_team_clutch(self):
        df = self.get_team_clutch()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_team_clutch.csv"),
            index=False,
        )

    def save_team_games(self):
        df = self.get_team_games()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_team_games.csv"),
            index=False,
        )

    def save_team_hustle(self):
        df = self.get_team_hustle()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_team_hustle.csv"),
            index=False,
        )

    def save_team_shot_locations(self):
        df = self.get_team_shot_locations()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_team_shot_locations.csv"),
            index=False,
        )

    def save_team_stats(self):
        df = self.get_team_stats()
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_team_stats.csv"),
            index=False,
        )

    def save_synergy_player(self, synergy_type: str):
        df = self.get_synergy_player(synergy_type)
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_{synergy_type}_player.csv"),
            index=False,
        )

    def save_tracking_player(self, tracking_type: str):
        df = self.get_tracking_player(tracking_type)
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_{tracking_type}_player.csv"),
            index=False,
        )

    def save_synergy_team(self, synergy_type: str):
        df = self.get_synergy_team(synergy_type)
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_{synergy_type}_team.csv"),
            index=False,
        )

    def save_tracking_team(self, tracking_type: str):
        df = self.get_tracking_team(tracking_type)
        df.to_csv(
            self.save_folder.joinpath(f"{self.season_id}_{tracking_type}_team.csv"),
            index=False,
        )


class GameIngest(Game):
    def __init__(
        self,
        game_id: str,
        save_folder: Path,
    ):
        super().__init__(game_id=game_id)
        self.game_id = game_id

        self.save_folder = (
            Path(save_folder).joinpath("GAME").joinpath(str(self.game_id))
        )

        if not Path(self.save_folder).exists():
            logger.info(f"Creating folder: {str(save_folder)}")
            Path(self.save_folder).mkdir(parents=True, exist_ok=True)

    def save_advanced(self):
        df = self.get_advanced()[0]
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_advanced.csv"),
            index=False,
        )

    def save_defense(self):
        df = self.get_defense()[0]
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_defense.csv"),
            index=False,
        )

    def save_hustle(self):
        df = self.get_hustle()[0]
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_hustle.csv"),
            index=False,
        )

    def save_matchups(self):
        df = self.get_matchups()[0]
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_matchups.csv"),
            index=False,
        )

    def save_playbyplay(self):
        df = self.get_playbyplay()
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_playbyplay.csv"),
            index=False,
        )

    def save_tracking(self):
        df = self.get_playertrack()[0]
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_tracking.csv"),
            index=False,
        )

    def save_rotations(self):
        df = self.get_rotations()
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_rotations.csv"),
            index=False,
        )

    def save_scoring(self):
        df = self.get_scoring()[0]
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_scoring.csv"),
            index=False,
        )

    def save_usage(self):
        df = self.get_usage()[0]
        df.to_csv(
            self.save_folder.joinpath(f"{self.game_id}_usage.csv"),
            index=False,
        )


if __name__ == "__main__":
    seasoningest = SeasonIngest("2019", "data/test/")
    seasoningest.save_synergy_player("ISO")
    time.sleep(1)
    seasoningest.save_tracking_player("SPEED")
    time.sleep(1)
    seasoningest.save_synergy_team("ISO")
    time.sleep(1)
    seasoningest.save_tracking_team("SPEED")
