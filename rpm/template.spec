%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-global-planner
Version:        1.16.3
Release:        1%{?dist}
Summary:        ROS global_planner package

License:        BSD
URL:            http://wiki.ros.org/global_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-costmap-2d
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-nav-core
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-navfn
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-tf2-ros
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-costmap-2d
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-nav-core
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-navfn
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-tf2-geometry-msgs
BuildRequires:  ros-melodic-tf2-ros

%description
A path planner library and node.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Fri Nov 15 2019 David V. Lu!! <davidvlu@gmail.com> - 1.16.3-1
- Autogenerated by Bloom

* Tue Jul 31 2018 David V. Lu!! <davidvlu@gmail.com> - 1.16.2-0
- Autogenerated by Bloom

* Sat Jul 28 2018 David V. Lu!! <davidvlu@gmail.com> - 1.16.1-0
- Autogenerated by Bloom

* Wed Jul 25 2018 David V. Lu!! <davidvlu@gmail.com> - 1.16.0-0
- Autogenerated by Bloom

