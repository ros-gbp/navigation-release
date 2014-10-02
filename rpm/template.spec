Name:           ros-hydro-navfn
Version:        1.11.12
Release:        0%{?dist}
Summary:        ROS navfn package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/navfn
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-costmap-2d
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-nav-core
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-pcl-conversions
Requires:       ros-hydro-pcl-ros
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-tf
Requires:       ros-hydro-visualization-msgs
BuildRequires:  netpbm-devel
BuildRequires:  ros-hydro-catkin >= 0.5.68
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-costmap-2d
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-nav-core
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-pcl-conversions
BuildRequires:  ros-hydro-pcl-ros
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-rosconsole
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-visualization-msgs

%description
navfn provides a fast interpolated navigation function that can be used to
create plans for a mobile base. The planner assumes a circular robot and
operates on a costmap to find a minimum cost plan from a start point to an end
point in a grid. The navigation function is computed with Dijkstra's algorithm,
but support for an A* heuristic may also be added in the near future. navfn also
provides a ROS wrapper for the navfn planner that adheres to the
nav_core::BaseGlobalPlanner interface specified in nav_core.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

