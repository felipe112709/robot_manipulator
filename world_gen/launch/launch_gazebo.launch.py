import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, AppendEnvironmentVariable, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    

    world = os.path.join( get_package_share_directory('world_gen'), 'generated', 'segmentation_world', 'segmentation_world.sdf')

    rviz_config_file = os.path.join( get_package_share_directory('world_gen'),'config','config.rviz')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    declare_use_sim_time_cmd = DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true')    



    gz_resource_path_world= AppendEnvironmentVariable(
            'IGN_GAZEBO_RESOURCE_PATH',
            os.path.join(get_package_share_directory('world_gen'), 'generated', 'segmentation_world'))
    
    gz_resource_path_robot = AppendEnvironmentVariable(
            'IGN_GAZEBO_RESOURCE_PATH',
            os.path.join(get_package_share_directory('world_gen'),'meshes'))

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
        os.path.join(
        get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
        )]), 
        launch_arguments={'gz_args': f'-r {world}'}.items(),
    )

    
    # urdf_file = os.path.join(
    #     get_package_share_directory('world_gen'),
    #     'urdf',
    #     'ur5e.urdf'  
    # )
    # with open(urdf_file, 'r') as infp:
    #     robot_desc= infp.read()

    sdf_path = os.path.join(
        get_package_share_directory('world_gen'),
        'models',
        'ur5e.sdf'
    )

    # joint_state_publisher_node = Node(
    #     package="joint_state_publisher_gui",
    #     executable="joint_state_publisher_gui",
    # )
    # Nodo del publicador de estado del robot


    # nueva linea de prueba

    # robot_state_publisher_node = Node(
    #     package="robot_state_publisher",
    #     executable="robot_state_publisher",
    #     output="both",
    #     parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
    # )
    
    
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'ur5e',
            '-file', sdf_path,
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.0'

        ],
        output='screen'
    )
    
    # rviz_node = Node(
    #     package="rviz2",
    #     executable="rviz2",
    #     name="rviz2",
    #     output="log",
    #     arguments=["-d", rviz_config_file],
    # )
    return LaunchDescription([
        declare_use_sim_time_cmd,
        gz_resource_path_world,
        gz_resource_path_robot,
        gazebo,
        # set_robot_resources,
        # robot_state_publisher_node,
        # joint_state_publisher_node, 
        spawn_entity,
        # rviz_node,
        
    ])
    