log_file_name = 'log.txt'

warnings_count = 0
info_count = 0
error_count = 0

try:
    with open(log_file_name,'r') as log_file:
        for line in log_file:
            print(line)
            if(line.find('INFO:') > -1):
                info_count+= 1
            elif(line.find('ERROR:') > -1):
                error_count+= 1
            elif(line.find('WARNING:') > -1):
                warnings_count += 1

except FileNotFoundError:
    print(log_file_name,'File not found')
except Exception as ex:
    print(ex)

print("WARNINGS:",warnings_count)
print("ERRORS:",error_count)
print("INFO:",info_count)

