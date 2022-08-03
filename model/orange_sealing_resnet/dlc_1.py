#!/bin/env python

import deeplabcut

#print(deeplabcut.__version__)

path_config_file='/scratch/xp2027/lab_33_OrSSRnetXi/OrSsRnetXi/config.yaml'

video_path_1='/scratch/xp2027/lab_33_OrSSRnetXi/OrSsRnetXi/videos/orange01-train-2022-05-10-18.15.05.mp4'

save_path='/scratch/xp2027/lab_33_OrSSRnetXi/OrSsRnetXi/videos/iteration-1/'


#deeplabcut.load_demo_data(path_config_file)

#deeplabcut.create_training_dataset(path_config_file)
#deeplabcut.create_training_dataset(path_config_file, augmenter_type='imgaug', net_type='resnet_50', Shuffles=[0])

#deeplabcut.train_network(path_config_file, shuffle=0, displayiters=100, saveiters=2000, maxiters=40000)
#deeplabcut.train_network(path_config_file, shuffle=1, displayiters=100, saveiters=2000, maxiters=40000)
#deeplabcut.train_network(path_config_file, shuffle=2, displayiters=100, saveiters=2000, maxiters=40000)
#deeplabcut.train_network(path_config_file, shuffle=3, displayiters=100, saveiters=2000, maxiters=40000)


#deeplabcut.train_network(path_config_file,displayiters=100, saveiters=2000, maxiters=40000)


#deeplabcut.evaluate_network(path_config_file,plotting=True,Shuffles=[0])

#deeplabcut.evaluate_network(path_config_file,plotting=True)

#deeplabcut.analyze_videos(path_config_file, [video_path_1],destfolder=save_path, save_as_csv=True)
#deeplabcut.plot_trajectories(path_config_file,[video_path_1],  displayedbodyparts='all', destfolder=save_path)
#deeplabcut.create_labeled_video(path_config_file,[video_path_1], draw_skeleton = 'Yes', destfolder=save_path)

for i in range(0,1):
	shuffle='shuffle-'+str(i)
	deeplabcut.analyze_videos(path_config_file, [video_path_1], shuffle=i, destfolder=save_path+shuffle, save_as_csv=True, cropping=[140,410,135,380])
	deeplabcut.plot_trajectories(path_config_file,[video_path_1], shuffle=i, displayedbodyparts='all', destfolder=save_path+shuffle)
	deeplabcut.create_labeled_video(path_config_file,[video_path_1], draw_skeleton = 'Yes',shuffle=i, destfolder=save_path+shuffle)


