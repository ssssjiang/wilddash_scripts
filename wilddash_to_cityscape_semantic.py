import numpy as np
import os
import os.path as osp
import cv2
from collections import namedtuple


from PIL import Image

join = os.path.join

WilddashClass = namedtuple(
    "WilddashClass",
    ["id", "trainId"]
)

wilddash_labels = [
    WilddashClass(0, 255),
    WilddashClass(1, 255),
    WilddashClass(2, 255),
    WilddashClass(3, 255),
    WilddashClass(4, 255),
    WilddashClass(5, 255),
    WilddashClass(6, 255),
    WilddashClass(7, 0),
    WilddashClass(8, 1),
    WilddashClass(9, 255),
    WilddashClass(10, 255),
    WilddashClass(11, 2),
    WilddashClass(12, 3),
    WilddashClass(13, 4),
    WilddashClass(14, 255),
    WilddashClass(15, 255),
    WilddashClass(16, 255),
    WilddashClass(17, 5),
    WilddashClass(18, 255),
    WilddashClass(19, 6),
    WilddashClass(20, 7),
    WilddashClass(21, 8),
    WilddashClass(22, 9),
    WilddashClass(23, 10),
    WilddashClass(24, 11),
    WilddashClass(25, 12),
    WilddashClass(26, 13),
    WilddashClass(27, 14),
    WilddashClass(28, 15),
    WilddashClass(29, 255),
    WilddashClass(30, 255),
    WilddashClass(31, 16),
    WilddashClass(32, 17),
    WilddashClass(33, 18),
    WilddashClass(34, 13),
    WilddashClass(35, 13),
    WilddashClass(36, 255),
    WilddashClass(37, 255),
    WilddashClass(38, 0),
]


def mkdir_or_exist(dir_name, mode=0o777):
    if dir_name == '':
        return
    dir_name = osp.expanduser(dir_name)
    os.makedirs(dir_name, mode=mode, exist_ok=True)


def custom_to_trainid(custom):
    trainid = np.ones_like(custom) * 255

    labels = wilddash_labels
    for label in labels:
        orig_id = label.id
        new_id = label.trainId
        # Manually set license plate to id 34 and trainId 255
        if orig_id == -1:
            orig_id = 34
            new_id = 255
        trainid[custom == orig_id] = new_id
    return trainid


if __name__ == '__main__':
    input_dir = '/persist_datasets/wilddashv1/labels/'
    output_semamic_dir = '/persist_datasets/wilddashv1/trainid/'

    # semantic_dir_list = [d for d in os.listdir(input_dir) if os.path.isdir(join(input_dir,d))]

    imgpath_list = [d for d in os.listdir(input_dir) if os.path.isdir(join(input_dir, d))]
    if output_semamic_dir:
        mkdir_or_exist(output_semamic_dir)
        for d in imgpath_list:
            mkdir_or_exist(join(output_semamic_dir, d))
    imgpath_list.append('')

    for d in imgpath_list:
        input_d = join(input_dir, d)
        semantic_file_list = [f for f in os.listdir(input_d) if os.path.isfile(join(input_d, f))]

        for f in semantic_file_list:
            panoptic_img = cv2.imread(join(input_d, f), cv2.IMREAD_GRAYSCALE)
            semantic_img = custom_to_trainid(panoptic_img)

            output_semamic_filename = join(output_semamic_dir, d, f)

            Image.fromarray(np.uint8(semantic_img)).convert('L').save(output_semamic_filename)
            print(output_semamic_filename)
        print(d, "OK")
