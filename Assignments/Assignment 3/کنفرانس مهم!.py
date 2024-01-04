import re

num_inputs = int(input())
domain_set = set()
pattern = r'@(\w+\.\w+)'

for i in range(num_inputs):
    email = input()
    match = re.findall(pattern, email)
    domain_set.update(match)

result = sorted(domain_set)

for domain in result:
    print(domain)