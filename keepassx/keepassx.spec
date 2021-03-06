Name:           keepassx
Version:        2.0.2
Release:        1%{?dist}
Summary:        Cross-platform password manager
Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://keepassx.sourceforge.net
Source0:        https://github.com/didier13150/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libXtst-devel
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  libgcrypt-devel
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme
Requires:       libgcrypt
Epoch:          2

%description
KeePassX is an application for people with extremely high demands on secure
personal data management.
KeePassX saves many different information e.g. user names, passwords, URLs,
attachments and comments in one single database. For a better management
user-defined titles and icons can be specified for each single entry.
Furthermore the entries are sorted in groups, which are customizable as well.
The integrated search function allows to search in a single group or the
complete database.
KeePassX offers a little utility for secure password generation. The password
generator is very customizable, fast and easy to use. Especially someone who
generates passwords frequently will appreciate this feature.
The complete database is always encrypted either with AES (alias Rijndael) or
Twofish encryption algorithm using a 256 bit key. Therefore the saved
information can be considered as quite safe. KeePassX uses a database format
that is compatible with KeePass Password Safe for MS Windows version 2.

%prep
%setup -qn %{name}

%build
mkdir build
cd build
cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DWITH_GUI_TESTS=OFF

make %{?_smp_mflags}

%install
cd build
make install DESTDIR=%{buildroot}

# Menu
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cp} %{SOURCE1}  %{buildroot}%{_datadir}/applications/%{name}.desktop
        
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --delete-original \
        --add-mime-type application/x-keepass \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

# Associate KDB* files
cat > x-keepassx.desktop << EOF
[Desktop Entry]
Comment=
Hidden=false
Icon=keepassx.png
MimeType=application/x-keepassx
Patterns=*.kdb;*.KDB;*.kdbx;*.KDBX*
Type=MimeType
EOF
install -D -m 644 -p x-keepassx.desktop \
  %{buildroot}%{_datadir}/mimelnk/application/x-keepassx.desktop

%check
cd build
make test

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null ||:
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null ||:
update-mime-database %{_datadir}/mime &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc CHANGELOG INSTALL COPYING LICENSE*

%{_bindir}/keepassx
%{_libdir}/keepassx/*.so
%{_datadir}/keepassx
%{_datadir}/applications/*.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/icons/hicolor/*/*/*keepassx.*
%{_datadir}/mime/packages/keepassx.xml

%changelog
* Wed Jun 15 2016 Didier Fabert <didier.fabert@gmail.com> - 2:2.0.2-1
- New upstream version
- Increment epoch

* Tue Jan 05 2016 Didier Fabert <didier.fabert@gmail.com> - 2.0.1-1
- New upstream version (2.0)

* Tue Nov 10 2015 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.8.beta2.1
- Sync to upstream

* Tue Sep 22 2015 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.7.beta2.1
- Modify systray menu action text (to be translated)

* Mon Sep 21 2015 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.6.beta2.1
- Resize about Window

* Mon Sep 21 2015 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.5.beta2.1
- Rebuild with modified sources

* Fri Sep 18 2015 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.4.beta2.1
- Sync to upstream

* Sat Apr 19 2014 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.3.alpha6.1
- Sync to upstream

* Fri Mar 28 2014 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.3.alpha5.2
- Sync to upstream

* Sun Mar 23 2014 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.3.alpha5.1
- Sync to upstream

* Tue Nov 26 2013 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.3.alpha4
- BUGFIX: multiple icons on systray when settings was edited

* Sun Nov 10 2013 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.2.alpha4
- Patch to change welcome page

* Sat Nov 09 2013 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.1.alpha4
- Patch to add systray icon capability

* Fri Sep 20 2013 Didier Fabert <didier.fabert@gmail.com> - 2.0-0.alpha4
- Update to 2.0 version (alpha)

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.4.3-7
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Tom Callaway <spot@fedoraproject.org> - 0.4.3-5
- fix FTBFS on gcc 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 14 2010 Aurelien Bompard <abompard@fedoraproject.org> -  0.4.3-1
- version 0.4.3

* Sun Jan 03 2010 Aurelien Bompard <abompard@fedoraproject.org> -  0.4.1-1
- version 0.4.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-2
- add patch0 to fix bug 496035

* Thu Mar 26 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.4.0-1
- version 0.4.0
- drop patch0 (upstream)

* Thu Mar 12 2009 Aurelien Bompard <abompard@fedoraproject.org> 0.3.4-3
- backport fix from upstream for bug #489820

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 11 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.4-1
- version 0.3.4

* Sat Aug 23 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.3-2
- rebase patch for version 0.3.3

* Tue Aug 12 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.3-1
- version 0.3.3

* Mon Jul 21 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.2-1
- version 0.3.2

* Sun Mar 16 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.1-1
- version 0.3.1
- drop xdg patch, keepassx now uses QDesktopServices

* Wed Mar 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-3.a
- version 0.3.0a

* Wed Mar 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-2
- patch for gcc 4.3

* Sun Mar 02 2008 Aurelien Bompard <abompard@fedoraproject.org> 0.3.0-1
- version 0.3.0
- drop helpwindow patch (feature dropped upstream)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.2-5
- Autorebuild for GCC 4.3

* Sun Oct 07 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-4
- use xdg-open instead of htmlview

* Sat Aug 25 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-3
- fix license tag
- rebuild for BuildID

* Wed Jun 27 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-2
- fix help button
- use htmlview instead of the hardcoded konqueror

* Sun Mar 04 2007 Aurelien Bompard <abompard@fedoraproject.org> 0.2.2-1
- initial package
