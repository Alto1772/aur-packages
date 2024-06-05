# Maintainer: AltoXorg <machinademoniko AT gmail DOT com>

# For package compiling issues, comment at the AUR package comments section or PM me on Discord @AltoXorg
# and I will try my best to resolve your problem if possible.
# This is much very experimental, so expect some game issues and crashes...

# An N64 Majora's Mask US ROM must be provided in order to build this package.
# Rename it to "baserom.mm.us.rev1.z64" and place it right to where this script is.

_mm_compat_commit=23beee0717364de43ca9a82957cc910cf818de90

_reponame=Zelda64Recomp
_pkgname=${_reponame,,}
pkgname=${_pkgname}-git
pkgver=1.1.1.r3.g030d793
_zrecomp_dirname="${_reponame}"
pkgrel=1
arch=("x86_64" "aarch64")
depends=("sdl2" "freetype2" "libx11" "libxrandr" "gtk3" "vulkan-driver" "vulkan-icd-loader")
makedepends=("git" "cmake" "ninja" "mold" "python" "make" "clang" "lld" "llvm" "mips-linux-gnu-binutils")
pkgdesc="A port of The Legend of Zelda Majora's Mask made possible by static recompilation (git)"
license=("GPL-3.0-only")
provides=("${_pkgname}")
conflicts=("${_pkgname}" "${_pkgname}-bin")  #  i don't have control over the bin version so i'll append this anyway...
url="https://github.com/Zelda64Recomp/${_reponame}"
source=("git+${url}.git#branch=dev"

        # main dependencies
        "git+https://github.com/mikke89/RmlUi.git"
        "git+https://github.com/rt64/rt64.git"
        #"git+https://github.com/ubawurinna/freetype-windows-binaries.git"
        "mm-decomp::git+https://github.com/zeldaret/mm.git"
        "git+https://github.com/sammycage/lunasvg.git"
        "git+https://github.com/DLTcollab/sse2neon.git"
        "git+https://github.com/N64Recomp/N64ModernRuntime.git"

        # RT64 dependencies
        "git+https://github.com/epezent/implot.git"
        "git+https://github.com/redorav/hlslpp.git"
        #"git+https://github.com/mupen64plus/mupen64plus-win32-deps.git"
        #"git+https://github.com/mupen64plus/mupen64plus-core.git"
        "git+https://github.com/Cyan4973/xxHash.git"
        "git+https://github.com/zeux/volk.git"
        "git+https://github.com/KhronosGroup/Vulkan-Headers.git"
        "git+https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator.git"
        "git+https://github.com/ocornut/imgui.git"
        "git+https://github.com/john-chapman/im3d.git"
        #"git+https://github.com/GPUOpen-LibrariesAndSDKs/D3D12MemoryAllocator.git"
        "dxc::git+https://github.com/rt64/dxc-bin.git"
        "git+https://github.com/nothings/stb.git"
        "git+https://github.com/btzy/nativefiledialog-extended.git"

        # Tools for building MM elf and generating static recomps
        "mm-compat::git+https://github.com/zeldaret/mm#commit=${_mm_compat_commit}"
        "git+https://github.com/N64Recomp/N64Recomp.git"

        # N64Recomp dependencies
        "git+https://github.com/Decompollaborate/rabbitizer.git"
        "git+https://github.com/serge1/ELFIO.git"
        "git+https://github.com/fmtlib/fmt.git"
        "git+https://github.com/marzer/tomlplusplus.git"

        # Misc. patches and the rom requirement
        "mm-compat-disasm-script.patch::https://github.com/zeldaret/mm/pull/1606.patch"
        "zelda64recomp.desktop"
        "file://baserom.mm.us.rev1.z64")
source_aarch64=("git+https://github.com/decompals/ido-static-recomp.git")
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '3df28d035ed99e08e0bcca794e1912db00254c91bd4b32652b7d2db3a506a8b1'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '68fa964348231904c427d471091258de75308c7f0a77022fc8a009f8c6b9fae1'
            '59443fba2781cecccf96f76772a04764477c1c57d3226baa43d8cc3c30b085ad'
            'efb1365b3ae362604514c0f9a1a2d11f5dc8688ba5be660a37debf5e3be43f2b')
sha256sums_aarch64=('SKIP')

# -- Per-repo submodules
# We only need some of them for this linux platform
_main_submodules=(
  RmlUi
  rt64
  #freetype-windows-binaries
  mm-decomp
  lunasvg
  sse2neon
  N64ModernRuntime
)
_rt64_submodules=(
  implot
  hlslpp
  #mupen64plus-win32-deps
  #mupen64plus-core
  xxHash
  volk
  Vulkan-Headers
  VulkanMemoryAllocator
  imgui
  im3d
  #D3D12MemoryAllocator
  dxc
  stb
  nativefiledialog-extended
)
_n64recomp_submodules=(rabbitizer ELFIO fmt tomlplusplus)
_n64modernruntime_submodules=(rt64)

PKG_PREFIX="/opt/${_pkgname}"


# -- Print helpers
_msg_info() {
  echo "${BOLD}>> ${GREEN}$@${ALL_OFF}"
}

_msg_warn() {
  echo "${BOLD}>> ${YELLOW}$@${ALL_OFF}"
}

_is_debug() {
  for opt in "${OPTIONS[@]}"; do
    if [ "$opt" = debug ]; then
      return 0
    fi
  done

  return 1
}

_init_submodules() {
  dir="$1"
  shift 1

  for sub in "$@"; do
    git submodule init "${dir}${sub}"
    git config "submodule.${dir}${sub}.url" "${srcdir}/${sub}"
    git -c protocol.file.allow=always submodule update "${dir}${sub}"
  done
}

pkgver() {
  cd "${srcdir}/${_reponame}"

  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
}

prepare() {
  _msg_info "Setting up the submodules..."

  cd "${srcdir}/${_zrecomp_dirname}"
  _init_submodules "lib/" "${_main_submodules[@]}"

  cd "${srcdir}/${_zrecomp_dirname}/lib/rt64"
  _init_submodules "src/contrib/" "${_rt64_submodules[@]}"

  cd "${srcdir}/${_zrecomp_dirname}/lib/N64ModernRuntime"
  _init_submodules "" "${_n64modernruntime_submodules[@]}"

  cd "${srcdir}/${_zrecomp_dirname}/lib/N64ModernRuntime/rt64"
  _init_submodules "src/contrib/" "${_rt64_submodules[@]}"

  cd "${srcdir}/N64Recomp"
  _init_submodules "lib/" "${_n64recomp_submodules[@]}"


  _msg_info "Patching stuff up..."

  cd "${srcdir}/mm-compat"
  patch -Np1 < "${srcdir}/mm-compat-disasm-script.patch"
}

build() {
  _msg_info "Building the N64Recomp & RSPRecomp tools..."

  cd "${srcdir}/N64Recomp"

  cmake -B build -DCMAKE_BUILD_TYPE=Release .
  cmake --build build

  cp build/{N64Recomp,RSPRecomp} "${srcdir}/${_zrecomp_dirname}"

  if [ "$CARCH" != "x86_64" ]; then
    cd "${srcdir}/ido-static-recomp"
    if [[ ! -e target-built.stamp || "$(cat target-built.stamp)" != "${_mm_compat_commit}" ]]; then
      _msg_info "Building IDO compiler recompilation for $CARCH"

      # append our flags with the flags from this project's makefile
      export CFLAGS="$CFLAGS -MMD -fno-strict-aliasing -I." CXXFLAGS="$CXXFLAGS -MMD" LDFLAGS="$LDFLAGS -lm"

      make setup
      make VERSION=5.3 RELEASE=1
      make VERSION=7.1 RELEASE=1

      echo "${_mm_compat_commit}" > target-built.stamp
    fi

    rm -rf "${srcdir}/mm-compat/tools/ido_recomp/linux/"*
    ln -srf build/5.3/out "${srcdir}/mm-compat/tools/ido_recomp/linux/5.3"
    ln -srf build/7.1/out "${srcdir}/mm-compat/tools/ido_recomp/linux/7.1"
  fi

  cd "${srcdir}/mm-compat"
  cp "${srcdir}/baserom.mm.us.rev1.z64" .

  if [[ ! -e target-built.stamp || "$(cat target-built.stamp)" != "${_mm_compat_commit}" ]]; then
    _msg_info "Building the MM decomp-specific ELF file..."

    [ ! -e .venv ] && python -m venv .venv
    (
      # Unset the build flags so that we won't intervene from this host system to the decomp's compilation process
      unset CFLAGS CXXFLAGS LDFLAGS CC CPP CXX LD
      export RUN_CC_CHECK=0
      source .venv/bin/activate
      pip install -U -r requirements.txt

      # Mostly the same thing as the make init process with the only difference is to speed up time
      make distclean
      make setup
      make assets
      make disasm
      make uncompressed  # We only need the uncompressed stuff out
    )
    echo "${_mm_compat_commit}" > target-built.stamp
  else
    _msg_warn "Decomp ELF file already built, skipping..."
  fi

  # Copy both the elf file and the uncompressed rom
  cp mm.us.rev1.rom_uncompressed.{elf,z64} "${srcdir}/${_zrecomp_dirname}/"


  cd "${srcdir}/${_zrecomp_dirname}"

  _msg_info "Generating recomp functions..."
  ./RSPRecomp aspMain.us.rev1.toml
  ./RSPRecomp njpgdspMain.us.rev1.toml
  ./N64Recomp us.rev1.toml


  _msg_info "Building the game..."

  if _is_debug; then
    BUILD_TYPE=RelWithDebInfo
  else
    BUILD_TYPE=Release
  fi

  # The entirety of the codebase doesn't care about security at all so we'll remove this flag
  export CFLAGS="${CFLAGS/-Werror=format-security/}"
  export CXXFLAGS="${CXXFLAGS/-Werror=format-security/}"
  # use mold to speed up linking
  export LDFLAGS="$LDFLAGS -fuse-ld=mold"

  # The official build docs recommends using Clang,
  # but if you want (just for your own sakes),
  # you can use GCC.

  cmake -B build -GNinja . \
    -DCMAKE_BUILD_TYPE=$BUILD_TYPE \
    -DCMAKE_CXX_COMPILER=clang++ \
    -DCMAKE_C_COMPILER=clang

  cmake --build build $NINJAFLAGS
}


package() {
  cd "${srcdir}"

  bin_name=Zelda64Recompiled

  cat << SHELL > launch.sh
#!/usr/bin/env bash
cd "${PKG_PREFIX}"
exec ./${bin_name}
SHELL

  install -Dm755 "${_zrecomp_dirname}/build/${bin_name}" "${pkgdir}/${PKG_PREFIX}/${bin_name}"

  # Strip the executable whether you like it or not, except for debugging purposes...
  if ! _is_debug; then
    strip --strip-all "${pkgdir}/${PKG_PREFIX}/${bin_name}"
  fi

  cp -r --preserve=mode "${_zrecomp_dirname}/assets" "${pkgdir}/${PKG_PREFIX}/"
  install -Dm755 launch.sh "${pkgdir}/usr/bin/${bin_name}"
  install -Dm644 zelda64recomp.desktop -t "${pkgdir}/usr/share/applications"
  install -Dm644 "${_zrecomp_dirname}/icons/512.png" "${pkgdir}/usr/share/icons/hicolor/512x512/apps/zelda64recomp.png"

  install -Dm644 "${_zrecomp_dirname}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
