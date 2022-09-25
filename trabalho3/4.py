import datetime
import zoneinfo


t = float(input())

stime = datetime.datetime(1970, 1, 1, 5, 0, tzinfo=datetime.timezone.utc)

ustime = stime.timestamp() # em segundos

hor = []

#print(ustime)

uhor = ustime
hor.append(uhor)
while uhor < 86100.0: # 23:55
    uhor = uhor + (t * 60)
    if uhor <= 86100.0:
        hor.append(uhor)

for i in hor:
    hora = str(datetime.datetime.fromtimestamp(i).astimezone(tz=zoneinfo.ZoneInfo("UTC"))).split()
    hora = hora[1].split(":")

    print(hora[0] + ":" + hora[1])