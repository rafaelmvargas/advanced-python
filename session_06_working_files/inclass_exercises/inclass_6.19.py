# 6.19:  Set PYTHONPATH environment variable to make utils.py
# importable from any directory.

# Move (don't copy) temputils.py to your Desktop.  This can be
# done through the PyCharm file view or your Finder or Windows
# Explorer windows.
# 
# If you are using Jupyter Notebook, for this exercise you
# must first restart the kernel.  Click the circular arrow in
# the menu bar, or Kernel -> Restart (no outputs will be
# cleared from your notebook).
# 
# Run the below exercise and note the ModuleNotFoundError,
# which indicates that the module can no longer be located.
# This is because it is not in the same directory as this
# exercise file.

import temputils as tu

val = tu.ftoc(212)
print(val)             # 100.0

val2 = tu.ctof(0)
print(val2)            # 32.0


# Now follow the directions under the slide Setting the
# PYTHONPATH Environment Variable to set or add your Desktop
# path there:
# 
# The most common locations for Desktop are:
# 
# Windows:  C:\Users\username\Desktop
# Mac:  /Users/username/Desktop
# 
# Where username is the name of your home directory.
# 
# Finally, run the code again and see that the module was
# found in its new location.

# Expected Output:

# 100.0
# 32.0

