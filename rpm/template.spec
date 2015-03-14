Name:           ros-indigo-dwa-local-planner
Version:        1.12.1
Release:        0%{?dist}
Summary:        ROS dwa_local_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/dwa_local_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-base-local-planner
Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-nav-core
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-base-local-planner
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-nav-core
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf

%description
This package provides an implementation of the Dynamic Window Approach to local
robot navigation on a plane. Given a global plan to follow and a costmap, the
local planner produces velocity commands to send to a mobile base. This package
supports any robot who's footprint can be represented as a convex polygon or
cicrle, and exposes its configuration as ROS parameters that can be set in a
launch file. The parameters for this planner are also dynamically
reconfigurable. This package's ROS wrapper adheres to the BaseLocalPlanner
interface specified in the nav_core package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Mar 14 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-0
- Autogenerated by Bloom

* Wed Feb 04 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

