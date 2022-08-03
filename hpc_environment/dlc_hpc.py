#!/bin/env python

import deeplabcut


path_config_file='/scratch/xp2027/lab_39_YlSsRnetCh/YlSsRnetChen/config.yaml'
video_path_1='/scratch/xp2027/lab_39_YlSsRnetCh/YlSsRnetChen/videos/yellow01-train-2022-06-04-18.56.16.mp4'
save_path='/scratch/xp2027/lab_39_YlSsRnetCh/YlSsRnetChen/videos/iteration-0/'

deeplabcut.create_training_dataset(path_config_file, augmenter_type='imgaug', net_type='resnet_50', Shuffles=[0])
#deeplabcut.create_training_model_comparison(path_config_file,net_types=["resnet_50","mobilenet_v2_1.0","mobilenet_v2_0.75","efficientnet-b6"], augmenter_types=["imgaug"])

deeplabcut.train_network(path_config_file, shuffle=0, displayiters=100, saveiters=2000, maxiters=40000)

deeplabcut.evaluate_network(path_config_file,plotting=True,Shuffles=[0])

deeplabcut.analyze_videos(path_config_file, [video_path_1], shuffle=0, destfolder=save_path, save_as_csv=True, cropping=[140,410,120,360])

deeplabcut.plot_trajectories(path_config_file,[video_path_1], shuffle=0, displayedbodyparts='all', destfolder=save_path)

deeplabcut.create_labeled_video(path_config_file,[video_path_1], shuffle=0, draw_skeleton = 'Yes', destfolder=save_path)