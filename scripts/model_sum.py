from torchvision import models
from torchsummary import summary

mod = models.__dict__['resnet101'](pretrained=True)
print(mod)

count = 0

for child in mod.children():
    count += 1
    if count == 7:
        break
    for param in child.parameters():
        param.requires_grad = False

# mod = mod.cuda()
# summary(mod, input_size=(3, 250, 250))
