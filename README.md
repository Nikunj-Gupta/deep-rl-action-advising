# Deep RL Action Advising Framework

DQN model checkpoints for the teacher(s) can be found in this [link](https://drive.google.com/drive/folders/1alwLhNBVYdGmm_1tAy22elaq-alSpDCZ?usp=sharing).

# Installation instructions 

```
virtualenv ~/virtualenvs/VENV 
source ~/virtualenvs/VENV/bin/activate 
pip install -r requirements.txt 
pip install gym[atari]
python3 code/main.py --env-key ALE-Pong --seed 0 
```

#### You might need atari ROMS 
Follow Instructions as given here: https://github.com/openai/atari-py#roms 

# Running instructions 

```
python3 code/main.py --env-key ALE-Pong --seed 0 
```

