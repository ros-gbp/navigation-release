Name:           ros-indigo-fake-localization
Version:        1.12.6
Release:        0%{?dist}
Summary:        ROS fake_localization package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/fake_localization
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-filters
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-tf

%description
A ROS node that simply forwards odometry information.

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

