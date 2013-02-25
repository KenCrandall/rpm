%define us_ver %(echo %{version} | sed -e 's/\\\./_/g')
Name:           povtree
Version:        1.5
Release:        1%{?dist}
Summary:        Tree generation for povray
License:        GPLv2
Group:          Applications/Multimedia
URL:            http://web.archive.org/web/20071101052625/propro.ru/go/Wshop/povtree/download.html
Source0:        http://web.archive.org/web/20071101052625/propro.ru/go/Wshop/povtree/%{name}%{version}.zip
Source1:        %{name}.desktop
Source2:        %{name}

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
Requires:       java
Requires:       jpackage-utils

%description
POV-Tree is a Java tree generator for POV-Ray. Tree generation algorithm
which is used in this program was based on TOMTREE macro developed by
Tom Aust.

You can think of this program as of GUI for that macro. In addition to the
possibility to define numerous parameters you can also preview tree and
save it either as an include file or as a mesh file.

%prep
%setup -qc %{name}%{version}

%build
%{__rm} -f build.xml
%{__rm} -rf src test

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/applications
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_javadir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%{__install} *.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications
%{__install} %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
%{__install} %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}
%{__cp} -r doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%{__cp} -r pov $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__cp} -r trees $RPM_BUILD_ROOT%{_datadir}/%{name}

sed -i -e 's#@datadir@#%{_javadir}/%{name}#' $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}*
%{_javadir}/%{name}
%{_javadocdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%doc COPYING README

%changelog
* Sat Feb 16 2013 Didier Fabert <didier.fabert@gmail.com> 1.9.8-1
- First Release