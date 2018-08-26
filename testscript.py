import os

counter=0;
for filename in os.listdir('data'):
    os.system('python run.py --model=mobilenet_thin --index={} --resize=432x368 --image=./data/{}'.format(counter, filename))
    counter+=1;
