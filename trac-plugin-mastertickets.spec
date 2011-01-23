%define		trac_ver	0.12
%define		plugin		mastertickets
Summary:	Add simple support for renaming/moving wiki pages
Name:		trac-plugin-%{plugin}
Version:	3.0
Release:	0.4
License:	BSD
Group:		Applications/WWW
# Source0Download:	http://trac-hacks.org/changeset/latest/xmlrpcplugin?old_path=/&filename=xmlrpcplugin&format=zip
#Source0:	%{plugin}plugin.zip
Source0:	http://github.com/coderanger/trac-mastertickets/zipball/master
# Source0-md5:	b32a2dac51488e6fd68bbcf49e384a72
URL:		http://trac-hacks.org/wiki/MasterTicketsPlugin
BuildRequires:	python-devel
BuildRequires:	unzip
Requires:	trac >= %{trac_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin adds "blocks" and "blocked by" fields to each ticket,
enabling you to express dependencies between tickets. It also provides
a graphviz-based dependency-graph feature for those tickets having
dependencies specified, allowing you to visually understand the
dependency tree. The dependency graph is viewable by clicking
'depgraph' in the context (in the upper right corner) menu when
viewing a ticket that blocks or is blocked by another ticket.

%prep
%setup -qc -n %{plugin}plugin

%build
cd coderanger-trac-mastertickets-ffc6543
%{__python} setup.py build
%{__python} setup.py egg_info

%install
rm -rf $RPM_BUILD_ROOT
cd coderanger-trac-mastertickets-ffc6543
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
	To enable the %{plugin} plugin, add to conf/trac.ini:

	[components]
	%{plugin}.* = enabled
EOF
fi

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{plugin}
%{py_sitescriptdir}/TracMasterTickets-*.egg-info
