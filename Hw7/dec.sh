#!/bin/bash

openssl aes-256-cbc -d -a -in archive.tar.gz.enc -out archive.tar.gz
tar -xzvf archive.tar.gz
rm archive.tar.gz
