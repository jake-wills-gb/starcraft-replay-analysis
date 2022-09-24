import sys
import sc2reader
import matplotlib.pyplot as plt
import prettyPrinterV2 as prettyPrinter
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

def plot_workers(replay):
    length_of_game = int(replay.game_length.total_seconds())
    workers_1 = [worker_counter(replay, k, 1) for k in range(length_of_game)]
    workers_2 = [worker_counter(replay, k, 2) for k in range(length_of_game)]
    plt.figure()
    plt.plot(workers_1, label=replay.players[0])
    plt.plot(workers_2, label=replay.players[1])
    plt.legend(loc=2)
    plt.show()


def main():
    path = sys.argv[1]
    replay = sc2reader.load_replay(path)
    print(prettyPrinter.formatReplay(replay))
    plot_workers(replay)


if __name__ == '__main__':
    main()
