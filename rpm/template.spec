%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-amcl
Version:        1.17.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS amcl package

License:        LGPL
URL:            http://wiki.ros.org/amcl
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-rosbag
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-srvs
Requires:       ros-noetic-tf2
Requires:       ros-noetic-tf2-msgs
Requires:       ros-noetic-tf2-ros
BuildRequires:  python3-pykdl
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-map-server
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-rosbag
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-srvs
BuildRequires:  ros-noetic-tf2
BuildRequires:  ros-noetic-tf2-geometry-msgs
BuildRequires:  ros-noetic-tf2-msgs
BuildRequires:  ros-noetic-tf2-ros
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
amcl is a probabilistic localization system for a robot moving in 2D. It
implements the adaptive (or KLD-sampling) Monte Carlo localization approach (as
described by Dieter Fox), which uses a particle filter to track the pose of a
robot against a known map. This node is derived, with thanks, from Andrew
Howard's excellent 'amcl' Player driver.

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
* Thu Aug 27 2020 David V. Lu!! <davidvlu@gmail.com> - 1.17.1-1
- Autogenerated by Bloom

* Thu Apr 02 2020 David V. Lu!! <davidvlu@gmail.com> - 1.17.0-1
- Autogenerated by Bloom

