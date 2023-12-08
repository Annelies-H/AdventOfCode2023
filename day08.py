import math
import re




def parse_input(filepath="./inputs/day08.txt"):
    nodes = {}
    starting_nodes = []
    with open(filepath, 'r') as f:
        line = f.readline().strip()
        instructions = line
        line = f.readline().strip()
        line = f.readline().strip()
        while line:
            parsed_line = re.findall('[A-Z,0-9]+', line)
            node = {
                "L": parsed_line[1].strip(','),
                "R": parsed_line[2].strip(','),
            }
            nodes[parsed_line[0]] = node
            if parsed_line[0].endswith("A"):
                starting_nodes.append(parsed_line[0])
            line = f.readline().strip()

    return instructions, nodes, starting_nodes

def find_zzz(instructions, nodes):
    steps = 0
    node = "AAA"
    while node != "ZZZ":
        for instruction in instructions:
            node = nodes[node][instruction]
            steps += 1
            if node == "ZZZ":
                break
    return steps

def find_multi_zzz(instructions, nodes, starting_nodes):
    # This is either stuck in an endless loop or taking forever :/
    steps = 0
    current_nodes = starting_nodes
    while not all_end_z(current_nodes):
        for instruction in instructions:
            for index, current_node in enumerate(current_nodes):
                current_nodes[index] = nodes[current_node][instruction]
            steps += 1
            if all_end_z(current_nodes):
                break
    return steps


def all_end_z(nodes):
    for node in nodes:
        if not node.endswith("Z"):
            return False
    return True


def find_z(instructions, nodes, starting_node):
    steps = 0
    node = starting_node
    while not node.endswith("Z"):
        for instruction in instructions:
            node = nodes[node][instruction]
            steps += 1
            if node.endswith("Z"):
                break
    return steps


def find_part_two_steps(instructions, nodes, starting_nodes):
    # with hint about using LCM
    all_steps = []
    for starting_node in starting_nodes:
        steps = find_z(instructions, nodes, starting_node)
        all_steps.append(steps)
    total_steps = math.lcm(*all_steps)
    return total_steps


def part_one(filepath="./inputs/day08.txt"):
    instructions, nodes, _ = parse_input(filepath)
    return find_zzz(instructions, nodes)

def part_two(filepath="./inputs/day08.txt"):
    instructions, nodes, starting_nodes = parse_input(filepath)
    result = find_part_two_steps(instructions, nodes, starting_nodes)
    return result