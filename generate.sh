#!/bin/bash

python -m grpc_tools.protoc -I . --python_out=./interface --grpc_python_out=./interface ./interface.proto
