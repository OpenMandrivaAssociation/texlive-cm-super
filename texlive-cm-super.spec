%global tl_name cm-super
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	CM-Super family of fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/cm-super
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-super.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-super.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The CM-Super family provides Adobe Type 1 fonts that replace the
T1/TS1-encoded Computer Modern (EC/TC), T1/TS1-encoded Concrete,
T1/TS1-encoded CM bright and LH Cyrillic fonts (thus supporting all
European languages except Greek), and bringing many ameliorations in
typesetting quality. The fonts exhibit the same metrics as the Metafont-
encoded originals.

