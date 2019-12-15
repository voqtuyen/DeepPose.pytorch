import os
from scipy.io import loadmat
import argparse
import glob
import pandas as pd
import numpy as np

# Set seed for random generator
np.random.seed(100)


def fix_invisible_joint(skeleton):
    """
    Args:
        skeleton: a 2-d numpy array of a person's skeleton
    Example:
        fix_invisible_joint([
            [75.0, 75.0, 1.0],
            [-20, 0., 0.]
            ...
        ])
    """
    return skeleton


def split_data(data_dir, val_ratio=0.2):
    """
    Read data from joints.mat annotation file and split into train and test set
    Descriptions:
        - The file joints.mat is a MATLAB data file containing the joint annotations in a 14x3x10000 matrix 
        called 'joints' with x and y locations and a binary value indicating the visbility of each joint.
            1. Right ankle
            2. Right knee
            3. Right hip
            4. Left hip
            5. Left knee
            6. Left ankle
            7. Right wrist
            8. Right elbow
            9. Right shoulder
            10. Left shoulder
            11. Left elbow
            12. Left wrist
            13. Neck
            14. Head top
        - The name of image file is the same as the index of the joint within joints.mat
    Args:
        - annotation: path to annotation file in .mat format
        - val_ration: dataset ratio to use for validation

    """

    joint_anno = os.path.join(data_dir, 'joints.mat')
    images_dir = os.path.join(data_dir, 'images')

    joint_content = loadmat(joint_anno)
    # Numpy array containing joints (14, 3, 10000)
    joints = joint_content['joints']
    # Convert to np array of shape (10000, 14, 3)
    joints = joints.transpose(2, 0, 1)
    num_val_examples = int(joints.shape[0] * val_ratio)
    # List containing indexes to extract data for validation data
    perm = np.random.permutation(joints.shape[0])[:num_val_examples].tolist()
    
    images = glob.glob(images_dir + '/*.jpg')
    
    train_images = []
    val_images = []
    train_joints = []
    val_joints = []

    for img_path in images:
        # Get image name 
        img_name = os.path.basename(img_path)
        # Image name is greater than image index by 1
        img_indx = int(img_name.split('.')[0][2:]) - 1
        skeleton = joints[img_indx, :, :]
        
        if img_indx in perm:
            val_images.append(img_name)
            val_joints.append(skeleton)
        else:
            train_images.append(img_name)
            train_joints.append(skeleton)

    train_df = pd.DataFrame({'image': train_images, 'joints': train_joints})
    val_df = pd.DataFrame({'image': val_images, 'joints': val_joints})
    train_df.to_csv(os.path.join(data_dir, 'train.csv'))
    val_df.to_csv(os.path.join(data_dir, 'val.csv'))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data_dir', default='data/lspet', help='Specify path to dataset directory')
    parser.add_argument('-r', '--val_ratio', default=0.2, help='The ration between train and test set')
    args = parser.parse_args()    

    split_data(args.data_dir)
