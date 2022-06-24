import os
import shutil
import time

print('Copying file started')
start = time.time()
count = 0
try:
   for root, dirs, files in os.walk('U:\\Mount Sinai\\MSN\\Raj_05Nov\\\Backup_05Nov\\All_835_on_5NOV'):
      for file in files:
         path_file = os.path.join(root,file)
         shutil.copy2(path_file,'U:\\Mount Sinai\MSN\\Raj_05Nov\\All_835_Till_5Nov')
         count = count+1
except FileNotFoundError:
   print("file not available")

print('Copying file complete')
print(str(count) + ' file copied')
done = time.time()
elapsed = done - start
print('Time Taken: ' + str(elapsed))