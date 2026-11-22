from datasets import load_dataset

ds = load_dataset("nyu-mll/glue", "mrpc")
print(ds)
print(ds["train"][:2])
