Name:           ros-lunar-nav-core
Version:        1.15.0
Release:        0%{?dist}
Summary:        ROS nav_core package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/nav_core
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-costmap-2d
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-tf
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-costmap-2d
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-tf

%description
This package provides common interfaces for navigation specific robot actions.
Currently, this package provides the BaseGlobalPlanner, BaseLocalPlanner, and
RecoveryBehavior interfaces, which can be used to build actions that can easily
swap their planner, local controller, or recovery behavior for new versions
adhering to the same interface.

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
* Mon Aug 07 2017 David V. Lu!! <davidvlu@gmail.com> - 1.15.0-0
- Autogenerated by Bloom

* Thu Jul 13 2017 David V. Lu!! <davidvlu@gmail.com> - 1.14.0-0
- Autogenerated by Bloom

