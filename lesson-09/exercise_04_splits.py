from datasets import load_dataset

def make_split(ds, seed=42):
    first = ds.train_test_split(test_size=0.3, seed=seed)
    second = first["test"].train_test_split(test_size=0.5, seed=seed)
    return first["train"], second["train"], second["test"]

ds = load_dataset("stanfordnlp/imdb", split="train")
train, val, test = make_split(ds)
print(f"Train: {len(train)}, Val: {len(val)}, Test: {len(test)}, Total: {len(train) + len(val) + len(test)}")

train2, val2, test2 = make_split(ds)
print("Same first train row:", train[0] == train2[0])
print("Same first val row:", val[0] == val2[0])
print("Same first test row:", test[0] == test2[0])
