import pandas as pd
from PIL import Image
from torch.utils.data import Dataset


class ProductionLineAnalysisDataset(Dataset):
    def __init__(self, anno_dir='files/', img_path='images/data/', transform=None,
                 test_mode=False):
        self.test_mode = test_mode
        self.transform = transform
        if self.test_mode:
            self.img_path = img_path + 'test/'
            self.image_list = pd.read_csv(anno_dir + 'test_labels.csv')
        else:
            self.img_path = img_path + 'train/'
            self.image_list = pd.read_csv(anno_dir + 'train_labels.csv')

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, idx):
        label = self.image_list['label'][idx]
        filename = self.image_list['images'][idx]
        img = Image.open(self.img_path + filename)
        img = img.convert('RGB')
        image = self.transform(img)
        return image, label
