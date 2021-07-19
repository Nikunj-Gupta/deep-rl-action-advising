import os 
text = """ 
#!/bin/bash
#SBATCH --account=rrg-mtaylor3
#SBATCH --cpus-per-task=4   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=32000M        # memory per node
#SBATCH --time=0-16:00      # time (DD-HH:MM)
#SBATCH --output=out_lunarlander_1000-%j.out  # %N for node name, %j for jobID
#SBATCH --error=err_lunarlander_1000%A.err   # %A for jobID

module load python/3.7
source ../../../venvs/tsrl/bin/activate 

"""
commands = [
    "python ../main.py --env-key BOX2D-LunarLander --config-set 0 --seed ", 
    "python ../main.py --env-key BOX2D-LunarLander --config-set 1000 --seed ", 
    "#python ../main.py --env-key BOX2D-LunarLander --config-set 2000 --seed ", 
    "#python ../main.py --env-key BOX2D-LunarLander --config-set 2100 --seed ", 
    "#python ../main.py --env-key BOX2D-LunarLander --config-set 5000 --seed ", 
    "#python ../main.py --env-key BOX2D-LunarLander --config-set 5100 --seed ", 
    "#python ../main.py --env-key BOX2D-LunarLander --config-set 6000 --seed ", 
    "#python ../main.py --env-key BOX2D-LunarLander --config-set 7000 --seed ", 
    "#python ../main.py --env-key BOX2D-LunarLander --config-set 8000 --seed "
    ]



for seed in range(10): 
    c=""
    for command in commands: 
        c += command+str(seed)+os.linesep 
    with open("code/runs/run_" + str(seed)+ ".sh", "w") as f:
        f.write(text+c) 

    
