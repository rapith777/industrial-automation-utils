```python
"""
Minimal OPC UA-style client demo.

This is a simplified example that shows how I like to structure
code for reading and writing nodes on an OPC UA server.

In real projects this would wrap an async or sync OPC UA library
and hide connection / reconnection logic behind a small interface.
"""

import asyncio
import logging
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FakeOpcUaClient:
    """
    A tiny, fake OPC UA client for demonstration purposes.

    In real code, this could:
    - manage a connection to an OPC UA server
    - provide typed read / write helpers
    - handle reconnects, timeouts, etc.
    """

    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.connected = False

    async def connect(self):
        logger.info("Connecting to OPC UA endpoint: %s", self.endpoint)
        await asyncio.sleep(0.1)
        self.connected = True
        logger.info("Connection established")

    async def disconnect(self):
        if self.connected:
            logger.info("Disconnecting from OPC UA endpoint: %s", self.endpoint)
            await asyncio.sleep(0.05)
            self.connected = False
            logger.info("Disconnected")

    async def read_node(self, node_id: str):
        if not self.connected:
            raise RuntimeError("Not connected")

        logger.info("Reading node %s", node_id)
        await asyncio.sleep(0.05)
        # Return a fake value
        value = 42
        logger.info("Read value %s from node %s", value, node_id)
        return value

    async def write_node(self, node_id: str, value):
        if not self.connected:
            raise RuntimeError("Not connected")

        logger.info("Writing value %s to node %s", value, node_id)
        await asyncio.sleep(0.05)
        logger.info("Write completed")


@asynccontextmanager
async def opcua_session(endpoint: str):
    client = FakeOpcUaClient(endpoint)
    await client.connect()
    try:
        yield client
    finally:
        await client.disconnect()


async def main():
    endpoint = "opc.tcp://demo-opcua-server:4840"

    async with opcua_session(endpoint) as client:
        value = await client.read_node("ns=2;s=Demo.Static.Scalar.Int32")
        await client.write_node("ns=2;s=Demo.Static.Scalar.Int32", value + 1)


if __name__ == "__main__":
    asyncio.run(main())
