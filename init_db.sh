#!/usr/bin/env bash
set -eux
sudo -u postgres psql < init.sql