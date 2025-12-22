name="Engineering College"
name2="Sidhartha Engineering College"
Length=len(name)
print(Length)

print(name[0:Length-3])
# "egelloc gnireenignE"

print(name[0:Length:2])
print(name[0:Length:4])

print(name[0:Length:1])

print(name[Length-1:-1:-1],"Line 14")
# 18,0,-1
# 18,-1,-1
# print(name[:])
# print(name[::-1])

print(name[-1:-len(name)-1:-1])