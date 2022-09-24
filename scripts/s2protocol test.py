import os
import mpyq;
from s2protocol import versions;
import json;
print(os.getcwd());
# os.path.isfile('~/Documents/Work/test.SC2Replay');
# archive = mpyq.MPQArchive('~/Documents/Work/SC2 Analyzer/replays/Waterfall (16).SC2Replay');
archive = mpyq.MPQArchive('test.SC2Replay');
print(archive.files);
contents = archive.header['user_data_header']['content'];
header = versions.latest().decode_replay_header(contents);
baseBuild  = header['m_version']['m_baseBuild'];
protocol = versions.build(baseBuild);
contents = archive.read_file('replay.game.events');
gameEvents = protocol.decode_replay_game_events(contents);
cmdEventList = [];
for event in gameEvents:
    if event['_event'] == 'NNet.Game.SCmdEvent':
        cmdEventList.append(event);
json_data = json.dumps(cmdEventList, indent = 4);
output_file = open("test1.JSON", "w");
output_file.write(json_data);
output_file.close;