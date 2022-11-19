#!/usr/bin/env python3
"""
Sample script to send prometheus metrics on port 8000
"""
from prometheus_client import start_http_server, Counter, Gauge
import time
import random

# Uncomment to avoid collecting own metrics
# import prometheus_client as prom
# prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
# prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
# prom.REGISTRY.unregister(prom.GC_COLLECTOR)

# Gauges
prom_dummy_gauge_1 = Gauge("prom_dummy_gauge_1", 
                      "prom_dummy_gauge_1_description", 
                      ["label1"])
def report_prom_dummy_gauge_1_gauge(metric_val, label_dict):
    prom_dummy_gauge_1.labels(label_dict["label1"])\
                            .set(value=metric_val)

prom_dummy_gauge_2 = Gauge("prom_dummy_gauge_2", 
                      "prom_dummy_gauge_2_description", 
                      ["label1", "label2"])
def report_prom_dummy_gauge_2_gauge(metric_val, label_dict):
    prom_dummy_gauge_2.labels(label_dict["label1"], 
                         label_dict["label2"])\
                            .set(value=metric_val)


# Counters
prom_dummy_counter_1 = Counter("prom_dummy_counter_1", 
                          "prom_dummy_counter_1_description", 
                          ['label1', 'label2', 'label3'])
def report_prom_dummy_counter_1_counter(inc, label_dict):
    prom_dummy_counter_1.labels(label_dict["label1"], 
                           label_dict["label2"], 
                           label_dict["label3"])\
                      .inc(amount=inc)

prom_dummy_counter_2 = Counter("prom_dummy_counter_2", 
                          "prom_dummy_counter_2_description", 
                          ['label1', 'label2'])
def report_prom_dummy_counter_2_counter(inc, label_dict):
    prom_dummy_counter_2.labels(label_dict["label1"], 
                           label_dict["label2"])\
                      .inc(amount=inc)

def init():
    # Start up the server to expose the metrics.
    # metrics are available on all paths right now.
    start_http_server(8000)

    while True:
        report_prom_dummy_gauge_1_gauge(metric_val=random.randint(1,100),
                                   label_dict={"label1": "label1_val"})

        # punch a value for dummy alert
        report_prom_dummy_gauge_1_gauge(metric_val=500,
                                   label_dict={"label1": "label2_val"})

        report_prom_dummy_gauge_2_gauge(metric_val=random.randint(100,200),
                                   label_dict={"label1": "label1_val",
                                               "label2": "label2_val"})
        report_prom_dummy_counter_1_counter(inc=random.randint(1,100),
                                       label_dict={"label1": "label1_val",
                                                   "label2": "label2_val",
                                                   "label3": "label3_val"})
        report_prom_dummy_counter_2_counter(inc=random.randint(1,100),
                                       label_dict={"label1": "label1_val",
                                                   "label2": "label2_val"})
        time.sleep(15)
    
init()