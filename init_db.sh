#!/usr/bin/env bash
set -eux
sudo pg_ctlcluster 14 main start
sudo -u postgres psql < init.sql