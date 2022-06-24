import os
for root, dirs, files in os.walk("U:\\teststring", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   print("Directories name below:")
   for name in dirs:
      print(os.path.join(root, name))