%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-dataspeed-pds-rqt
Version:        1.0.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS dataspeed_pds_rqt package

License:        BSD
URL:            http://dataspeedinc.com
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-dataspeed-pds-msgs
Requires:       ros-noetic-python-qt-binding
Requires:       ros-noetic-rospy
Requires:       ros-noetic-rqt-gui
Requires:       ros-noetic-rqt-gui-py
BuildRequires:  python3-setuptools
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-dataspeed-pds-msgs
BuildRequires:  ros-noetic-python-qt-binding
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-rqt-gui
BuildRequires:  ros-noetic-rqt-gui-py
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS rqt GUI for the Dataspeed Inc. Power Distribution System (PDS)

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Jul 09 2020 Kevin Hallenbeck <khallenbeck@dataspeedinc.com> - 1.0.3-1
- Autogenerated by Bloom

