# output format wasn't specified in the task
d = {}
for i in range(2):
    for _ in range(int(input())):
        p, c = map(int, input().split())
        d[p] = d.get(p, 0) + c
output = ''
for pwr in sorted(d.keys(), reverse=True):
    if d[pwr]:
        if d[pwr] < 0:
            output += ' - '
        else:
            output += ' + '
        if abs(d[pwr]) != 1:
            output += str(abs(d[pwr]))
        elif not pwr:
            output += '1'
        if pwr:
            output += 'x'
            if pwr != 1:
                output += '^' + str(pwr)
if output[:3] == " + ":
  print(output.lstrip(' + '))
elif output[:3] == " - ":
  output = "-"+output[3:]
  print(output)
else:
  print(0)
