%include	/usr/lib/rpm/macros.python
%define		zope_subname	GroupUserFolder
Summary:	A Zope product, a convenient tool to manage groups of users within Zope
Summary(pl):	Dodatek do Zope z wygodnym narzêdziem do zarz±dzaniem grupami i u¿ytkownikami w Zope
Name:		Zope-%{zope_subname}
Version:	2.0
%define		sub_ver Beta2
Release:	1.%{sub_ver}.1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}%{sub_ver}.tar.gz
# Source0-md5:	1b1922ff25c496bbc837f31a486d6b04
Patch0:		Zope-GroupUserFolder-bad_path_python.patch
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):  /usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GroupUserFolder is a Zope product that is a convenient tool to manage
groups of users within Zope.

%description -l pl
GroupUserFolder jest dodatkiem dla Zope zawieraj±cym wygodne narzêdzie
do zarz±dzania grupami i u¿ytkownikami zawartymi w Zope.

%prep
%setup -q -n %{zope_subname}
%patch0 -p1
rm -f interfaces/.cvsignore

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

# should tests be included or not?
cp -af {Extensions,data,doc,dtml,interfaces,skins,tests,website,www,*.py,*.gif,refresh.txt,version.txt,PRODUCT_NAME} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname} 
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS README-Plone.stx README.txt TODO ChangeLog INSTALL.txt
%{_datadir}/%{name}
