while [ 3 -gt 0 ]; do find -type f -name *.zip -exec unzip -- '{}' \; -exec rm -- '{}' \;; done
