#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=6:00:00
#SBATCH --mem-per-cpu=10G

#SBATCH --gres=gpu:1
##SBATCH --gres=gpu:1g.10gb:1
#SBATCH --job-name=deeplabcut

module purge

singularity exec --nv \
	    --overlay /scratch/xp2027/pytorch-example/my_pytorch.ext3:ro \
	    /scratch/work/public/singularity/cuda11.2.2-cudnn8-devel-ubuntu20.04.sif \
	    /bin/bash -c "source /ext3/miniconda3/bin/activate ; python /scratch/xp2027/lab_33_OrSSRnetXi/dlc_1.py"
