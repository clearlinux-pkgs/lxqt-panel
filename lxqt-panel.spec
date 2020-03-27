#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x42C9C8D3AF5EA5E3 (agaida@siduction.org)
#
Name     : lxqt-panel
Version  : 0.14.1
Release  : 3
URL      : https://downloads.lxqt.org/downloads/lxqt-panel/0.14.1/lxqt-panel-0.14.1.tar.xz
Source0  : https://downloads.lxqt.org/downloads/lxqt-panel/0.14.1/lxqt-panel-0.14.1.tar.xz
Source99 : https://downloads.lxqt.org/downloads/lxqt-panel/0.14.1/lxqt-panel-0.14.1.tar.xz.asc
Summary  : The LXQt desktop panel
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-panel-bin = %{version}-%{release}
Requires: lxqt-panel-data = %{version}-%{release}
Requires: lxqt-panel-lib = %{version}-%{release}
Requires: lxqt-panel-license = %{version}-%{release}
Requires: lxqt-panel-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libpulse)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libdbusmenu-dev
BuildRequires : libdbusmenu-qt-dev
BuildRequires : liblxqt-dev
BuildRequires : libsysstat-dev
BuildRequires : lm-sensors-dev
BuildRequires : lxqt-build-tools
BuildRequires : lxqt-globalkeys-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xrender)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qttools-dev

%description
# lxqt-panel
## Overview
`lxqt-panel` represents the taskbar of LXQt.
The elements available in lxqt-panel are called "plugin" technically. This applies e. g. to the source code where they reside in directories `./plugin-<plugin>` like `plugin-mainmenu`. In contrast to this they are called "widgets" by the configuration GUI so far. Also, a more descriptive term is used to refer to distinct plugins within the GUI. E. g. the aforementioned `plugin-mainmenu` is called "Application menu" that way.
Configuration dialogue "Add Plugins", see [below](https://github.com/lxqt/lxqt-panel#customizing), is listing all available plugins plus a short description and hence provides an overview of the available ones.
Notes on some of the plugins, sorted by terms used within the GUI in alphabetical order, technical term in parenthesis:

%package bin
Summary: bin components for the lxqt-panel package.
Group: Binaries
Requires: lxqt-panel-data = %{version}-%{release}
Requires: lxqt-panel-license = %{version}-%{release}

%description bin
bin components for the lxqt-panel package.


%package data
Summary: data components for the lxqt-panel package.
Group: Data

%description data
data components for the lxqt-panel package.


%package dev
Summary: dev components for the lxqt-panel package.
Group: Development
Requires: lxqt-panel-lib = %{version}-%{release}
Requires: lxqt-panel-bin = %{version}-%{release}
Requires: lxqt-panel-data = %{version}-%{release}
Requires: lxqt-panel-man = %{version}-%{release}
Provides: lxqt-panel-devel = %{version}-%{release}
Requires: lxqt-panel = %{version}-%{release}

%description dev
dev components for the lxqt-panel package.


%package lib
Summary: lib components for the lxqt-panel package.
Group: Libraries
Requires: lxqt-panel-data = %{version}-%{release}
Requires: lxqt-panel-license = %{version}-%{release}

%description lib
lib components for the lxqt-panel package.


%package license
Summary: license components for the lxqt-panel package.
Group: Default

%description license
license components for the lxqt-panel package.


%package man
Summary: man components for the lxqt-panel package.
Group: Default

%description man
man components for the lxqt-panel package.


%prep
%setup -q -n lxqt-panel-0.14.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551233746
mkdir -p clr-build
pushd clr-build
%cmake .. -DCPULOAD_PLUGIN=false -DNETWORKMONITOR_PLUGIN=false
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1551233746
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-panel
cp LICENSE %{buildroot}/usr/share/package-licenses/lxqt-panel/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lxqt-panel

%files data
%defattr(-,root,root,-)
/usr/share/desktop-directories/lxqt-leave.directory
/usr/share/desktop-directories/lxqt-settings.directory
/usr/share/lxqt/lxqt-panel/colorpicker.desktop
/usr/share/lxqt/lxqt-panel/desktopswitch.desktop
/usr/share/lxqt/lxqt-panel/directorymenu.desktop
/usr/share/lxqt/lxqt-panel/kbindicator.desktop
/usr/share/lxqt/lxqt-panel/mainmenu.desktop
/usr/share/lxqt/lxqt-panel/mount.desktop
/usr/share/lxqt/lxqt-panel/quicklaunch.desktop
/usr/share/lxqt/lxqt-panel/sensors.desktop
/usr/share/lxqt/lxqt-panel/showdesktop.desktop
/usr/share/lxqt/lxqt-panel/spacer.desktop
/usr/share/lxqt/lxqt-panel/statusnotifier.desktop
/usr/share/lxqt/lxqt-panel/sysstat.desktop
/usr/share/lxqt/lxqt-panel/taskbar.desktop
/usr/share/lxqt/lxqt-panel/tray.desktop
/usr/share/lxqt/lxqt-panel/volume.desktop
/usr/share/lxqt/lxqt-panel/worldclock.desktop
/usr/share/lxqt/panel.conf
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_ca.qm
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_cy.qm
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_da.qm
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_de.qm
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_gl.qm
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_pl.qm
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/colorpicker/colorpicker_tr.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_ar.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_ca.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_cs.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_cy.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_da.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_de.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_el.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_eo.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_es.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_es_UY.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_eu.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_fi.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_fr.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_gl.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_he.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_hr.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_hu.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_ia.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_id.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_it.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_ja.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_ko.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_lt.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_nl.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_pl.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_pt.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_ru.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_sk_SK.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_sl.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_sr@latin.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_sr_BA.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_sr_RS.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_tr.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_uk.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/desktopswitch/desktopswitch_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_ar.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_ca.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_cs.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_cy.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_da.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_de.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_el.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_es.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_fr.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_gl.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_he.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_hr.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_hu.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_id.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_it.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_ja.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_lt.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_nl.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_pl.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_pt.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_ru.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_tr.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_uk.qm
/usr/share/lxqt/translations/lxqt-panel/directorymenu/directorymenu_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_ar.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_ca.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_cs.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_cy.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_da.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_de.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_el.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_es.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_fr.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_gl.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_he.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_hr.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_hu.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_id.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_it.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_ja.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_lt.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_nl.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_pl.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_pt.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_ru.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_tr.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_uk.qm
/usr/share/lxqt/translations/lxqt-panel/kbindicator/kbindicator_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_ar.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_ca.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_cs.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_cy.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_da.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_de.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_el.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_eo.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_es.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_es_UY.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_eu.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_fa.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_fi.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_fr.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_gl.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_he.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_hr.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_hu.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_ia.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_id.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_it.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_ja.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_ko.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_lt.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_nl.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_pl.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_pt.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_ru.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_sk_SK.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_sl.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_sr@latin.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_sr_BA.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_sr_RS.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_tr.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_uk.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/lxqt-panel_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_ar.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_ca.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_cs.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_cy.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_da.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_de.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_el.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_eo.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_es.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_es_UY.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_eu.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_fi.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_fr.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_gl.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_he.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_hr.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_hu.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_ia.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_id.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_it.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_ja.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_ko.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_lt.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_nl.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_pl.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_pt.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_ru.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_sk_SK.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_sl.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_sr@latin.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_sr_BA.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_sr_RS.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_tr.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_uk.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/mainmenu/mainmenu_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_ar.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_ca.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_cs.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_cy.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_da.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_de.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_el.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_eo.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_es.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_es_UY.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_eu.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_fi.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_fr.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_gl.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_he.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_hr.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_hu.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_ia.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_id.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_it.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_ja.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_ko.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_lt.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_nl.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_pl.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_pt.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_ru.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_sk_SK.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_sl.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_sr@latin.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_sr_BA.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_sr_RS.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_tr.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_uk.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/mount/mount_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_ar.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_ca.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_cs.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_cy.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_da.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_de.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_el.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_eo.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_es.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_eu.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_fi.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_fr.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_gl.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_hu.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_ia.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_id.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_it.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_ja.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_ko.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_lt.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_nl.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_pl.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_pt.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_ru.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_sk_SK.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_sl.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_sr@latin.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_sr_BA.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_sr_RS.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_tr.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_uk.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/quicklaunch/quicklaunch_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_ar.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_ca.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_cs.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_cy.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_da.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_de.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_el.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_es.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_eu.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_fi.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_fr.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_gl.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_he.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_hr.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_hu.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_id.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_it.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_ja.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_lt.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_nl.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_pl.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_pt.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_ru.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_tr.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_uk.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/sensors/sensors_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_ar.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_ca.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_cs.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_cy.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_da.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_de.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_el.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_eo.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_es.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_eu.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_fi.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_fr.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_gl.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_he.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_hr.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_hu.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_ia.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_id.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_it.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_ja.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_ko.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_lt.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_nl.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_pl.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_pt.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_ru.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_sk_SK.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_sl.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_sr@latin.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_sr_BA.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_sr_RS.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_tr.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_uk.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/showdesktop/showdesktop_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_ar.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_ca.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_cs.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_cy.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_da.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_de.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_el.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_es.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_fr.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_gl.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_he.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_hr.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_hu.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_id.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_it.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_ja.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_lt.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_nl.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_pl.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_pt.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_ru.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_sk.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_tr.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_uk.qm
/usr/share/lxqt/translations/lxqt-panel/spacer/spacer_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/statusnotifier/statusnotifier_ca.qm
/usr/share/lxqt/translations/lxqt-panel/statusnotifier/statusnotifier_cy.qm
/usr/share/lxqt/translations/lxqt-panel/statusnotifier/statusnotifier_da.qm
/usr/share/lxqt/translations/lxqt-panel/statusnotifier/statusnotifier_de.qm
/usr/share/lxqt/translations/lxqt-panel/statusnotifier/statusnotifier_gl.qm
/usr/share/lxqt/translations/lxqt-panel/statusnotifier/statusnotifier_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/statusnotifier/statusnotifier_pl.qm
/usr/share/lxqt/translations/lxqt-panel/statusnotifier/statusnotifier_tr.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_ca.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_cs.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_cy.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_da.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_de.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_el.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_es.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_fr.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_gl.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_he.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_hu.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_id.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_it.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_ja.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_lt.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_nl.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_pl.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_pt.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_ru.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_tr.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_uk.qm
/usr/share/lxqt/translations/lxqt-panel/sysstat/sysstat_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_ar.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_ca.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_cs.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_cy.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_da.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_de.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_el.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_eo.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_es.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_eu.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_fi.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_fr.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_gl.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_he.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_hr.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_hu.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_ia.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_id.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_it.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_ja.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_ko.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_lt.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_nl.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_pl.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_pt.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_ru.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_sk_SK.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_sl.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_sr@latin.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_sr_BA.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_sr_RS.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_tr.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_uk.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/taskbar/taskbar_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_ca.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_cs.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_cy.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_da.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_de.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_gl.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_id.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_pl.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_ru_RU.qm
/usr/share/lxqt/translations/lxqt-panel/tray/tray_tr.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_ar.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_ca.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_cs.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_cy.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_da.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_de.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_el.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_eo.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_es.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_es_VE.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_eu.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_fi.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_fr.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_gl.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_he.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_hu.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_id.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_it.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_ja.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_lt.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_nl.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_pl.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_pt.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_pt_BR.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_ro_RO.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_ru.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_sl.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_th_TH.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_tr.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_uk.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_zh_CN.qm
/usr/share/lxqt/translations/lxqt-panel/volume/volume_zh_TW.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_ar.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_ca.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_cs.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_cy.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_da.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_de.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_el.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_es.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_fr.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_gl.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_he.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_hu.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_id.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_it.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_ja.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_lt.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_nb_NO.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_nl.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_pl.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_pt.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_ru.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_tr.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_uk.qm
/usr/share/lxqt/translations/lxqt-panel/worldclock/worldclock_zh_CN.qm

%files dev
%defattr(-,root,root,-)
/usr/include/lxqt/ilxqtpanel.h
/usr/include/lxqt/ilxqtpanelplugin.h
/usr/include/lxqt/lxqtpanelglobals.h
/usr/include/lxqt/pluginsettings.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/lxqt-panel/libcolorpicker.so
/usr/lib64/lxqt-panel/libdirectorymenu.so
/usr/lib64/lxqt-panel/libkbindicator.so
/usr/lib64/lxqt-panel/libmount.so
/usr/lib64/lxqt-panel/libsensors.so
/usr/lib64/lxqt-panel/libsysstat.so
/usr/lib64/lxqt-panel/libvolume.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-panel/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lxqt-panel.1
