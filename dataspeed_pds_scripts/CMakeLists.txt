cmake_minimum_required(VERSION 2.8.3)
project(dataspeed_pds_scripts)

find_package(catkin REQUIRED COMPONENTS)

catkin_package()

install(DIRECTORY scripts/
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
        USE_SOURCE_PERMISSIONS
)
