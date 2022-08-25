#!/usr/bin/env bash

WILD_LIST=./random_split/training.txt
type=train

cat ${WILD_LIST} | while read img
do
  echo "${img}"
  line=${img: 0: 13}
  echo "${line}"
#  cp "../images/${line}.jpg" "../${type}/images/${line}.jpg" || exit 1
  convert "../${type}/images/${line}.jpg" "../${type}/images/${line}.png" || exit 1
  cp "../${type}/images/${line}.png" /persist_datasets/custom_datasets/img/train/wilddash/
#  cp "../trainid/${line}.png" "../${type}/trainid/${line}.png"
#  cp "../panoptic/${line}.png" "../${type}/colormap/${line}.png"
done