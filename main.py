import tftpy
import logging
import os

logging.basicConfig(level=logging.INFO)

server_host = "10.10.119.167"
remote_path = "\\SMSImages\\K0100005\\boot.K0100005.wim"
local_path = "boot.K0100005.wim"

try:
    tftpy_client = tftpy.TftpClient(server_host)
    logging.info(f"Downloading file from server: {server_host}:{remote_path}")
    tftpy_client.download(remote_path, local_path)
except tftpy.TftpException as e:
    logging.error(f"TFTP error: {e}")
except PermissionError as e:
    logging.error(f"Permission error: {e}")

logging.info(f"Download complete: {local_path}" if os.path.exists(local_path) else "Download failed")
