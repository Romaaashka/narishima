
byte = int(input("entered number "))
kiloBytes = (byte/1024)
megaBytes = (kiloBytes/1024)

print(" ")
print(byte, " bytes")
print( "% 3f" % kiloBytes, " kilobytes")
print( "% 3f" % megaBytes, " megabytes")
