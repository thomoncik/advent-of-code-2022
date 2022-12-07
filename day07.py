with open("input.txt", 'r') as input_file:
    input = input_file.read()

def part1():
    sys = {}
    dirs = set('/')
    current_dir = []
    sizes = {}
    files = set()
    for line in input.splitlines():
        cmd = line.split(' ')
        dir_str = '/'.join(current_dir)
        # print(cmd)
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    current_dir.pop()
                else:
                    current_dir.append(cmd[2])
        elif cmd[0] == 'dir':
            if dir_str not in sys:
                sys[dir_str] = {cmd[1]}
            else:
                sys[dir_str].add(cmd[1])
            dirs.add('/'.join(current_dir) + '/' + cmd[1])
        else:
            if dir_str in files:
                continue
            files.add(dir_str + '/' + cmd[1])
            if dir_str not in sizes:
                sizes[dir_str] = int(cmd[0])
            else:
                sizes[dir_str] += int(cmd[0])

    result = 0
    for dir in dirs:
        r = sum(v for k, v in sizes.items() if k.startswith(dir))
        if r <= 100000:
            result += r

    return result

def part2():
    sys = {}
    dirs = set('/')
    current_dir = []
    sizes = {}
    files = set()
    for line in input.splitlines():
        cmd = line.split(' ')
        dir_str = '/'.join(current_dir)
        # print(cmd)
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    current_dir.pop()
                else:
                    current_dir.append(cmd[2])
        elif cmd[0] == 'dir':
            if dir_str not in sys:
                sys[dir_str] = {cmd[1]}
            else:
                sys[dir_str].add(cmd[1])
            dirs.add('/'.join(current_dir) + '/' + cmd[1])
        else:
            if dir_str in files:
                continue
            files.add(dir_str + '/' + cmd[1])
            if dir_str not in sizes:
                sizes[dir_str] = int(cmd[0])
            else:
                sizes[dir_str] += int(cmd[0])

    max_size = 70000000
    must_left = 30000000

    out = {}
    result = 0
    for dir in dirs:
        r = sum(v for k, v in sizes.items() if k.startswith(dir))
        out[dir] = r

    sor = {k: v for k, v in sorted(out.items(), key=lambda item: item[1])}

    for s, v in sor.items():
        if max_size - out['/'] + v >= must_left:
            return v

    return result

print("Part One: " + str(part1()))
print("Part Two: " + str(part2()))
