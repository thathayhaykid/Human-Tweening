# Filename: checkingCuda.py
# Author: Hayhay
# Purpose: To check cuda version

import torch

print(torch.cuda.is_available())

print(torch.cuda.get_device_name(0))

x = torch.tensor([1.0, 2.0, 3.0])
if torch.cuda.is_available():
    x = x.to('cuda')

torch.cuda.empty_cache()
