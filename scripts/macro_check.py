import sys
import sc2reader
import matplotlib.pyplot as plt
from sc2reader.engine.plugins import APMTracker, SelectionTracker
sc2reader.engine.register_plugin(APMTracker())
sc2reader.engine.register_plugin(SelectionTracker())


def worker_counter(replay, second, player_id):
    workers = []

    for event in replay.events:
        if event.name == "UnitBornEvent" and event.control_pid == player_id:
            if event.unit.is_worker:
                workers.append(event.unit)
        if event.name == "UnitDiedEvent":
            if event.unit in workers:
                workers.remove(event.unit)
        if event.second > second:
            break
    return len(workers)


def formatReplay(replay):
    return """
    {filename}
    --------------------------------------------------
    SC2 Version {release_string}
    {category} Game, {start_time}
    {type} on {map_name}
    Length: {game_length}
    """.format(**replay.__dict__)


def twoBaseSaturation(replay, player):
    length_of_game = int(replay.game_length.total_seconds())
    for time in range(length_of_game):
        if(worker_counter(replay, time, player)>=44):
            return(time)
    return(0)

def secondsToMinutes(seconds):
    m, s = divmod(seconds, 60)
    return('{:02d}:{:02d}'.format(m,s))


def main():
    path = sys.argv[1]
    replay = sc2reader.load_replay(path)
    print(formatReplay(replay))
    print('two base saturation at :')
    print(secondsToMinutes(twoBaseSaturation(replay, 1)))
    print(secondsToMinutes(twoBaseSaturation(replay, 2)))


if __name__ == '__main__':
    main()
