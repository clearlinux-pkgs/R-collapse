#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-collapse
Version  : 2.0.19
Release  : 39
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/collapse_2.0.19.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/collapse_2.0.19.tar.gz
Summary  : Advanced and Fast Data Transformation
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-collapse-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R

%description
statistical computing in R that is extremely fast, class-agnostic, robust and 
    programmer friendly. Core functionality includes a rich set of S3 generic grouped 
    and weighted statistical functions for vectors, matrices and data frames, which 
    provide efficient low-level vectorizations, OpenMP multithreading, and skip missing 
    values by default. These are integrated with fast grouping and ordering algorithms 
    (also callable from C), and efficient data manipulation functions. The package also 
    provides a flexible and rigorous approach to time series and panel data in R. 
    It further includes fast functions for common statistical procedures, detailed 
    (grouped, weighted) summary statistics, powerful tools to work with nested data, 
    fast data object conversions, functions for memory efficient R programming, and 
    helpers to effectively deal with variable labels, attributes, and missing data. 
    It is well integrated with base R classes, 'dplyr'/'tibble', 'data.table', 'sf', 'units', 
    'plm' (panel-series and data frames), and 'xts'/'zoo'.

%package lib
Summary: lib components for the R-collapse package.
Group: Libraries

%description lib
lib components for the R-collapse package.


%prep
%setup -q -n collapse
pushd ..
cp -a collapse buildavx2
popd
pushd ..
cp -a collapse buildavx512
popd
pushd ..
cp -a collapse buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736457187

%install
export SOURCE_DATE_EPOCH=1736457187
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/collapse/CITATION
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
/usr/lib64/R/library/collapse/WORDLIST
/usr/lib64/R/library/collapse/data/Rdata.rdb
/usr/lib64/R/library/collapse/data/Rdata.rds
/usr/lib64/R/library/collapse/data/Rdata.rdx
/usr/lib64/R/library/collapse/doc/collapse_and_sf.Rmd
/usr/lib64/R/library/collapse/doc/collapse_and_sf.html
/usr/lib64/R/library/collapse/doc/collapse_documentation.Rmd
/usr/lib64/R/library/collapse/doc/collapse_documentation.html
/usr/lib64/R/library/collapse/doc/collapse_for_tidyverse_users.R
/usr/lib64/R/library/collapse/doc/collapse_for_tidyverse_users.Rmd
/usr/lib64/R/library/collapse/doc/collapse_for_tidyverse_users.html
/usr/lib64/R/library/collapse/doc/collapse_object_handling.R
/usr/lib64/R/library/collapse/doc/collapse_object_handling.Rmd
/usr/lib64/R/library/collapse/doc/collapse_object_handling.html
/usr/lib64/R/library/collapse/doc/developing_with_collapse.Rmd
/usr/lib64/R/library/collapse/doc/developing_with_collapse.html
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
/usr/lib64/R/library/collapse/tests/testthat/test-fmatch.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmean.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmedian.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmin-fmax.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmode.R
/usr/lib64/R/library/collapse/tests/testthat/test-fmutate.R
/usr/lib64/R/library/collapse/tests/testthat/test-fprod.R
/usr/lib64/R/library/collapse/tests/testthat/test-fquantile.R
/usr/lib64/R/library/collapse/tests/testthat/test-fscale-STD.R
/usr/lib64/R/library/collapse/tests/testthat/test-fsubset-ftransform.R
/usr/lib64/R/library/collapse/tests/testthat/test-fsum.R
/usr/lib64/R/library/collapse/tests/testthat/test-fvar-fsd.R
/usr/lib64/R/library/collapse/tests/testthat/test-indexing.R
/usr/lib64/R/library/collapse/tests/testthat/test-join.R
/usr/lib64/R/library/collapse/tests/testthat/test-list-processing.R
/usr/lib64/R/library/collapse/tests/testthat/test-misc.R
/usr/lib64/R/library/collapse/tests/testthat/test-miscellaneous-issues.R
/usr/lib64/R/library/collapse/tests/testthat/test-pivot.R
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
/usr/lib64/R/library/collapse/tests/testthat/testthat-problems.rds

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/collapse/libs/collapse.so
/V4/usr/lib64/R/library/collapse/libs/collapse.so
/VA/usr/lib64/R/library/collapse/libs/collapse.so
/usr/lib64/R/library/collapse/libs/collapse.so
