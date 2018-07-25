Name:           ros-melodic-move-slow-and-clear
Version:        1.16.0
Release:        0%{?dist}
Summary:        ROS move_slow_and_clear package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/move_slow_and_clear
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-costmap-2d
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-nav-core
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-costmap-2d
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-nav-core
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp

%description
move_slow_and_clear

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
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

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Jul 25 2018 David V. Lu!! <davidvlu@gmail.com> - 1.16.0-0
- Autogenerated by Bloom

