%define version 1.0.1
%define reponame hmta

Name:           hmta
Version:        %{version}
Release:        1%{?dist}
Summary:        Do you wanna know how much time would take you to watch an anime? Well, this is your tool.
License:        MIT
Url:            https://github.com/rooyca/hmta
Source0:        https://github.com/rooyca/hmta/archive/refs/tags/v%{version}.tar.gz

BuildArch: noarch

Requires: python3

%description
A script that helps you find out how much time would take you to watch an anime.

%prep
%setup -q

%build
# Nothing to do here

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 hmta.py %{buildroot}%{_bindir}/hmta

%files
%{_bindir}/hmta

%changelog
* Mon Aug 16 2023 Ronald Cantillo <rooyca@gmail.com>
- Initial RPM release
