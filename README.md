# NBA Database Build

## Overview

This repo builds a database to store data from the NBA API. It uses the `NBAStatPy` package (a wrapper for `nba_api`). Every week the database will be updated with new data during the season.

## Data Ingested

This shows a list of the data being collected, the methods used to collect the data and a brief description.

---

### Player Level Data

> :ledger: Some player data may not need to be updated as frequently (i.e., player awards). The season level API will be used for most player/season level data.

#### Combine Stats

- Method: `Player.get_combine_stats`
- Primary Key: `PLAYER_ID`
- Description: Gets combine stats for all participating players for the given player's rookie season

#### Common Info

- Method: `Player.get_common_info`
- Primary Key: `PLAYER_ID`
- Description: `.json` file containing common player information such as height/weight

---

### Season Level Data

> :ledger: Season level API calls get data for each player in the league. This is much more efficient than calling data for each player and season separately.

#### Player Defense

- Method: `Season.get_defense_player`
- Primary Key: `PLAYER_ID` + `SEASON_ID`
- Description: Shows player level defense.

#### Team Defense

- Method: `Season.get_defense_team`
- Primary Key: `TEAM_ID` + `SEASON_ID`
- Description: Shows team level defense

#### Lineup Details

- Method: `Season.get_lineup_details`
- Primary Key: `LINEUP_ID` +`SEASON_ID`
- Description: Gets advanced lineup data

#### Lineups

- Method: `Season.get_lineups`
- Primary Key: `LINEUP_ID` + `SEASON_ID`
- Description: Gets basic lineup data

#### Opponent Shooting

- Method: `Season.get_opponent_shooting`
- Primary Key: `TEAM_ID` + `SEASON_ID`
- Description: Shows how opponents shot against a team

#### Player Clutch

- Method: `Season.get_player_clutch`
- Primary Key: `PLAYER_ID` + `SEASON_ID`
- Description: Gets team lineup data

#### Player Games

- Method: `Season.get_player_games`
- Primary Key: `GAME_ID` + `PLAYER_ID`
- Description: Gets game data for each player for a given season

#### Player Hustle

- Method: `Season.get_player_hustle`
- Primary Key: `PLAYER_ID` + `SEASON_ID`
- Description: Gets player hustle data for a season

#### Player Matchups

- Method: `Season.get_player_matchups`
- Primary Key: `PLAYER_ID` + `OPPONENT_ID` + `SEASON_ID`
- Description: Gets data for each matchup for a given season (offensive player vs defensive player)

#### Player Shot Locations

- Method: `Season.get_player_shot_locations`
- Primary Key: `PLAYER_ID` + `SEASON_ID`
- Description: Gets player shot splits by location

#### Player Shots

- Method: `Season.get_lineups`
- Primary Key: `LINEUP_ID` + `SEASON_ID`
- Description: Gets team lineup data

#### Player Stats

- Method: `Season.get_player_stats`
- Primary Key: `PLAYER_ID` + `SEASON_ID`
- Description: Gets basic player stats

#### Player Salaries

- Method: `Season.get_salaries`
- Primary Key: `PLAYER_ID` + `SEASON_ID`
- Description: Gets player salary data

#### Team Clutch

- Method: `Season.get_team_clutch`
- Primary Key: `TEAM_ID` + `SEASON_ID`
- Description: Gets team clutch data

#### Team Games

- Method: `Season.get_team_games`
- Primary Key: `TEAM_ID` + `SEASON_ID`
- Description: Gets game data for each team for a season

#### Team Hustle

- Method: `Season.get_team_hustle`
- Primary Key: `TEAM_ID` + `SEASON_ID`
- Description: Gets team hustle data for a season

#### Team Shot Locations

- Method: `Season.get_team_shot_locations`
- Primary Key: `TEAM_ID` + `SEASON_ID`
- Description: Gets team shooting splits by location

#### Team Stats

- Method: `Season.get_team_stats`
- Primary Key: `TEAM_ID` + `SEASON_ID`
- Description: Gets basic team stats

---

### Game Data

> :ledger: Game data is data at a game level for each player or Play by Play data

#### Advanced

- Method: `Game.get_advanced`
- Primary Key: `PLAYER_ID` + `GAME_ID`
- Description: Gets advanced stats for each player for a game

#### Defense

- Method: `Game.get_defense`
- Primary Key: `PLAYER_ID` + `GAME_ID`
- Description: Gets defensive stats for each player for a game

#### Hustle

- Method: `Game.get_hustle`
- Primary Key: `PLAYER_ID` + `GAME_ID`
- Description: Gets hustle stats for each player for a game

#### Matchups

- Method: `Game.get_matchups`
- Primary Key: `PLAYER_ID` + `OPPONENT_ID` + `GAME_ID`
- Description: Gets matchup stats for a game

#### PlaybyPlay

- Method: `Game.get_playbyplay`
- Primary Key: `ACTION_ID` + `GAME_ID`
- Description: Gets play by play data for a game

#### Tracking

- Method: `Game.get_playertrack`
- Primary Key: `PLAYER_ID` + `GAME_ID`
- Description: Gets location stats for each player for a game

#### Rotation

- Method: `Game.get_rotations`
- Primary Key: `ROTATION_ID` + `PLAYER_ID` + `GAME_ID`
- Description: Gets rotations for each player for a game

#### Scoring

- Method: `Game.get_scoring`
- Primary Key: `PLAYER_ID` + `GAME_ID`
- Description: Gets scoring stats for each player for a game

#### Usage

- Method: `Game.get_usage`
- Primary Key: `PLAYER_ID` + `GAME_ID`
- Description: Gets usage stats for each player for a game

---

### Synergy Data

> :ledger: Synergy data is split by play type. It can be gotten for teams and for players

#### Player Transition

- Method: `Season.get_synergy_player("TRANSITION")` / `Season.get_synergy_team("TRANSITION)`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets transition data

#### Isolation

- Method: `Season.get_synergy_player("ISOLATION")` / `Season.get_synergy_team("ISOLATION")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets isolation data

#### P&R Ball Handler

- Method: `Season.get_synergy_player("PRBALLHANDLER")` / `Season.get_synergy_team("PRBALLHANDLER")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets pick and roll data when they are the ball handler

#### P&R Roller

- Method: `Season.get_synergy_player("PRROLLMAN")` / `Season.get_synergy_team("PRROLLMAN")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets pick and roll data when they are the roll man

#### Post Up

- Method: `Season.get_synergy_player("POSTUP")` / `Season.get_synergy_team("POSTUP")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets post up data

#### Spot Up

- Method: `Season.get_synergy_player("SPOTUP")` / `Season.get_synergy_team("SPOTUP")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets spotup data

#### Handoff

- Method: `Season.get_synergy_player("HANDOFF")` / `Season.get_synery_team("HANDOFF")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets dribble handoff data

#### Cut

- Method: `Season.get_synergy_player("CUT")` / `Season.get_synergy_team("CUT")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets cutting data

#### Screens

- Method: `Season.get_synergy_player("OFFSCREEN")` / `Season.get_synergy_team("OFFSCREEN")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets screening data for coming off screens

#### Offensive Rebounds

- Method: `Season.get_synergy_player("OFFREBOUND")` / `Season.get_synergy_team("OFFREBOUND")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets offensive rebounding data

---

### Tracking Data

> :ledger: Tracking data is similar to synergy data but instead of playtype the splits are more based on location

#### Distance

- Method: `Season.get_tracking_player("DISTANCE")` / `Season.get_tracking_team("DISTANCE")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets distance traveled data

#### Possessions

- Method: `Season.get_tracking_player("POSSESSIONS")` / `Season.get_tracking_team("POSSESSIONS")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets per possession stats

#### Catch & Shoot

- Method: `Season.get_tracking_player("CATCHSHOOT")` / `Season.get_tracking_team("CATCHSHOOT")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets catch & shoot data

#### Pullup

- Method: `Season.get_tracking_player("PULLUP")` / `Season.get_tracking_team("PULLUP")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets data for pullup shots

#### Drives

- Method: `Season.get_tracking_player("DRIVES")` / `Season.get_tracking_team("DRIVES")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets data for drives to the basket

#### Passing

- Method: `Season.get_tracking_player("PASSING")` / `Season.get_tracking_team("PASSING")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets passing data and estimated assists

#### Elbow

- Method: `Season.get_tracking_player("ELBOW")` / `Season.get_tracking_team("ELBOW")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets data for elbow area shots

#### Post

- Method: `Season.get_tracking_player("POST")` / `Season.get_tracking_team("POST")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets data for when a player/team is in the post

#### Paint

- Method: `Season.get_tracking_player("PAINT")` / `Season.get_tracking_team("PAINT")`
- Primary Key: `PLAYER_ID` + `SEASON_ID` / `TEAM_ID` + `SEASON_ID`
- Description: Gets data for when a player/team is in the paint

---

### Potential Future Inclusions

#### Pass Splits

- Method: `Player.get_pt_pass`
- Primary Key: `PLAYER_ID` + `SEASON_ID` + `GROUP_SET`
- Description: Shows passing statistics for passes made to/from teammates

#### Rebound Splits

- Method: `Player.get_pt_reb`
- Primary Key: `PLAYER_ID` + `SEASON_ID` + `GROUP_SET`
- Description: Shows rebounding statistics by splits

#### Shot Splits

- Method: `Player.get_pt_shot`
- Primary Key: `PLAYER_ID` + `SEASON_ID` + `GROUP_SET`
- Description: Shows shooting spits
