Name:           ros-hydro-dwa-local-planner
Version:        1.11.14
Release:        0%{?dist}
Summary:        ROS dwa_local_planner package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/dwa_local_planner
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-hydro-base-local-planner
Requires:       ros-hydro-costmap-2d
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-nav-core
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-hydro-base-local-planner
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-costmap-2d
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-nav-core
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-pcl-conversions
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-tf

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
* Fri Dec 05 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

* Thu Oct 02 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

