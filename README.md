# Subnetting problem generator

This python script is made for students of the Faculty of Computing, Belgrade, to automatically create problems to practice subnet problems for the Computer Communications/Networks class. 



## How it works

Run the following command to start the script

```bash
python3 main.py
```

The script outputs a file `podmrezavanje.md`, a markdown file that has the problem sets and their solutions.

Example generation can be found in the repository files.

### Global variables

| Variable Name | Function                       |
| ------------- | ------------------------------ |
| NUM_PROBLEMS  | Number of problems to generate |
| MIN_DEVICES   | Minimum devices per subnet     |
| MAX_DEVICES   | Maximum devices per subnet     |
| MIN_SUBNETS   | Minimum subnets per problem    |
| MAX_SUBNETS   | Maximum subnets per problem    |

## Known issues

When a problem has **3** subnets, the solution only solves for 1 subnet. 

