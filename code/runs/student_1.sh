#!/bin/bash
#SBATCH --account=rrg-mtaylor3
#SBATCH --gres=gpu:2        # request GPU generic resource
#SBATCH --cpus-per-task=2   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=32000M        # memory per node
#SBATCH --time=0-16:00      # time (DD-HH:MM)
#SBATCH --output=cudapong_1000-%j.out  # %N for node name, %j for jobID
#SBATCH --error=errcudapong_1000%A.err   # %A for jobID

module load cuda cudnn
module load python/3.7
source ../../../venvs/tsrl/bin/activate 

python ../main.py --env-key BOX2D-LunarLander --seed 10 --config-set 2000 
python ../main.py --env-key BOX2D-LunarLander --seed 10 --config-set 2100 