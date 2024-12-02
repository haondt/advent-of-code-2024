import lib

def is_safe(report):
    previous_level = None
    trend = None
    is_safe = True
    for level in report:
        if previous_level is None:
            previous_level = level
            continue
        dist = abs(previous_level - level)
        if (dist < 1) or (dist > 3):
            is_safe = False
            break
        if trend is None:
            if previous_level < level:
                trend = 'increasing'
            else:
                trend = 'decreasing'
            previous_level = level
            continue
        if trend == 'increasing':
            if previous_level > level:
                is_safe = False
                break
        else:
            if previous_level < level:
                is_safe = False
                break
        previous_level = level
    return is_safe

def p1():
    data = lib.read()
    safe = 0
    for report in data.split('\n'):
        report = [int(i) for i in report.split(' ')]
        if is_safe(report):
            safe += 1
    print(safe)

def p2():
    data = lib.read()
    safe = 0
    for report in data.split('\n'):
        report = [int(i) for i in report.split(' ')]
        if is_safe(report):
            safe += 1
            continue
        for i in range(len(report)):
            partial_report = report[:i] + report[i+1:]
            if is_safe(partial_report):
                safe += 1
                break

    print(safe)

p2()


