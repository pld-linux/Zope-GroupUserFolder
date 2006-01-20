%define		zope_subname	GroupUserFolder
Summary:	A Zope product, a convenient tool to manage groups of users within Zope
Summary(pl):	Dodatek do Zope z wygodnym narzędziem do zarządzaniem grupami i użytkownikami w Zope
Name:		Zope-%{zope_subname}
Version:	3.5
%define		part_name groupuserfolder-3-5
# %%define		sub_ver Beta2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://plone.org/products/groupuserfolder/releases/%{version}/%{part_name}-tar.gz
# Source0-md5:	bbde3e369202eed37c833d37f176af26
# Patch0:		Zope-GroupUserFolder-bad_path_python.patch
URL:		http://ingeniweb.sourceforge.net/Products/GroupUserFolder/
BuildRequires:	python
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GroupUserFolder is a Zope product that is a convenient tool to manage
groups of users within Zope.

%description -l pl
GroupUserFolder jest dodatkiem dla Zope zawierającym wygodne narzędzie
do zarządzania grupami i użytkownikami zawartymi w Zope.

%prep
%setup -q -n %{zope_subname}
# %%patch0 -p1
rm -f interfaces/.cvsignore
rm -f doc/py2htmldoc.py.orig

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,doc,dtml,interfaces,skins,tests,www,*.py,*.gif,refresh.txt,version.txt,PRODUCT_NAME,product.txt} \
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
%doc ABOUT CHANGES CONTRIBUTORS README.txt TODO INSTALL.txt design.txt
%{_datadir}/%{name}
