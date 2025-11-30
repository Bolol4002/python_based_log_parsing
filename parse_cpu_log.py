import re
from collections import defaultdict


with open("cpu_log.txt", "r") as f:
    lines = f.readlines()

cycle_count = 0
opcode_count = defaultdict(int)


for line in lines:

    cycle_match = re.search(r"cycle (\d+)", line)
    if cycle_match:
        cycle_count = max(cycle_count, int(cycle_match.group(1)))

   
    op_match = re.search(r"\] (\w+) executed", line)
    if op_match:
        opcode = op_match.group(1)
        opcode_count[opcode] += 1

print("----- CPU Performance Summary -----")
print(f"Total Cycles: {cycle_count}")
print("Instruction Counts:")
for op, count in opcode_count.items():
    print(f"  {op}: {count}")

