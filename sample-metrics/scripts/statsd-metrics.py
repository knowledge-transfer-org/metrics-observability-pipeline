#!/usr/bin/env python3
"""
Sample script to send statsd metrics
"""
from datadog import initialize, statsd
import time
import random

options = {
    'statsd_host':'telegraf',
    'statsd_port':8125
}

initialize(**options)

while(True):
  # Gauges
  statsd.gauge('statsd_dummy_gauge_1', random.randint(1,100), tags=["label1:label1_val"])
  statsd.gauge('statsd_dummy_gauge_2', random.randint(100,200), tags=["label1:label1_val"])
  # Counters
  statsd.increment('statsd_dummy_counter_1', tags=["label1:label1_val"])
  statsd.decrement('statsd_dummy_counter_2', tags=["label1:label1_val"])
  time.sleep(15)