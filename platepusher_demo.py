"""
Minimal plate pusher demo.

This script shows how I would structure a small client for an
HTTP-based plate pusher or similar lab-automation device.

The endpoints and URLs here are fake and used for structure only.
"""

import logging
from dataclasses import dataclass
from typing import Any, Dict

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class PlatePusherConfig:
    base_url: str


class PlatePusherClient:
    def __init__(self, config: PlatePusherConfig):
        self.config = config

    def _request(self, path: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
        url = f"{self.config.base_url.rstrip('/')}/{path.lstrip('/')}"
        logger.info("POST %s payload=%s", url, payload)
        # In a real system we would call the device.
        # Here we just simulate a response structure.

        # response = requests.post(url, json=payload, timeout=2.0)
        # response.raise_for_status()
        # return response.json()

        # Simulated response:
        return {"status": "ok", "url": url, "payload": payload}

    def move_to_site(self, site: str) -> Dict[str, Any]:
        logger.info("Requesting move to site: %s", site)
        return self._request("/move", {"site": site})

    def home(self) -> Dict[str, Any]:
        logger.info("Requesting homing move")
        return self._request("/home", {})


def main():
    config = PlatePusherConfig(base_url="http://demo-platepusher.local/api")
    client = PlatePusherClient(config)

    logger.info("Sending demo moves to plate pusher")
    print(client.home())
    print(client.move_to_site("A1"))
    print(client.move_to_site("B4"))


if __name__ == "__main__":
    main()
