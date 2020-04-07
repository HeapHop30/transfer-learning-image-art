from torchvision import transforms

img_size = 512

preprocessing = transforms.Compose([
    transforms.Resize(img_size),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[1, 1, 1])
])

postprocessing = transforms.Compose([
    transforms.Normalize(mean=[-0.485, -0.456, -0.406],
                         std=[1, 1, 1]),
    transforms.ToPILImage()
])
