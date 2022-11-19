#!/bin/bash

set -e

exec ./prometheus-metrics.py &
exec ./statsd-metrics.py