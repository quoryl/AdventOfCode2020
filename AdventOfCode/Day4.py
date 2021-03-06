import sys, re
# solution from https://github.com/kresimir-lukin/AdventOfCode2020/blob/main/day04.py
# mandatory_field_validators = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

mandatory_field_validators = {
    'byr': lambda x: re.match('^\d{4}$', x) and 1920 <= int(x) <= 2002,
    'iyr': lambda x: re.match('^\d{4}$', x) and 2010 <= int(x) <= 2020,
    'eyr': lambda x: re.match('^\d{4}$', x) and 2020 <= int(x) <= 2030,
    'hgt': lambda x: (re.match('^\d{3}cm$', x) and 150 <= int(x.replace('cm', '')) <= 193) or (re.match('^\d{2}in$', x) and 59 <= int(x.replace('in', '')) <= 76),
    'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: re.match('^\d{9}$', x)
}

print(mandatory_field_validators)

file = 'Day4_data.txt'
with open(file) as passFile:
    passport_lines = passFile.read().replace('\r\n', '\n').replace('\n\n', '|').replace('\n', ' ').split('|')

part1 = 0
part2 = 0

for line in passport_lines:
    passport = {field.split(':')[0]: field.split(':')[1] for field in line.split()}
    part1 += all(key in passport for key in mandatory_field_validators)
    part2 += all(func(passport.get(key, '')) for key, func in mandatory_field_validators.items())
    
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
