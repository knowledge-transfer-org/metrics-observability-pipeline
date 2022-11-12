FROM telegraf:1.24.3 as telegraf

COPY configs/telegraf.conf /etc/telegraf/telegraf.conf

CMD ["telegraf", "--config", "/etc/telegraf/telegraf.conf"]