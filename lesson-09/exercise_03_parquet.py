import sys
sys.path.insert(0, "code")
from datasets import load_dataset
from data_utils import convert_format, load_from_parquet

ds = load_dataset("nyu-mll/glue", "mrpc", split="train")
paths = convert_format(ds, "/tmp/exercise_03", "mrpc_train")
reloaded = load_from_parquet(str(paths["parquet"]))
print(f"Original rows: {len(ds)}, reloaded rows: {len(reloaded)}")
