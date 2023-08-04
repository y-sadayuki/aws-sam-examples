#!/bin/sh

for i in `seq 0 599`
do
    # 1秒に1回実行
    echo $i;
    curl https://xxxx
    sleep 1
done
