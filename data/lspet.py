import os
from scipy.io import loadmat
import argparse


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
    # Ignore visibility label
    joints = joints[:, :, :2]

    num_val_examples = int(joints.shape[0] * val_ratio)
    print(joints.shape)
    print(num_val_examples)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data_dir', default='data/lspet', help='Specify path to dataset directory')
    parser.add_argument('-r', '--val_ratio', default=0.2, help='The ration between train and test set')
    args = parser.parse_args()

    

    split_data(args.data_dir)