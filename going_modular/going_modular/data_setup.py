
import os
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
import requests
import zipfile
from pathlib import Path

# data_path=Path("data/")
# image_path=data_path/"pizza_steak_sushi"

# if image_path.is_dir():
#   print(f"{image_path} already exists.")
# else:
#   print(f"Did not find {image_path} creating one...")
#   image_path.mkdir(parents=True,exist_ok=True)
# with open(data_path/"pizza_steak_sushi.zip","wb") as f:
#   request=requests.get("https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip")
#   print("Downloading pizza, steak, sushi data")
#   f.write(request.content)
# with zipfile.ZipFile(data_path/"pizza_steak_sushi.zip","r") as zip_ref:
#   print("Unzipping pizza,steak,sushi data...")
#   zip_ref.extractall(image_path)

# os.remove(data_path/"pizza_steak_sushi.zip")


NUM_WORKERS=os.cpu_count()
def create_dataloaders(
    train_dir:str,
    test_dir:str,
    transform:transforms.Compose,
    batch_size:int,
    num_workers:int=NUM_WORKERS
):
  train_data=datasets.ImageFolder(train_dir,transform=transform)
  test_data=datasets.ImageFolder(test_dir,transform=transform)
  class_names=train_data.classes
  train_dataloader=DataLoader(
      train_data,
      batch_size=batch_size,
      shuffle=True,
      num_workers=NUM_WORKERS,
      pin_memory=True)
  test_dataloader=DataLoader(test_data,
                             batch_size=batch_size,
                             shuffle=False,
                             num_workers=NUM_WORKERS,
                             pin_memory=True)
  return train_dataloader,test_dataloader,class_names
