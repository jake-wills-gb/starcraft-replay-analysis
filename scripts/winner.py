import sys
import sc2reader

def getWinner(replay):
    for team in replay.teams:
        print(team.number)
        if team == replay.winner:
            print("{} won the game".format(team.players[0].init_data["name"]))
        else:
            print("{} lost the game".format(team.players[0].init_data["name"]))

def main():
    path = sys.argv[1]
    replay = sc2reader.load_replay(path)
    print(getWinner(replay))


if __name__ == '__main__':
    main()
