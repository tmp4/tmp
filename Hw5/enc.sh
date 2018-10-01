#!/bin/bash

tar -czvf archive.tar.gz ./solutions
openssl aes-256-cbc -a -salt -in archive.tar.gz -out archive.tar.gz.enc
rm archive.tar.gz
