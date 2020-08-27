%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-carrot-planner
Version:        1.17.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS carrot_planner package

License:        BSD
URL:            http://wiki.ros.org/carrot_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-noetic-base-local-planner
Requires:       ros-noetic-costmap-2d
Requires:       ros-noetic-nav-core
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-tf2
Requires:       ros-noetic-tf2-ros
BuildRequires:  eigen3-devel
BuildRequires:  ros-noetic-base-local-planner
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-costmap-2d
BuildRequires:  ros-noetic-nav-core
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-tf2
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-tf2-ros
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
This planner attempts to find a legal place to put a carrot for the robot to
follow. It does this by moving back along the vector between the robot and the
goal point.

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
* Thu Aug 27 2020 Aaron Hoy <ahoy@fetchrobotics.com> - 1.17.1-1
- Autogenerated by Bloom

* Thu Apr 02 2020 Aaron Hoy <ahoy@fetchrobotics.com> - 1.17.0-1
- Autogenerated by Bloom

