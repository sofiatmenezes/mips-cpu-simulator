# MIPS instruction
class Instruction:
    def __init__(self, inst):
        if inst is not 0:
            parts = str(inst).strip().split(',')
            self.opcode = parts[0]
            self.operands = parts[1:]
        else:
            self.opcode = 'HALT'

    def is_valid(self):
        return self.opcode in {"ADD", "ADDI", "SUB", "SLT", "BNE", "J", "JAL", "LW", "SW", "CACHE", "HALT"}

# Set of registers in the MIPS architecture
class RegisterFile:
    def __init__(self):
        self.registers = {f"R{i}": 0 for i in range(32)}
        self.pc = 0

    def read(self, register):
        return self.registers[register]

    def write(self, register, value):
        self.registers[register] = value

# Memory of the system  
class Memory:
    def __init__(self, size=1024):
        self.memory = [0] * size

    def load(self, address, cache_state, cache_data):
        if address < 0 or address >= len(self.memory):
            raise IndexError(f"Memory load error: Address {address} out of bounds")
        
        # Check if cache is ON and the data is in the cache
        if cache_state == 1:  # Cache ON
            if address in cache_data:
                return cache_data[address]  # Return cached value
            else:
                value = self.memory[address]  # Fetch from memory
                cache_data[address] = value  # Cache it
                return value
        else:
            # If cache is OFF, fetch directly from memory
            return self.memory[address]

    def store(self, address, value, cache_state, cache_data):
        if address < 0 or address >= len(self.memory):
            raise IndexError(f"Memory store error: Address {address} out of bounds")
        
        # Update the memory
        self.memory[address] = value

        # If cache is ON, update the cache as well
        if cache_state == 1:
            cache_data[address] = value


# Arithmetic Logic Unit
class ALU:
    def add(self, rs, rt):
        return rs + rt

    def addi(self, rs, immediate):
        return rs + immediate

    def sub(self, rs, rt):
        return rs - rt

    def slt(self, rs, rt):
        return 1 if rs < rt else 0

# Executes a given instruction
class InstructionExecutor:
    def __init__(self, register_file, memory, alu, processor):
        self.register_file = register_file
        self.memory = memory
        self.alu = alu
        self.processor = processor

    def execute(self, instruction):
        opcode = instruction.opcode
        operands = instruction.operands

        if opcode == "ADD":
            rd, rs, rt = operands
            self.register_file.write(rd, self.alu.add(self.register_file.read(rs), self.register_file.read(rt)))
        elif opcode == "ADDI":
            rt, rs, immediate = operands
            self.register_file.write(rt, self.alu.addi(self.register_file.read(rs), int(immediate)))
        elif opcode == "SUB":
            rd, rs, rt = operands
            self.register_file.write(rd, self.alu.sub(self.register_file.read(rs), self.register_file.read(rt)))
        elif opcode == "CACHE":
            code = int(operands[0])
            if code == 0:
                self.processor.cache_state = 0  # Cache OFF
                self.processor.cache_data.clear()
                print("Cache OFF")
            elif code == 1:
                self.processor.cache_state = 1  # Cache ON
                print("Cache ON")
            elif code == 2:
                self.processor.cache_data.clear()  # Flush Cache
                print("Cache FLUSHED")
        elif opcode == "J":
            target = int(operands[0])
            self.register_file.pc = target * 4

# MIPS Processor
class MIPSProcessor:
    def __init__(self):
        self.register_file = RegisterFile()
        self.memory = Memory(size=1024)  # Default size of 1024 words
        self.alu = ALU()
        self.cache_state = 0  # 0 = OFF, 1 = ON, 2 = FLUSH
        self.cache_data = {}
        self.executor = InstructionExecutor(self.register_file, self.memory, self.alu, self)
        self.halted = False

    def load_program(self, program):
        if len(program) > len(self.memory.memory):
            raise MemoryError(f"Program size exceeds memory size ({len(self.memory.memory)})")
        
        for i, instruction in enumerate(program):
            self.memory.store(i, instruction, self.cache_state, self.cache_data)

    def run(self):
        # Execution loop
        while not self.halted:
            pc = self.register_file.pc

            # Check if pc is within memory bounds
            if pc < 0 or pc >= len(self.memory.memory):
                raise IndexError(f"Program Counter (PC) out of bounds: {pc}")

            instruction_raw = self.memory.load(pc, self.cache_state, self.cache_data)
            instruction = Instruction(instruction_raw)

            if instruction.opcode == "HALT":
                break

            self.executor.execute(instruction)
            print(processor.register_file.registers)
            self.register_file.pc += 1  # Increment PC


# Example program
program = []

with open('instruction_input.txt') as lines_doc:
    for line in lines_doc.readlines():
        program.append(line)

processor = MIPSProcessor()
processor.load_program(program)
processor.run()
