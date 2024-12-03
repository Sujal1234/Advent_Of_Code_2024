with open("input.txt", 'r') as file:
    lines = [line.strip() for line in file]

def is_safe(report):
    all_inc = True
    all_dec = True
    for i in range(1, len(report)):
        if(report[i] - report[i-1] < 1 or report[i] - report[i-1] > 3):
            all_inc = False
        if(report[i] - report[i-1] < -3 or report[i] - report[i-1] > -1):
            all_dec = False

    return all_inc or all_dec

def count_safe(reports):
    num = 0
    for report in reports:
        if(is_safe(report)):
            num += 1
    return num

def consider(report, index):
    new_rep = report[:index] + report[index+1:]
    return is_safe(new_rep)

def can_be_safe(report):
    '''
    for i in range(len(report)):
        new_rep = report[:i] + report[i+1:]
        if(is_safe(new_rep)):
            return True
    return False
    '''
    ok = False
    k = len(report)

    ok = ok or consider(report, 0)
    for i in range(k - 1):
        diff = report[i+1] - report[i]
        if(abs(diff) < 1 or abs(diff) > 3):
            ok = ok or consider(report, i)
            ok = ok or consider(report, i+1)
            break
        
        if(i+2 < k):
            diff2 = report[i+2] - report[i+1]
            if((diff > 0) != (diff2 > 0)):
                ok = ok or consider(report, i)
                ok = ok or consider(report, i+1)
                ok = ok or consider(report, i+2)
                break
    return ok

def count_safe_new(reports):
    num = 0
    for report in reports:
        if(is_safe(report) or can_be_safe(report)):
            num += 1
    return num

lines = [line.split(" ") for line in lines]
lines = [[int(n) for n in line] for line in lines]

#For part 1:
#print(count_safe(lines))

#For part 2:
print(count_safe_new(lines))
