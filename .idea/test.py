import re
file = open('syslogClassShare.5', 'r')
aLine = 0

accessDenie = ""
clineError = ""
runTime = ""
transportError = ""
responeError = ""
w = ""
for line in file:
    aLine = aLine + 1
    if 'AccessDeniedException' in line:

        match = line[0:15]
        accessDenie = accessDenie + line + '\n' + 'Line Number: ' + str(aLine) + '\n' + 'date: ' + match + '\n\n'
    elif 'HttpClientErrorException' in line:
        match = line[0:15]
        clineError = clineError + line + '\n' + 'Line Number: ' + str(aLine) + '\n' + 'date: ' + match + '\n\n'
    elif 'RuntimeException' in line:
        match = line[0:15]
        runTime = runTime + line + '\n' + 'Line Number: ' + str(aLine) + '\n' + 'date: ' + match + '\n\n'
    elif 'transport error' in line:
        match = line[0:15]
        transportError = transportError + line + '\n' + 'Line Number: ' + str(aLine) + '\n' + 'date: ' + match + '\n\n'
    elif 'DefaultResponseErrorHandler' in line:
        match = line[0:15]
        responeError = responeError + line + '\n' + 'Line Number: ' + str(aLine) + '\n' + 'date: ' + match + '\n\n'
    elif 'WARN' in line:
        match = line[0:15]
        w = w + line + '\n' + 'Line Number: ' + str(aLine) + '\n' + 'date: ' + match + '\n\n'



print("================================================= Access Denied ================================================\n")
print accessDenie
print("================================================= Clined Error ================================================\n")
print clineError
print("================================================= Run Time ================================================\n")
print runTime
print("================================================= Transport Error ================================================\n")
print transportError
print("================================================= Respone Error ================================================\n")
print responeError
print("================================================= Warn Part ================================================\n")
print w