"""Simple Prometheus Client to log (public) IP Address."""

import argparse
import logging
import os
import requests
import time
from prometheus_client import start_http_server, Info


parser = argparse.ArgumentParser(description="Public IP as Prometheus metrics.")
parser.add_argument("--port", type=int, default=9191)
parser.add_argument("--delay", type=int, default=60 * 5, help="time in seconds")
args = parser.parse_args()

IP = Info("public_ip", "The public IP address of the host.")
URL = "https://api.ipify.org/?format=json"

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)


def get_public_ip():
    fqn = os.uname()[1]
    public_ip = requests.get(URL).json()['ip']
    logging.info("ip: %s host: %s", public_ip, fqn)
    IP.info({"ip": public_ip, "host": fqn})


if __name__ == "__main__":
    start_http_server(args.port)
    while True:
        get_public_ip()
        time.sleep(args.delay)
