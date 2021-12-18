import math
from enum import Enum


class StateMachine(Enum):
    VERSION = "get version"
    TYPE = "get type"
    BLOCK = "read block"
    END_PACK = "end of pack"


def decrypt_hex(a):
    s = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    return s[a]


class Package:
    def __init__(self, parent=None):
        self.version = 0
        self.type = None
        self.parent = parent
        self.needs = None
        self.length_type = None
        self.data = ""
        self.mean = ""

    def set_version(self, version):
        self.version = int(version, base=2)
        self.data += version

    def set_type(self, type):
        self.type = int(type, base=2)
        self.data += type

    def set_length_type(self, type):
        self.length_type = int(type, base=2)
        self.data += type

    def add_data(self, data):
        self.mean += data[1:]
        self.data += data

    def set_needs(self, needs):
        self.needs = int(needs, base=2)
        self.data += needs

    def read_subpack(self, subpack):
        if self.length_type == 0:
            self.needs -= subpack.length
        elif self.length_type == 1:
            self.needs -= 1

    def __repr__(self):
        return f"v: {self.version} t: {self.type} mean: {self.mean}"

    def __str__(self):
        return self.__repr__()

    @property
    def length(self):
        return len(self.data)


with open("input.txt") as f:
    bits = "".join(list(map(lambda x: decrypt_hex(x), f.readline().strip())))

state = StateMachine.VERSION

pack = Package()
packages = [pack]

while bits:
    if all([x == "0" for x in bits]):
        break
    if state == StateMachine.VERSION:

        pack.set_version(bits[:3])
        bits = bits[3:]

        state = StateMachine.TYPE

    elif state == StateMachine.TYPE:

        pack.set_type(bits[:3])
        bits = bits[3:]

        if pack.type == 4:
            state = StateMachine.BLOCK
        else:

            type_length = bits[:1]
            bits = bits[1:]
            pack.set_length_type(type_length)

            if type_length == "0":
                needs = bits[:15]
                bits = bits[15:]
            else:
                needs = bits[:11]
                bits = bits[11:]
            pack.set_needs(needs)

            pack = Package(pack)
            packages.append(pack)

            state = StateMachine.VERSION

    elif state == StateMachine.BLOCK:

        block = bits[:5]
        bits = bits[5:]

        pack.add_data(block)

        if block[0] == "0":
            state = StateMachine.END_PACK

    elif state == StateMachine.END_PACK:

        if pack.parent is None:

            state = StateMachine.VERSION
            pack = Package()
            packages.append(pack)

        else:
            pack.parent.read_subpack(pack)
            if pack.parent.needs == 0:
                pack = pack.parent
            else:
                pack = Package(pack.parent)
                packages.append(pack)
                state = StateMachine.VERSION

print(sum([packed.version for packed in packages]))


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


def calculate_package(in_pack):
    if in_pack.type == 4:
        mean = int(in_pack.mean, base=2)
    else:
        subpacks = [calculate_package(subpack) for subpack in packages if subpack.parent == in_pack]
        if in_pack.type == 0:
            mean = sum(subpacks)
        elif in_pack.type == 1:
            mean = multiplyList(subpacks)
        elif in_pack.type == 2:
            mean = min(subpacks)
        elif in_pack.type == 3:
            mean = max(subpacks)
        elif in_pack.type == 5:
            mean = 1 if subpacks[0] > subpacks[1] else 0
        elif in_pack.type == 6:
            mean = 1 if subpacks[0] < subpacks[1] else 0
        elif in_pack.type == 7:
            mean = 1 if subpacks[0] == subpacks[1] else 0

    return mean


print(calculate_package(packages[0]))
