%include	/usr/lib/rpm/macros.python
%define		zope_subname	GroupUserFolder
Summary:	GroupUserFolder - a Zope product, a convenient tool to manage groups of users within Zope
Summary(pl):	GroupUserFolder - dodatek do Zope z wygodnym narzêdziem do zarz±dzaniem grupami i u¿ytkownikami w Zope
Name:		Zope-%{zope_subname}
Version:	1.32
Release:	1
License:	GNU
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
%setup -q -c %{zope_subname}-%{version}

%build
cd %{zope_subname}
rm -rf `find . -type d -name debian`
rm -f `find . -type f -name .cvsignore`
mkdir docs
mv -f CHANGES CONTRIBUTORS INSTALL.txt README.txt TODO docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{product_dir}

cp -af * $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

%py_comp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}
%py_ocomp $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}

rm -rf $RPM_BUILD_ROOT%{product_dir}/%{zope_subname}/docs
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
%doc %{zope_subname}/docs/*
%{product_dir}/%{zope_subname}
