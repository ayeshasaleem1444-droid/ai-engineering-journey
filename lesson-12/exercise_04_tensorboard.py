import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("runs/exercise_04")

x_train = torch.randn(64, 784)
y_train = torch.randint(0, 10, (64,))
x_val = torch.randn(64, 784)
y_val = torch.randint(0, 10, (64,))

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10),
)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

for epoch in range(100):
    for step in range(20):
        optimizer.zero_grad()
        loss = criterion(model(x_train), y_train)
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        val_loss = criterion(model(x_val), y_val)

    writer.add_scalar("loss/train", loss.item(), epoch)
    writer.add_scalar("loss/val", val_loss.item(), epoch)

    if epoch % 20 == 0 or epoch == 99:
        print(f"epoch {epoch}: train={loss.item():.4f} val={val_loss.item():.4f}")

writer.close()
print("Done. Scalars written to runs/exercise_04")
