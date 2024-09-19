import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import EnvironmentVariable
from launch_ros.actions import Node
from pathlib import Path

def generate_launch_description():
    

    world = os.path.join( get_package_share_directory('world_gen'), 'generated', 'segmentation_world', 'segmentation_world.sdf')
    world_path = os.path.join(get_package_share_directory('world_gen'), 'generated', 'segmentation_world')
    gz_resource_path = SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=[
                                                EnvironmentVariable('IGN_GAZEBO_RESOURCE_PATH',
                                                                    default_value=''),
                                                                     world_path])

    

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
        os.path.join(
        get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
        )]), 
        launch_arguments={'gz_args': f'-r {world}'}.items(),
    )

    
    return LaunchDescription([
        gz_resource_path,
        gazebo
       
    ])
    