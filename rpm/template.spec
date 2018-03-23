Name:           ros-lunar-base-local-planner
Version:        1.15.2
Release:        0%{?dist}
Summary:        ROS base_local_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/base_local_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       pcl-devel
Requires:       ros-lunar-angles
Requires:       ros-lunar-costmap-2d
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-nav-core
Requires:       ros-lunar-nav-msgs
Requires:       ros-lunar-pcl-ros
Requires:       ros-lunar-pluginlib
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-tf
Requires:       ros-lunar-visualization-msgs
Requires:       ros-lunar-voxel-grid
BuildRequires:  eigen3-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-lunar-angles
BuildRequires:  ros-lunar-catkin >= 0.5.68
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-costmap-2d
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-nav-core
BuildRequires:  ros-lunar-nav-msgs
BuildRequires:  ros-lunar-pcl-conversions
BuildRequires:  ros-lunar-pcl-ros
BuildRequires:  ros-lunar-pluginlib
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-rosunit
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-tf
BuildRequires:  ros-lunar-visualization-msgs
BuildRequires:  ros-lunar-voxel-grid

%description
This package provides implementations of the Trajectory Rollout and Dynamic
Window approaches to local robot navigation on a plane. Given a plan to follow
and a costmap, the controller produces velocity commands to send to a mobile
base. This package supports both holonomic and non-holonomic robots, any robot
footprint that can be represented as a convex polygon or circle, and exposes its
configuration as ROS parameters that can be set in a launch file. This package's
ROS wrapper adheres to the BaseLocalPlanner interface specified in the nav_core
package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Thu Mar 22 2018 David V. Lu!! <davidvlu@gmail.com> - 1.15.2-0
- Autogenerated by Bloom

* Mon Aug 14 2017 David V. Lu!! <davidvlu@gmail.com> - 1.15.1-0
- Autogenerated by Bloom

* Mon Aug 07 2017 David V. Lu!! <davidvlu@gmail.com> - 1.15.0-0
- Autogenerated by Bloom

* Thu Jul 13 2017 David V. Lu!! <davidvlu@gmail.com> - 1.14.0-0
- Autogenerated by Bloom

