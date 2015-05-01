Name:           ros-hydro-base-local-planner
Version:        1.11.16
Release:        0%{?dist}
Summary:        ROS base_local_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/base_local_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-hydro-angles
Requires:       ros-hydro-costmap-2d
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-generation
Requires:       ros-hydro-nav-core
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-pcl-ros
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-tf
Requires:       ros-hydro-visualization-msgs
Requires:       ros-hydro-voxel-grid
BuildRequires:  eigen3-devel
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-catkin >= 0.5.68
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-costmap-2d
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-nav-core
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-pcl-conversions
BuildRequires:  ros-hydro-pcl-ros
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-rosconsole
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-voxel-grid

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
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Apr 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.11.16-0
- Autogenerated by Bloom

* Tue Feb 03 2015 David V. Lu!! <davidvlu@gmail.com> - 1.11.15-0
- Autogenerated by Bloom

* Fri Dec 05 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

* Thu Oct 02 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

