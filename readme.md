# MIPS CPU Simulator

This project implements a CPU simulator capable of handling a subset of MIPS instructions. The simulator includes a Register File, Memory, Arithmetic Logic Unit (ALU), and support for executing instructions such as `ADD`, `SUB`,`J`, and others. It also includes a basic cache mechanism that can be toggled on, off, or flushed.

## Features

- **Instruction Set Architecture (ISA)**: Implements a subset of MIPS instructions.
- **Register File**: 32 general-purpose registers (`R0` to `R31`) with program counter (`pc`).
- **Memory**: A configurable memory module (default size 1024 words) with load and store functionality.
- **Arithmetic Logic Unit (ALU)**: Supports basic arithmetic and comparison operations.
- **Cache System**: Supports enabling, disabling, and flushing cache for memory operations.
- **Instruction Execution**: Includes an executor to handle and execute individual instructions.
- **HALT Instruction**: Terminates program execution.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sofiatmenezes/your-repo-name.git
   cd your-repo-name
2. Ensure you have Python 3.6 or higher installed on your system.
3. Create an instruction_input.txt file in the same directory with your program instructions (one instruction per line).

## Usage

1. Define your program in the instruction_input.txt file using the supported MIPS instructions.

Example:

```txt
ADD,R1,R2,R3
SUB,R4,R5,R6
CACHE,1
HALT
```

2. Run the simulator:

```bash
python main.py
```

3. The program will execute the instructions sequentially and display the state of registers after each step.


## Supported Instructions

| Instruction | Description                                               |
|-------------|-----------------------------------------------------------|
| `ADD`       | Adds two registers (`ADD,Rd,Rs,Rt`)                       |
| `ADDI`      | Adds an immediate value to a register (`ADDI,Rt,Rs,Imm`)  |
| `SUB`       | Subtracts two registers (`SUB,Rd,Rs,Rt`)                  |
| `SLT`       | Sets if less than (`SLT,Rd,Rs,Rt`)                        |
| `BNE`       | Branch if not equal (`BNE,Rs,Rt,Offset`)                  |
| `J`         | Jumps to a memory address (`J,Address`)                   |
| `LW`        | Loads a word from memory (`LW,Rt,Offset(Rs)`)             |
| `SW`        | Stores a word to memory (`SW,Rt,Offset(Rs)`)              |
| `CACHE`     | Cache operations (`CACHE,Code`) - 0: OFF, 1: ON, 2: FLUSH |
| `HALT`      | Halts program execution                                   |


## Error Handling
- **Invalid Instructions**: The simulator checks for invalid opcodes and raises an error.
- **Memory Access**: Out-of-bounds memory access raises an IndexError.
- **Cache States**: Cache operations are handled gracefully with appropriate messages.

## Future Enhancements
- Extend support for additional MIPS instructions.
- Add more detailed debugging and logging features.
- Implement pipelining and hazard detection for advanced simulations.
