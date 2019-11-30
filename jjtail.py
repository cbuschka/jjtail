#!/usr/bin/env python3

import json
import sys
from sh import tail

LEVELS = ["???", "DEBUG", "DEBUG", "DEBUG", "DEBUG", "DEBUG", "DEBUG", "INFO", "eight", "nine", "ten"]

for line in tail(*sys.argv[1:], _iter=True):
  map = json.loads(line)
  map["level"] = LEVELS[int(map.get("level","-1"))+1]
  print("{timestamp} [{level}] {_app_name}@{host} [{_thread_name}] {short_message}".format(**map))
