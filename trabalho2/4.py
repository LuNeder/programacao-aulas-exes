import datetime

data = input().split("/")

# time = "1970" + "-" + data[1] + "-" + data[0] + " 00:00:00+00:00"

time = datetime.datetime(1970, int(data[1]), int(data[0]), tzinfo=datetime.timezone.utc)

utime = time.timestamp()

print(utime)



# if utime >= 9331200.0 and utime <= 11404800.0:
#   print("Áries")
# elif utime >= 11491200.0 and utime <= 14601600.0:
#   print("Touro")
# elif utime >= 14688000.0 and utime <= 17280000.0:
#   print("Gêmeos")
# elif utime >= 17366400.0 and utime <= 19008000.0:
#   print("Câncer")
# elif utime >= 19094400.0 and utime <= 22204800.0:
#   print("Leão")
# elif utime >= 22291200.0 and utime <= 26092800.0:
#   print("Virgem")
# elif utime >= 26179200.0 and utime <= 28080000.0:
#   print("Libra")
# elif utime >= 