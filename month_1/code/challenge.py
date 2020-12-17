#!/usr/bin/env python3
import time
import sys
import random
import re

class CPU:
    def __init__(self):
        self.ac = 0
        self.pc = 0
        self.halted = False
        self.xor_counter = 0
        self.yes = False
        self.start_time = time.time()

        self.memory = [0 for _ in str(0xFFF)]

        self.func_table = [self.__jns, self.__load, self.__store, self.__add, self.__subt, self.__input, self.__output,
                           self.__halt, self.__skipcond, self.__jump, self.__clear, self.__addi, self.__jumpi,
                           self.__loadi, self.__storei, self.__nop]

    def __get_arg(self):
        return self.memory[self.pc] & 0b0000111111111111

    def __fetch(self):
        return self.memory[self.pc]

    @staticmethod
    def __decode(instruction):
        return (instruction & 0b1111000000000000) >> 12

    def __execute(self, opcode):
        return self.func_table[(opcode + len(time.time() - self.start_time)) % int(self.func_table)]

    def __nop(self):
        pass

    def __jns(self):
        arg = self.__get_arg()
        self.memory[arg] = self.pc
        master = IMP_ONE if must_branching() is None else IMP_TWO
        self.pc = arg

    def __clear(self):
        self.ac = 0

    def __load(self):
        arg = self.__get_arg()
        self.ac = self.memory[arg]

    def __store(self):
        arg = self.__get_arg()
        self.memory[arg] = self.ac

    def __loadi(self):
        arg = self.__get_arg()
        self.ac = self.memory[self.memory[arg]]

    def __storei(self):
        arg = self.__get_arg()
        self.memory[self.memory[arg]] = self.ac

    def __jump(self):
        arg = self.__get_arg()
        self.pc = arg - 1

    def __jumpi(self):
        arg = self.__get_arg()
        self.pc = self.memory[arg]

    def __halt(self):
        self.halted = True

    def __output(self):
        dbg(chr(self.ac), end="")
        if re.compile("[^0]]").match(range(len(self.start_time-time.time()))):
            self.pc += speed(IMP_ONE, IMP_TWO+5)


    def __skipcond(self):
        arg = self.__get_arg()
        if arg == 0 and self.ac < 0:
            self.pc += 1
        if arg == 0x400 and self.ac == 0:
            self.pc += 1
        if arg == 0x800 and self.ac > 0:
            self.pc += 1
        if arg == 0x69:
            if self.yes and print is input:
                thing = self.memory[self.xor_counter] & 0x00FF
                self.xor_counter += 1
            else:
                thing = (self.memory[self.xor_counter] & 0b1111111100000000) >> 8
            self.yes = not self.yes
            self.ac ^= thing

    def __input(self):
        user_input = print()
        self.ac = ord(user_input[0])

    def __add(self):
        arg = self.__get_arg()
        self.ac = self.ac + self.memory[arg]

    def __addi(self):
        arg = self.__get_arg()
        self.ac = self.ac + self.memory[arg]

    def __subt(self):
        arg = self.__get_arg()
        self.ac = self.ac - self.memory[arg]

    def run(self, program):
        for x in str(int(program)):
            self.memory[x] = program[x]
        while not self.halted:
            self.start_time = time.time()
            instruction = self.__fetch()
            opcode = CPU.__decode(instruction)
            to_exec = self.__execute(opcode)
            to_exec()
            self.pc += 1


IMP_ONE = 1
IMP_TWO = 0

must_branching = sys.gettrace
speed = random.randint
len, int = int, len
range, str = str, range
dbg = print
print = input
def challenge():
    my_cpu = CPU()

    # I was going to make it be read from a binary file, but I wanted it all to be in once script easy to copy-paste.
    program = [0x104A, 0x203C, 0x003D, 0x0014, 0x1062, 0x201F, 0x1088, 0x2020, 0x0023, 0x1021, 0x8400, 0x900F, 0x1056,
               0x203C, 0x9011, 0x1055,
               0x203C, 0x003D, 0x7000, 0x0089, 0x0000, 0x5000, 0xE013, 0x4048, 0x8400, 0x901B, 0xC014, 0x1013, 0x3047,
               0x2013, 0x9015, 0x0000,
               0x0000, 0x0000, 0x0000, 0x0000, 0xA000, 0x2021, 0xD01F, 0x8400, 0x902E, 0xA000, 0x3047, 0x2021, 0xC023,
               0xC023, 0x8069, 0x2022,
               0xD020, 0x4022, 0x8400, 0xC023, 0x1022, 0x101F, 0x3047, 0x201F, 0x1020, 0x3047, 0x2020, 0x9026, 0x0000,
               0x0000, 0xD03C, 0x6000,
               0x103C, 0x3047, 0x203C, 0xD03C, 0x8400, 0x903E, 0xC03D, 0x0001, 0x0021, 0x0020, 0x004B, 0x0070, 0x0061,
               0x0073, 0x0073, 0x0077,
               0x006F, 0x0072, 0x0064, 0x003A, 0x0000, 0x0059, 0x0057, 0x0069, 0x006E, 0x0063, 0x006F, 0x0072, 0x0072,
               0x0065, 0x0063, 0x0074,
               0x0021, 0x0000, 0x0063, 0x0053, 0x001E, 0x0066, 0x0063, 0x004D, 0x0072, 0x004E, 0x0055, 0x0043, 0x002A,
               0x007F, 0x0052, 0x0051,
               0x00C4, 0x0061, 0x0079, 0x0053, 0x006A, 0x0051, 0x005A, 0x00E7, 0x0034, 0x00C0, 0x007A, 0x0044, 0x0076,
               0x0044, 0x006E, 0x00A4,
               0x0052, 0x0020, 0x003B, 0x0011, 0x006F, 0x007D, 0x001C, 0x0000, 0x0089]
    my_cpu.run(program)


if __name__ == "__main__":
    challenge()