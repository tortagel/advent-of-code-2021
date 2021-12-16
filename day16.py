from math import prod

def prepare_puzzle(puzzle):
    return bin(int(puzzle[0], 16))[2:].zfill(len(puzzle[0]) * 4)

def parse_packet(bits, result, version_sum, single = False):
    if len(bits) == 0 or int(bits) == 0:
        return '', result, version_sum
    version = int(bits[:3], 2)
    version_sum += version
    type_id = int(bits[3:6], 2)
    bits = bits[6:]
    if type_id == 4:
        literal = ''
        while bits[0] == '1':
            literal += bits[1:5]
            bits = bits[5:]
        literal += bits[1:5]
        bits = bits[5:]
        num = int(literal, 2)
    else:
        if bits[0] == '0':
            bits = bits[1:]
            length_of_sub_packets = int(bits[:15], 2)
            bits = bits[15:]
            _, tmp_result, version_sum = parse_packet(bits[:length_of_sub_packets], [], version_sum)
            bits = bits[length_of_sub_packets:]
        elif bits[0] == '1':
            bits = bits[1:]
            number_of_sub_packets = int(bits[:11], 2)
            bits = bits[11:]
            tmp_result = []
            for _ in range(number_of_sub_packets):
                bits, num, version_sum = parse_packet(bits, [], version_sum, single=True)
                tmp_result.append(num)
        if type_id == 0:
            num = sum(tmp_result)
        elif type_id == 1:
            num = prod(tmp_result)
        elif type_id == 2:
            num = min(tmp_result)
        elif type_id == 3:
            num = max(tmp_result)
        elif type_id == 5:
            num = int(tmp_result[0] > tmp_result[1])
        elif type_id == 6:
            num = int(tmp_result[0] < tmp_result[1])
        elif type_id == 7:
            num = int(tmp_result[0] == tmp_result[1])
    result.append(num)
    if single: return bits, result[0], version_sum
    return parse_packet(bits, result, version_sum)

def solve_part1(puzzle):
    _, _, version_sum = parse_packet(puzzle, [], 0)
    return version_sum

def solve_part2(puzzle):
    _, result, _ = parse_packet(puzzle, [], 0)
    return result[0]
