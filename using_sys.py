import sys # the sys library refers to the system where Python is running
import os  # the os library refers to the operating system

print(sys.platform)
print(sys.version_info)

# what about import... Python will always search for a module when we import
# it will search the path
sys.path.append('c:')
print(sys.path)

print(os.get_exec_path())
