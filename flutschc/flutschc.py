#!/usr/bin/env python3

# Author: Florian Zaruba
# Date: 14.10.2017
# Description: UVM Scaffolding

import argparse

parser = argparse.ArgumentParser(description='Flutsch compiler')
parser.add_argument("filename", help="filename.fl")
args = parser.parse_args()

print(args.filename)
