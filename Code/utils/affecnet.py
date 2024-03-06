import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from torchvision.transforms import Lambda
from torchvision.io import read_image


class AffectNet(Dataset):
    """
    A Dataset subclass for handling the AffectNet dataset.

    Attributes:
        annotations (DataFrame): The annotations for the images.
        root_dir (str): The root directory where the images are stored.
        transform (callable, optional): Optional transform to be applied on an image.
    """

    def __init__(self, annotations_file, img_root_dir, transform=None):
        """
        Initializes the AffectNet dataset.

        Args:
            annotations_file (str): The path to the CSV file containing the annotations.
            img_root_dir (str): The root directory where the images are stored.
            transform (callable, optional): Optional transform to be applied on an image.
        """

        self.annotations = pd.read_csv(annotations_file)
        self.root_dir = img_root_dir
        self.transform = transform

        # Check if number of images and annotations match
        if len(self.annotations) != len(os.listdir(self.root_dir)):
            raise ValueError(f"Number of images and annotations do not match:\
            {len(self.annotations)} != {len(os.listdir(self.root_dir))}"
                             )

    def __len__(self):
        """
        Returns the length of the dataset.

        Returns:
            int: The length of the dataset.
        """

        return len(self.annotations)

    def __getitem__(self, idx):
        """
        Returns the image and its labels at the given index.

        Args:
            idx (int): The index of the image.

        Returns:
            tuple: A tuple containing the image, and its labels.
        """

        # Get image name and create path
        img_name = f"{self.annotations.iloc[idx, 0]}.jpg"
        img_path = os.path.join(self.root_dir, img_name)

        # Read image
        image = read_image(img_path)

        # Get labels and convert to tensor
        labels = self.annotations.iloc[idx, 1:]
        labels = labels.to_numpy()
        labels = torch.from_numpy(labels.astype('float'))

        # One-Hot Encode the categorical expressions
        ohe = Lambda(lambda y: torch.zeros(8, dtype=torch.float).scatter_(
            0, torch.tensor(int(y)), value=1))
        exp = ohe(labels[2])
        labels = torch.cat([labels[:2], exp], dim=0)

        # Apply input transforms
        if self.transform:
            image = self.transform(image)

        # Return image and labels
        return image, labels
