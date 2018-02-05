#!/usr/bin/env bash

INSTALL_DIR="${HOME}/filesystem/vbox-vm-status"

mkdir -p "${INSTALL_DIR}"
./setup.py install --prefix "${INSTALL_DIR}"
