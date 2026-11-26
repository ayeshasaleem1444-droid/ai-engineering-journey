import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10),
)
x = torch.randn(64, 784)
target = torch.randint(0, 10, (64,))
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for step in range(3):
    optimizer.zero_grad()
    output = model(x)
    loss = criterion(output, target)
    loss.backward()
    breakpoint()
    optimizer.step()
    print(f"step {step}: loss={loss.item():.4f}")
