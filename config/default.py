import os
from yacs.config import CfgNode as CN

_C = CN()

# General configurations
_C.OUTPUT_DIR = ''
_C.LOG_DIR = ''
_C.DATA_DIR = ''

# Model configurations
_C.MODEL = CN()
_C.MODEL.NAME = ''
_C.MODEL.NUM_JOINTS = 17
_C.MODEL.IMAGE_SIZE = [256, 256]

# Train configurations
_C.TRAIN = CN()
_C.TRAIN.OPTIMIZER = 'Adam'
_C.TRAIN.LR = 0.001
_C.TRAIN.BATCH_SIZE = 32

# Dataset configurations
_C.DATASET = CN()
_C.DATASET.ROOT = ''
_C.DATASET.DATASET = 'lsp'
_C.DATASET.TRAIN_SET = 'train'
_C.DATASET.TEST_SET = 'valid'

# Debug configurations
_C.DEBUG = CN()
_C.DEBUG.DEBUG = False
