%include	/usr/lib/rpm/macros.python
%define		zope_subname	GroupUserFolder
Summary:	GroupUserFolder - a Zope product, a convenient tool to manage groups of users within Zope
Summary(pl):	GroupUserFolder - dodatek do Zope z wygodnym narzêdziem do zarz±dzaniem grupami i u¿ytkownikami w Zope
Name:		Zope-%{zope_subname}
Version:	1.32
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	12066901e073b148422058876adc0773
URL:		http://sourceforge.net/projects/collective/
%pyrequires_eq	python-modules
Requires:	Zope
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	product_dir	/usr/lib/zope/Products

%description
GroupUserFolder is a Zope product that is a convenient tool to manage
groups of users within Zope.

%description -l pl
GroupUserFolder jest dodatkiem dla Zope zawieraj±cym wygodne narzêdzie
do zarz±dzania grupami i u¿ytkownikami zawartymi w Zope.

%prep
%setup -q -n %{zope_subname}

rm -f interfaces/.cvsignore

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# should tests be included or not?
cp -af {Extensions,doc,dtml,interfaces,skins,tests,website,www,*.py,*.gif} \
	$RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS README-Plone.stx README.txt TODO
%{product_dir}/%{zope_subname}
