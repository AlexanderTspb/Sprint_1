time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
time_str_no_spaces = time_str.replace(' ', ',')
time_str_single = time_str_no_spaces.split(',')
count_s = 0
for n in time_str_single:
    if 'h' in n:
        count_s = count_s + int(n.replace('h',''))*3600
    elif 'm' in n:
        count_s = count_s + int(n.replace('m',''))*60
    elif 's' in n:
        count_s = count_s + int(n.replace('s',''))
count_m = count_s / 60
print(count_m)