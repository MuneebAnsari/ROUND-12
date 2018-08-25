import os

for filename in os.listdir('data'):
    print(filename)
    os.system('python run.py --model=mobilenet_thin --resize=432x368 --image=./data/'+filename)
