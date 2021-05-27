
import subprocess
import chardet

args = ['ping', 'yandex.ru']
yandex_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in yandex_ping.stdout:
    print(line)
    detect = chardet.detect(line)
    line = line.decode(detect['encoding']).encode('utf-8').decode('utf-8')
    print(line)

args_1 = ['ping', 'youtube.common']
youtube_ping = subprocess.Popen(args_1, stdout=subprocess.PIPE)
for line in youtube_ping.stdout:
    print(line)
    detect = chardet.detect(line)
    line = line.decode(detect['encoding']).encode('utf-8').decode('utf-8')
    print(line)
