cmake_minimum_required(VERSION 2.8.3)
project(dataspeed_pds_can)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  nodelet
  can_msgs
  dataspeed_pds_msgs
  message_filters
  dataspeed_can_msg_filters
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_library(${PROJECT_NAME}
  src/nodelet.cpp
  src/PdsNode.cpp
)
add_dependencies(${PROJECT_NAME} dataspeed_pds_msgs_gencpp)
target_link_libraries(${PROJECT_NAME}
  ${catkin_LIBRARIES}
)

add_executable(${PROJECT_NAME}_node
  src/node.cpp
)
add_dependencies(${PROJECT_NAME}_node dataspeed_pds_msgs_gencpp)
target_link_libraries(${PROJECT_NAME}_node
  ${PROJECT_NAME}
)
set_target_properties(${PROJECT_NAME}_node PROPERTIES OUTPUT_NAME pds_node PREFIX "")

install(TARGETS ${PROJECT_NAME} ${PROJECT_NAME}_node
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
)
install(DIRECTORY include/${PROJECT_NAME}/
        DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)
install(FILES nodelets.xml
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

if (CATKIN_ENABLE_TESTING)
  add_subdirectory(tests)
endif()
