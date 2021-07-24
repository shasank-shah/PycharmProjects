from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine

print("\n")
print(machine())

from platform import processor

print("\n")
print(processor())

from platform import system

print("\n")
print(system())

from platform import version

print("\n")
print(version())

from platform import python_implementation, python_version_tuple

print("\n")
print(python_implementation())
for atr in python_version_tuple():
    print(atr)
