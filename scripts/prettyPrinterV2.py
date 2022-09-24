import sys
import sc2reader


def formatTeams(replay):
    teams = list()
    for team in replay.teams:
        players = list()
        for player in team:
            players.append("({0}) {1}".format(
                player.pick_race[0], player.name))
        formattedPlayers = '\n            '.join(players)
        teams.append("Team {0}:  {1}".format(team.number, formattedPlayers))
    return '\n\n'.join(teams)


def formatReplay(replay):
    return """
    {filename}
    --------------------------------------------------
    SC2 Version {release_string}
    {category} Game, {start_time}
    {type} on {map_name}
    Length: {game_length}
    """.format(**replay.__dict__)


def main():
    paths = sys.argv[1]
    for replay in sc2reader.load_replays(paths):
        print (formatReplay(replay))


if __name__ == '__main__':
    main()
