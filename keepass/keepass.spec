Summary:        Cross-platform password manager
Name:           keepass
Version:        2.23
Release:        1%{?dist}
License:        GPLv2+
Group:          Applications/System
URL:            http://keepass.info/
Source0:        http://downloads.sourceforge.net/keepass/KeePass-%{version}.zip
Source1:        http://upload.wikimedia.org/wikipedia/commons/1/19/KeePass_icon.png
Source2:        keepass.desktop
Source3:        keepass.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  unzip
Requires:       mono-core > 2.6
Requires:       mono-winforms > 2.6

%description
KeePass is a free open source password manager, which helps you to manage your
passwords in a secure way. You can put all your passwords in one database,
which is locked with one master key or a key file.

%prep
%setup -qc %{name}-%{version}

%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cp} -R *  %{buildroot}%{_datadir}/%{name}/
%{__cp} %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
%{__sed} -e 's#@datadir@#%{_datadir}#' \
    %{SOURCE2} > %{buildroot}%{_datadir}/applications/keepass.desktop
%{__sed} -e 's#@datadir@#%{_datadir}#' \
    %{SOURCE3} > %{buildroot}%{_bindir}/keepass


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/keepass.desktop
%attr(755,root,root) %{_bindir}/keepass

%changelog
* Wed Sep 18 2013 Didier Fabert <didier.fabert@gmail.com> 2.23-1
- First Import

