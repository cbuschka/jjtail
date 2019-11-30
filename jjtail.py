#!/usr/bin/env python3

import json
import sys
import time
from sh import tail

LEVELS = ["???", "DEBUG", "DEBUG", "DEBUG", "DEBUG", "DEBUG", "DEBUG", "INFO", "eight", "nine", "ten"]

for line in tail(*sys.argv[1:], _iter=True):
  map = json.loads(line)
  map["level"] = LEVELS[int(map.get("level","-1"))+1]
  map["timestamp"] = time.strftime('%Y-%m-%d %H:%M:%S%z', time.gmtime(int(map["timestamp"])))
  print("{timestamp} {host} [{_thread_name}] {level}  {short_message}".format(**map))
