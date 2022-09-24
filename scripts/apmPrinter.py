import sys
import sc2reader
from sc2reader.engine.plugins import APMTracker, SelectionTracker
sc2reader.engine.register_plugin(APMTracker())
sc2reader.engine.register_plugin(SelectionTracker())


def getAPM(replay):
    return replay.teams[0].players[0].avg_apm


def getAvgAPM(replays):
    avg_apm = 0
    nb_replays = 0
    for r in replays:
        apm = getAPM(r)
        if (apm > 0):
            nb_replays += 1
            avg_apm += apm
            print(apm)
    avg_apm = avg_apm/nb_replays
    return avg_apm


def main():
    paths = sys.argv[1]
    replays = sc2reader.load_replays(paths)
    print("average apm: {}".format(getAvgAPM(replays)))


if __name__ == '__main__':
    main()
