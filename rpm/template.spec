Name:           ros-indigo-navfn
Version:        1.12.4
Release:        0%{?dist}
Summary:        ROS navfn package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/navfn
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nav-core
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pcl-conversions
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
Requires:       ros-indigo-visualization-msgs
BuildRequires:  netpbm-devel
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-core
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-visualization-msgs

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
* Wed Jun 03 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.4-0
- Autogenerated by Bloom

* Thu Apr 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.3-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.2-0
- Autogenerated by Bloom

* Sat Mar 14 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.1-0
- Autogenerated by Bloom

* Wed Feb 04 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

* Fri Dec 05 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.14-0
- Autogenerated by Bloom

* Thu Oct 02 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

* Wed Oct 01 2014 David V. Lu!! <davidvlu@gmail.com> - 1.11.12-0
- Autogenerated by Bloom

