#!/bin/bash
# Build roboto-example Debian package (Architecture: all, no cmake build)
set -e

PACKAGE="roboto-example"
VERSION="1.0.1"
PREFIX="/opt/roboparty"
DEB_DIR="${PACKAGE}_${VERSION}_all"

echo ">>> Building ${PACKAGE} ${VERSION}"

# Clean previous staging directory and deb file
rm -rf "${DEB_DIR}" "${DEB_DIR}.deb"
mkdir -p "${DEB_DIR}/DEBIAN"

# Install sample scripts and config separately
mkdir -p "${DEB_DIR}${PREFIX}/share/sample/scripts"
cp -r scripts/. "${DEB_DIR}${PREFIX}/share/sample/scripts/"
find "${DEB_DIR}${PREFIX}/share/sample/scripts" -name "*.py" -exec chmod 755 {} \;

mkdir -p "${DEB_DIR}${PREFIX}/share/sample/config"
cp -r config/. "${DEB_DIR}${PREFIX}/share/sample/config/"

# Copy DEBIAN maintainer scripts
cp debian/postinst  "${DEB_DIR}/DEBIAN/"
cp debian/postrm    "${DEB_DIR}/DEBIAN/"
chmod 755 "${DEB_DIR}/DEBIAN/postinst" "${DEB_DIR}/DEBIAN/postrm"

# Generate Control file (Replace placeholders)
sed -e "s/VERSION_PLACEHOLDER/${VERSION}/g" \
    debian/control > "${DEB_DIR}/DEBIAN/control"

echo ">>> Executing dpkg-deb build..."
dpkg-deb --root-owner-group --build "${DEB_DIR}"

echo ">>> Success! Generated ${DEB_DIR}.deb"
