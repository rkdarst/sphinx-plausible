# Quick and dirty test

set -xe
cd $(dirname $0)

(
    set -e
    cd site-1
    make clean html
    grep domain-test-1 build/html/index.html

    SPHINX_PLAUSIBLE_DEACTIVATE=1 make clean html
    ! grep domain-test-1 build/html/index.html

)
