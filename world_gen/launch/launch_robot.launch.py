import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    rviz_config_file = os.path.join(
        get_package_share_directory('world_gen'),'config','config.rviz'
    )
    urdf_file = os.path.join(
        get_package_share_directory('world_gen'),'urdf','ur5e.urdf'  
    )
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()


    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )
    # Nodo del publicador de estado del robot


    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[{ 'robot_description': robot_desc}],
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", rviz_config_file],
    )


    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_node,  
        rviz_node,  
    ])
    