#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-collapse
Version  : 1.8.4
Release  : 4
URL      : https://cran.r-project.org/src/contrib/collapse_1.8.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/collapse_1.8.4.tar.gz
Summary  : Advanced and Fast Data Transformation
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-collapse-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : R-data.table
BuildRequires : buildreq-R

%description
statistical computing in R that is extremely fast, class-agnostic,
    and programmer friendly through a flexible and parsimonious syntax.
    It is well integrated with base R, 'dplyr' / (grouped) 'tibble', 
    'data.table', 'sf', 'plm' (panel-series and data frames), and 
    non-destructively handles other matrix or data frame based classes (like 
    'ts', 'xts' / 'zoo', 'tsibble', ...)

%package lib
Summary: lib components for the R-collapse package.
Group: Libraries

%description lib
lib components for the R-collapse package.


%prep
%setup -q -c -n collapse
cd %{_builddir}/collapse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1654793294

%install
export SOURCE_DATE_EPOCH=1654793294
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library collapse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library collapse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library collapse
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc collapse || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/collapse/DESCRIPTION
/usr/lib64/R/library/collapse/INDEX
/usr/lib64/R/library/collapse/LICENSE
/usr/lib64/R/library/collapse/Meta/Rd.rds
/usr/lib64/R/library/collapse/Meta/data.rds
/usr/lib64/R/library/collapse/Meta/features.rds
/usr/lib64/R/library/collapse/Meta/hsearch.rds
/usr/lib64/R/library/collapse/Meta/links.rds
/usr/lib64/R/library/collapse/Meta/nsInfo.rds
/usr/lib64/R/library/collapse/Meta/package.rds
/usr/lib64/R/library/collapse/Meta/vignette.rds
/usr/lib64/R/library/collapse/NAMESPACE
/usr/lib64/R/library/collapse/NEWS.md
/usr/lib64/R/library/collapse/R/collapse
/usr/lib64/R/library/collapse/R/collapse.rdb
/usr/lib64/R/library/collapse/R/collapse.rdx
/usr/lib64/R/library/collapse/data/Rdata.rdb
/usr/lib64/R/library/collapse/data/Rdata.rds
/usr/lib64/R/library/collapse/data/Rdata.rdx
/usr/lib64/R/library/collapse/doc/collapse_documentation.Rmd
/usr/lib64/R/library/collapse/doc/collapse_documentation.html
/usr/lib64/R/library/collapse/doc/index.html
/usr/lib64/R/library/collapse/help/AnIndex
/usr/lib64/R/library/collapse/help/aliases.rds
/usr/lib64/R/library/collapse/help/collapse.rdb
/usr/lib64/R/library/collapse/help/collapse.rdx
/usr/lib64/R/library/collapse/help/paths.rds
/usr/lib64/R/library/collapse/html/00Index.html
/usr/lib64/R/library/collapse/html/R.css
/usr/lib64/R/library/collapse/tests/testthat.R
/usr/lib64/R/library/collapse/tests/testthat/test-BY.R
/usr/lib64/R/library/collapse/tests/testthat/test-GRP.R
/usr/lib64/R/library/collapse/tests/testthat/test-TRA.R
/usr/lib64/R/library/collapse/tests/testthat/test-attribute-handling.R
/usr/lib64/R/library/collapse/tests/testthat/test-collap.R
/usr/lib64/R/library/collapse/tests/testthat/test-dapply.R
/usr/lib64/R/library/collapse/tests/testthat/test-data.table.R
/usr/lib64/R/library/collapse/tests/testthat/test-fHDbetween-fHDwithin-HDB-HDW.R
/usr/lib64/R/library/collapse/tests/testthat/test-fNobs-fNdistinct.R
/usr/lib64/R/library/collapse/tests/testthat/test-fbetween-fwithin-B-W.R
/usr/lib64/R/library/collapse/tests/testthat/test-fcumsum.R
/usr/lib64/R/library/collapse/tests/testthat/test-fdiff-fgrowth-D-G.R
/usr/lib64/R/library/collapse/tests/testthat/test-ffirst-flast.R
/usr/lib64/R/library/collapse/tests/testthat/test-flag-L-F.R
/usr/lib64/R/library/collapse/tests/testthat/test-flm-fFtest.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmean.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmedian.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmin-fmax.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmode.R
/usr/lib64/R/library/collapse/tests/testthat/test-fprod.R
/usr/lib64/R/library/collapse/tests/testthat/test-fscale-STD.R
/usr/lib64/R/library/collapse/tests/testthat/test-fsubset-ftransform.R
/usr/lib64/R/library/collapse/tests/testthat/test-fsum.R
/usr/lib64/R/library/collapse/tests/testthat/test-fvar-fsd.R
/usr/lib64/R/library/collapse/tests/testthat/test-indexing.R
/usr/lib64/R/library/collapse/tests/testthat/test-list-processing.R
/usr/lib64/R/library/collapse/tests/testthat/test-misc.R
/usr/lib64/R/library/collapse/tests/testthat/test-miscellaneous-issues.R
/usr/lib64/R/library/collapse/tests/testthat/test-psmat-psacf.R
/usr/lib64/R/library/collapse/tests/testthat/test-qsu.R
/usr/lib64/R/library/collapse/tests/testthat/test-qtab.R
/usr/lib64/R/library/collapse/tests/testthat/test-quick-conversion.R
/usr/lib64/R/library/collapse/tests/testthat/test-recode-replace.R
/usr/lib64/R/library/collapse/tests/testthat/test-roworder-colorder-rename.R
/usr/lib64/R/library/collapse/tests/testthat/test-select-replace-vars.R
/usr/lib64/R/library/collapse/tests/testthat/test-seqid-groupid.R
/usr/lib64/R/library/collapse/tests/testthat/test-setop.R
/usr/lib64/R/library/collapse/tests/testthat/test-sf.R
/usr/lib64/R/library/collapse/tests/testthat/test-splitting.R
/usr/lib64/R/library/collapse/tests/testthat/test-varying.R
/usr/lib64/R/library/collapse/tests/testthat/test-whichv.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/collapse/libs/collapse.so
/usr/lib64/R/library/collapse/libs/collapse.so.avx2
/usr/lib64/R/library/collapse/libs/collapse.so.avx512
