%define  debug_package %{nil}

Summary:    Korora configs for Cinnamon
Name:       korora-settings-cinnamon
Version:    0.2
Release:    1%{?dist}

Group:      System Environment/Base
License:    GPLv3+
Url:        http://kororaproject.org
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

%description
%{summary}.


%prep
%setup -q


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config

cp -a %{_builddir}/%{name}-%{version}/autostart %{buildroot}%{_sysconfdir}/skel/.config/
cp -a %{_builddir}/%{name}-%{version}/cinnamon %{buildroot}%{_sysconfdir}/skel/.cinnamon
cp -a %{_builddir}/%{name}-%{version}/plank %{buildroot}%{_sysconfdir}/skel/.config/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sysconfdir}/skel/.cinnamon/
%{_sysconfdir}/skel/.config/autostart/plank.desktop
%{_sysconfdir}/skel/.config/plank


%changelog
* Mon Jul 27 2015 Ian Firns <firnsy@kororaproject.org> 0.2-1
- Updated settings for Cinnamon

* Thu Jul 16 2015 Ian Firns <firnsy@kororaproject.org> 0.1-1
- Initial settings for Cinnamon
