import torch
import torchvision
from torchvision import transforms
from torch import nn
def create_vit_model(num_classes:int=101,
                     seed:int=42):
    weights=torchvision.models.ViT_B_16_Weights.DEFAULT
    transforms=weights.transforms()
    model=torchvision.models.vit_b_16(weights=weights)

    for param in model.parameters():
        param.requires_grad=False
    # torch.cuda.manual_seed(42)
    model.heads=nn.Sequential(nn.Linear(in_features=768,
                                        out_features=num_classes))
    return model,transforms
