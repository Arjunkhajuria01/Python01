#how to make folders 
import os 
# os.mkdir("data")
# for i in range(100):
#     os.mkdir(f"data/Day{i+1}")

    # renaming these folders 
for i in range (0,100):
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")

