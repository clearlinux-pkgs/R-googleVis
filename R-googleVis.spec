#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-googleVis
Version  : 0.6.4
Release  : 19
URL      : https://cran.r-project.org/src/contrib/googleVis_0.6.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/googleVis_0.6.4.tar.gz
Summary  : R Interface to Google Charts
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-jsonlite
BuildRequires : R-jsonlite
BuildRequires : R-markdown
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# googleVis
[![Travis-CI Build Status](https://travis-ci.org/mages/googleVis.svg?branch=master)](https://travis-ci.org/mages/googleVis)   [![CRAN\_Status\_Badge](https://www.r-pkg.org/badges/version/googleVis)](https://cran.r-project.org/package=googleVis) [![downloads](https://cranlogs.r-pkg.org/badges/grand-total/googleVis)](https://cran.r-project.org/package=googleVis)

%prep
%setup -q -c -n googleVis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571839798

%install
export SOURCE_DATE_EPOCH=1571839798
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library googleVis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library googleVis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library googleVis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc googleVis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/googleVis/CITATION
/usr/lib64/R/library/googleVis/DESCRIPTION
/usr/lib64/R/library/googleVis/INDEX
/usr/lib64/R/library/googleVis/Meta/Rd.rds
/usr/lib64/R/library/googleVis/Meta/data.rds
/usr/lib64/R/library/googleVis/Meta/demo.rds
/usr/lib64/R/library/googleVis/Meta/features.rds
/usr/lib64/R/library/googleVis/Meta/hsearch.rds
/usr/lib64/R/library/googleVis/Meta/links.rds
/usr/lib64/R/library/googleVis/Meta/nsInfo.rds
/usr/lib64/R/library/googleVis/Meta/package.rds
/usr/lib64/R/library/googleVis/Meta/vignette.rds
/usr/lib64/R/library/googleVis/NAMESPACE
/usr/lib64/R/library/googleVis/NEWS
/usr/lib64/R/library/googleVis/R/googleVis
/usr/lib64/R/library/googleVis/R/googleVis.rdb
/usr/lib64/R/library/googleVis/R/googleVis.rdx
/usr/lib64/R/library/googleVis/brew/Stock.html
/usr/lib64/R/library/googleVis/brew/andrew.html
/usr/lib64/R/library/googleVis/data/Rdata.rdb
/usr/lib64/R/library/googleVis/data/Rdata.rds
/usr/lib64/R/library/googleVis/data/Rdata.rdx
/usr/lib64/R/library/googleVis/demo/AnimatedGeoChart.R
/usr/lib64/R/library/googleVis/demo/EventListener.R
/usr/lib64/R/library/googleVis/demo/Roles.R
/usr/lib64/R/library/googleVis/demo/Trendlines.R
/usr/lib64/R/library/googleVis/demo/WorldBank.R
/usr/lib64/R/library/googleVis/demo/googleVis.R
/usr/lib64/R/library/googleVis/doc/Using_Roles_via_googleVis.R
/usr/lib64/R/library/googleVis/doc/Using_Roles_via_googleVis.Rmd
/usr/lib64/R/library/googleVis/doc/Using_Roles_via_googleVis.html
/usr/lib64/R/library/googleVis/doc/Using_Trendlines_with_googleVis.R
/usr/lib64/R/library/googleVis/doc/Using_Trendlines_with_googleVis.Rmd
/usr/lib64/R/library/googleVis/doc/Using_Trendlines_with_googleVis.html
/usr/lib64/R/library/googleVis/doc/Using_googleVis_with_knitr.R
/usr/lib64/R/library/googleVis/doc/Using_googleVis_with_knitr.Rmd
/usr/lib64/R/library/googleVis/doc/Using_googleVis_with_knitr.html
/usr/lib64/R/library/googleVis/doc/googleVis.R
/usr/lib64/R/library/googleVis/doc/googleVis.Rnw
/usr/lib64/R/library/googleVis/doc/googleVis.pdf
/usr/lib64/R/library/googleVis/doc/googleVis_examples.R
/usr/lib64/R/library/googleVis/doc/googleVis_examples.Rmd
/usr/lib64/R/library/googleVis/doc/googleVis_examples.html
/usr/lib64/R/library/googleVis/doc/index.html
/usr/lib64/R/library/googleVis/gadgets/gadgets.R
/usr/lib64/R/library/googleVis/help/AnIndex
/usr/lib64/R/library/googleVis/help/aliases.rds
/usr/lib64/R/library/googleVis/help/googleVis.rdb
/usr/lib64/R/library/googleVis/help/googleVis.rdx
/usr/lib64/R/library/googleVis/help/paths.rds
/usr/lib64/R/library/googleVis/html/00Index.html
/usr/lib64/R/library/googleVis/html/R.css
/usr/lib64/R/library/googleVis/mansections/GoogleChartToolsURL.txt
/usr/lib64/R/library/googleVis/mansections/GoogleChartToolsURLConfigOptions.txt
/usr/lib64/R/library/googleVis/mansections/gvisOptions.txt
/usr/lib64/R/library/googleVis/mansections/gvisOutputStructure.txt
/usr/lib64/R/library/googleVis/rsp/index.rsp
/usr/lib64/R/library/googleVis/rsp/myAnalysis/index.rsp
/usr/lib64/R/library/googleVis/rsp/src/simpleFooter.rsp
/usr/lib64/R/library/googleVis/rsp/src/simpleHead.rsp
/usr/lib64/R/library/googleVis/rsp/src/simpleHeader.rsp
/usr/lib64/R/library/googleVis/shiny/server.R
/usr/lib64/R/library/googleVis/shiny/ui.R
