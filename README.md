# industrial-automation-utils
Small examples for interacting with industrial-style devices (OPC UA, HTTP).  Visibility

Small, self-contained Python examples that demonstrate how I structure
code for interacting with industrial-style devices and services.

These scripts are **simplified** and do not connect to any real hardware.
They are inspired by patterns I used when working with:

- OPC UA–controlled devices (e.g. grippers via gateways)
- HTTP-based plate pushers and similar lab automation equipment

## Contents

- `opc_ua_client_demo.py` – a minimal stub-style OPC UA client interface
- `platepusher_demo.py` – a simple example for driving a plate pusher over HTTP-style APIs

## Run the examples

```bash
pip install -r requirements.txt
python opc_ua_client_demo.py
python platepusher_demo.py

