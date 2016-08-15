Name:           ros-indigo-clear-costmap-recovery
Version:        1.12.13
Release:        0%{?dist}
Summary:        ROS clear_costmap_recovery package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/clear_costmap_recovery
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-costmap-2d
Requires:       ros-indigo-nav-core
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-costmap-2d
BuildRequires:  ros-indigo-nav-core
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf

%description
This package provides a recovery behavior for the navigation stack that attempts
to clear space by reverting the costmaps used by the navigation stack to the
static map outside of a given area.

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Mon Aug 15 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.13-0
- Autogenerated by Bloom

* Fri Jun 24 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.12-0
- Autogenerated by Bloom

* Wed Jun 08 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.11-0
- Autogenerated by Bloom

* Fri May 27 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.10-0
- Autogenerated by Bloom

* Thu May 26 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.9-0
- Autogenerated by Bloom

* Mon May 16 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.8-0
- Autogenerated by Bloom

* Sat Feb 06 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.7-0
- Autogenerated by Bloom

* Sat Jan 02 2016 David V. Lu!! <davidvlu@gmail.com> - 1.12.6-0
- Autogenerated by Bloom

* Fri Oct 30 2015 David V. Lu!! <davidvlu@gmail.com> - 1.12.5-0
- Autogenerated by Bloom

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

