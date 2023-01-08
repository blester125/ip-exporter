# ip-exporter

A small script using the prometheus client to log your public IP address.

The IP address is logged as a `Gauage` metric with the key `"ip"` as a label. The value of the metric will always be
`1`.

Using the "label to field" transformation in Grafana is the easiest way to get the IP address to appear in a dashboard
panel.
