#!/usr/bin/env bash
# longOrfs_args.sh
# Usage: bash scripts/longOrfs_args.sh 1>results/logs/longOrfs_args.log 2>results/logs/longOrfs_args.err

TransDecoder.LongOrfs -t $1 -O $2 
