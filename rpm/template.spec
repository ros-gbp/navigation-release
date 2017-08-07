Name:           ros-lunar-navigation
Version:        1.15.0
Release:        0%{?dist}
Summary:        ROS navigation package

Group:          Development/Libraries
License:        BSD,LGPL,LGPL (amcl)
URL:            http://wiki.ros.org/navigation
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-amcl
Requires:       ros-lunar-base-local-planner
Requires:       ros-lunar-carrot-planner
Requires:       ros-lunar-clear-costmap-recovery
Requires:       ros-lunar-costmap-2d
Requires:       ros-lunar-dwa-local-planner
Requires:       ros-lunar-fake-localization
Requires:       ros-lunar-global-planner
Requires:       ros-lunar-map-server
Requires:       ros-lunar-move-base
Requires:       ros-lunar-move-base-msgs
Requires:       ros-lunar-move-slow-and-clear
Requires:       ros-lunar-nav-core
Requires:       ros-lunar-navfn
Requires:       ros-lunar-robot-pose-ekf
Requires:       ros-lunar-rotate-recovery
Requires:       ros-lunar-voxel-grid
BuildRequires:  ros-lunar-catkin

%description
A 2D navigation stack that takes in information from odometry, sensor streams,
and a goal pose and outputs safe velocity commands that are sent to a mobile
base.

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

