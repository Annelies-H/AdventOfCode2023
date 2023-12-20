import re
from collections import namedtuple
from enum import Enum

Destination = namedtuple("Destination", ["destination"])
Instruction = namedtuple("Instruction", ["input", "type", "compare", "out"])
MachinePart = namedtuple("MachinePart", ["x", "m", "a", "s"])
Pipeline = namedtuple("Pipeline", ["name", "instructions"])

class InstructionType(Enum):
    UNCONDITIONAL = "unconditional"
    GREATER_THAN = ">"
    SMALLER_THAN = "<"

def parse_part(line: str) -> MachinePart:
    # machine parts always have the same order in the input file
    ratings = [int(rating) for rating in re.findall('[0-9]+', line)]
    machine_part = MachinePart(*ratings)

    return machine_part

def parse_pipeline(line: str) -> Pipeline:
    name = line.split("{")[0]
    instructions = line.split("{")[1].split(",")
    parsed_instructions = []
    for instruction in instructions:
        if ":" in instruction:
            input = re.findall('[a-zA-Z]+', instruction)[0]
            kind = InstructionType(re.findall("[<,>]", instruction)[0])
            compare = int(re.findall('[0-9]+', instruction)[0])
            out = Destination(re.findall('[a-zA-Z]+', instruction)[-1])
            parsed_instructions.append(Instruction(input, kind, compare, out))
        else:
            kind = InstructionType.UNCONDITIONAL
            out = Destination(re.findall('[a-zA-Z]+', instruction)[-1])
            parsed_instructions.append(Instruction(input=None, type=kind, compare=None, out=out))
    return Pipeline(name=name, instructions=parsed_instructions)


def match_instruction(instruction: Instruction, part: MachinePart) -> bool:
    if instruction.type == InstructionType.UNCONDITIONAL:
        return True
    input = getattr(part, instruction.input)
    if instruction.type == InstructionType.GREATER_THAN:
        return input > instruction.compare
    if instruction.type == InstructionType.SMALLER_THAN:
        return input < instruction.compare
    raise Exception("No matching instruction")


def run_single_pipeline(pipeline: Pipeline, part: MachinePart) -> Destination:
    for instruction in pipeline.instructions:
        if match_instruction(instruction, part):
            return instruction.out
    raise Exception("Pipeline ended before destination was found")


def run_pipelines(pipelines: dict[str, Pipeline], part: MachinePart, name: str = "in") -> bool:
    next_pipeline = pipelines[name]
    destination = run_single_pipeline(next_pipeline, part)
    if destination.destination == "A":
        return True
    if destination.destination == "R":
        return False
    return run_pipelines(pipelines=pipelines, part=part, name=destination.destination)

def part_one(filepath="./inputs/day19.txt"):
    pipelines = {}
    machine_parts = []

    with open(filepath, 'r') as f:
        line = f.readline().strip()

        while line:
            pipeline = parse_pipeline(line)
            pipelines[pipeline.name] = pipeline
            line = f.readline().strip()

        line = f.readline().strip()
        while line:
            machine_part = parse_part(line)
            machine_parts.append(machine_part)
            line = f.readline().strip()


    total_accepted_rating = 0
    for part in machine_parts:
        if run_pipelines(pipelines, part, "in"):
            total_accepted_rating += part.x
            total_accepted_rating += part.m
            total_accepted_rating += part.a
            total_accepted_rating += part.s

    return total_accepted_rating