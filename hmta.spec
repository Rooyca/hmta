%define version 1.0.1
%define reponame hmta

Name:           hmta
Version:        %{version}
Release:        1%{?dist}
Summary:        Do you wanna know how much time would take you to watch an anime? Well, this is your tool.
License:        MIT
Url:            https://github.com/rooyca/hmta
Source0:        https://github.com/rooyca/hmta/archive/refs/tags/v%{version}.tar.gz

BuildRequires: python3-copr
BuildRequires: python3-copr-common >= %copr_common_version

Requires:   python3-copr
Requires:   python3-copr-common >= %copr_common_version

%description

A script that helps you find out how much time would take you to watch an anime.


%prep
%autosetup -n %{reponame}-%{version}


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Aug 16 2023 rooyca <rooyca@gmail.com>
- Initial RPM Release
