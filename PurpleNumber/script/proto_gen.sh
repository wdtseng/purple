#!/bin/bash
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/
SRC_DIR=../src/proto
DST_DIR=../gen

for f in $SRC_DIR/*.proto
do
  echo "protoc -I=$SRC_DIR --python_out=$DST_DIR $f"
  protoc -I=$SRC_DIR --python_out=$DST_DIR $f
done
