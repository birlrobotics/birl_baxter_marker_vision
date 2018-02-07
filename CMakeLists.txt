cmake_minimum_required(VERSION 2.8.3)
project(birl_baxter_vision)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  geometry_msgs
  message_generation
)

# Generate services in the 'srv' folder
add_service_files(
  DIRECTORY srv
  FILES 
  get_pose.srv
  )

generate_messages(DEPENDENCIES
  geometry_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS
  std_msgs
  geometry_msgs
  message_runtime
)


