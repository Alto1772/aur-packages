# Maintainer: AltoXorg <machinademoniko AT gmail DOT com>

# For package compiling issues, comment at the AUR package comments section or PM me on Discord @AltoXorg
# and I will try my best to resolve your problem if possible.
# This is much very experimental, so expect some game issues and crashes...

# An N64 Majora's Mask US ROM must be provided in order to build this package.
# Rename it to "baserom.mm.us.rev1.z64" and place it right to where this script is.

_RmlUi_commit=a893ea6386e0c842f90a726a53c9b9e888797519
_lunasvg_tag=v2.3.9
_mm_decomp_commit=5607eec18bae68e4cd38ef6d1fa69d7f1d84bfc8
_rt64_commit=ecdd609c49fb5f10e3040335901d8860ef259f67

_N64Recomp_commit=94b59d56f70228c3d3e3062cf1b1ab6ce42153c0
_mm_compat_commit=0492c8e89af3806707e44a88379a3c8d9c503ca1


_reponame=Zelda64Recomp
_pkgname=${_reponame,,}
pkgname=${_pkgname}
pkgver=1.0.1
_zrecomp_dirname="${_reponame}-${pkgver}"
pkgrel=1
arch=("x86_64")
depends=("sdl2" "freetype2" "libx11" "libxrandr" "gtk3" "vulkan-driver" "vulkan-icd-loader")
makedepends=("cmake" "ninja" "mold" "python" "make" "clang" "lld" "llvm" "mips-linux-gnu-binutils")
pkgdesc="A port of The Legend of Zelda Majora's Mask made possible by static recompilation"
license=("GPL-3.0")
conflicts=("${_pkgname}-bin")  #  i don't have control over this package so i'll append this anyway...
url="https://github.com/Mr-Wiseguy/${_reponame}"
source=("${_zrecomp_dirname}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"

        # main dependencies
        # We only fetch the required submodules for this linux platform
        "RmlUi::git+https://github.com/mikke89/RmlUi.git#commit=${_RmlUi_commit}"
        "lunasvg::git+https://github.com/sammycage/lunasvg.git#tag=${_lunasvg_tag}"
        "mm-decomp::git+https://github.com/zeldaret/mm#commit=${_mm_decomp_commit}"
        "rt64::git+https://github.com/rt64/rt64.git#commit=${_rt64_commit}"

        # RT64 dependencies
        "git+https://github.com/NVIDIA/DLSS.git"
        "git+https://github.com/epezent/implot.git"
        "git+https://github.com/redorav/hlslpp.git"
        "git+https://github.com/intel/xess.git"
        "git+https://github.com/mupen64plus/mupen64plus-win32-deps.git"
        "git+https://github.com/mupen64plus/mupen64plus-core.git"
        "git+https://github.com/Cyan4973/xxHash.git"
        "git+https://github.com/zeux/volk.git"
        "git+https://github.com/KhronosGroup/Vulkan-Headers.git"
        "git+https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator.git"
        "git+https://github.com/ocornut/imgui.git"
        "git+https://github.com/john-chapman/im3d.git"
        "git+https://github.com/GPUOpen-LibrariesAndSDKs/D3D12MemoryAllocator.git"
        "dxc::git+https://github.com/rt64/dxc-bin.git"
        "git+https://github.com/nothings/stb.git"
        "git+https://github.com/btzy/nativefiledialog-extended.git"

        # Tools for building MM elf and generating static recomps
        "mm-compat::git+https://github.com/zeldaret/mm#commit=${_mm_compat_commit}"
        "N64Recomp::git+https://github.com/Mr-Wiseguy/N64Recomp.git#commit=${_N64Recomp_commit}"

        # N64Recomp dependencies
        "git+https://github.com/Decompollaborate/rabbitizer.git"
        "git+https://github.com/serge1/ELFIO.git"
        "git+https://github.com/fmtlib/fmt.git"
        "git+https://github.com/marzer/tomlplusplus.git"

        # Misc. patches and few
        "rt64-cmake-libxrandr.patch"
        "rt64-runtime-fix-prebuilt-shader-cache.patch"
        "mm-compat-disasm-script.patch"
        "zelda64recomp.desktop"
        "file://baserom.mm.us.rev1.z64")
sha256sums=('2dd551fb8d090fccdd757b42ff215a293cbd7b11244be091e1aa52d44f1de46d'
            'fffad7b6eb3c3cec5b4e9033a09c068d33fb0bf028cc1560a4b96d1a15db32f1'
            '9d3878d9f7d7f93a2181551b8271420fe32d33f7259b3744667bca659b7e2593'
            'dc421693786da0df9d309b07134d84edf6e513e986aab92327dfbc7c8bab4f68'
            '52acd1db3ee21a0d377d6d85156b6afa4770cc724b6cd8e65d87ac282d53250b'
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
            'b9f25deece8210a15049287953f9f5838545f23cf44d21261fd315869af5a701'
            'ad0d188dd5cfa610456154ecedab2d020e20b641bc812956d7c84052003a51de'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '3bf9a13aa8cf99256c10cd41a98fecc1bc431887606e5902d771e40b743e8b2d'
            '1ff448f413e3ad5bf3e16879c53686decc7d4ce6347d7ec494054ba1f170a88a'
            '2582f9cd6fb69b1e21c2bd10ca2d252e14f690fd17b56b245c8044911bf5d420'
            '59443fba2781cecccf96f76772a04764477c1c57d3226baa43d8cc3c30b085ad'
            'efb1365b3ae362604514c0f9a1a2d11f5dc8688ba5be660a37debf5e3be43f2b')

PKG_PREFIX="/opt/${_pkgname}"

#  Print helpers
_msg_info() {
  echo "${BOLD}>> ${GREEN}$@${ALL_OFF}"
}

_msg_warn() {
  echo "${BOLD}>> ${YELLOW}$@${ALL_OFF}"
}


prepare() {
  _msg_info "Setting up the submodules..."

  cd "${srcdir}/${_zrecomp_dirname}"
  cd lib
  for dir in RmlUi lunasvg mm-decomp rt64; do
    if [ ! -L "${dir}" ]; then
      rm -rf "${dir}"
      ln -srf "${srcdir}/${dir}" "${dir}"
    fi
  done

  cd "${srcdir}/${_zrecomp_dirname}/lib/rt64"
  git submodule init
  for submodule in DLSS implot hlslpp xess mupen64plus-win32-deps mupen64plus-core \
      xxHash volk Vulkan-Headers VulkanMemoryAllocator imgui im3d D3D12MemoryAllocator \
      dxc stb nativefiledialog-extended; do
    git config "submodule.src/contrib/${submodule}.url" "${srcdir}/${submodule}"
  done
  git -c protocol.file.allow=always submodule update

  cd "${srcdir}/N64Recomp"
  git submodule init
  for submodule in rabbitizer ELFIO fmt tomlplusplus; do
    git config "submodule.lib/${submodule}.url" "${srcdir}/${submodule}"
  done
  git -c protocol.file.allow=always submodule update


  _msg_info "Patching stuff up..."

  cd "${srcdir}/${_zrecomp_dirname}"

  # Ignore warnings on GCC not just clang...
  sed -i -e 's/__clang__/__GNUC__/' -e 's/clang/GCC/g' include/disable_warnings.h


  cd "${srcdir}/mm-compat"
  patch -Np1 < "${srcdir}/mm-compat-disasm-script.patch" || true


  cd "${srcdir}/${_zrecomp_dirname}/lib/rt64"
  chmod +x "src/contrib/dxc/bin/x64/dxc"

  # Patch that links libxrandr on the RT64 side...
  # Without this the linker will complain about an incomprehensible DSO error
  patch -Np1 < "${srcdir}/rt64-cmake-libxrandr.patch" || true

  # Patch to force RT64 for using the prebuilt mm_shader_cache.bin bundled in the game's repo...
  patch -Np1 < "${srcdir}/rt64-runtime-fix-prebuilt-shader-cache.patch" || true
}

# yah this build process is a much bit complicated tbh
build() {
  _msg_info "Building the N64Recomp & RSPRecomp tools..."

  cd "${srcdir}/N64Recomp"

  cmake -B build -DCMAKE_BUILD_TYPE=Release .
  cmake --build build

  cp build/{N64Recomp,RSPRecomp} "${srcdir}/${_zrecomp_dirname}"


  cd "${srcdir}/mm-compat"
  cp "${srcdir}/baserom.mm.us.rev1.z64" .

  if [[ ! -e target-built.stamp || "$(cat target-built.stamp)" != "${_mm_compat_commit}" ]]; then
    _msg_info "Building the MM decomp-specific ELF file..."

    [ ! -e .venv ] && python -m venv .venv
    (
      # Unset the build flags so that we won't intervene from this host system to the decomp's compilation process
      unset CFLAGS CXXFLAGS LDFLAGS CC CPP CXX LD
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

  echo ">> Generating recomp functions..."
  ./RSPRecomp aspMain.us.rev1.toml
  ./RSPRecomp njpgdspMain.us.rev1.toml
  ./N64Recomp us.rev1.toml


  _msg_info "Building the game..."

  if [[ "${OPTIONS[@]}" =~ " debug " ]]; then
    BUILD_TYPE=RelWithDebInfo
  else
    BUILD_TYPE=Release
  fi

  # The entirety of the codebase doesn't care about security at all so we'll remove this flag
  export CFLAGS="${CFLAGS/-Werror=format-security/}"
  export CXXFLAGS="${CXXFLAGS/-Werror=format-security/}"

  # The official build docs recommends using Clang,
  # but if you want to compensate file size or
  # just for your own sakes, you can use GCC.

  # use mold to speed up linking; added by myself
  cmake -B build -GNinja . \
    -DCMAKE_BUILD_TYPE=$BUILD_TYPE \
    -DCMAKE_EXE_LINKER_FLAGS=-fuse-ld=mold \
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
  if [[ "${OPTIONS[@]}" =~ " debug " ]]; then
    strip --strip-all "${pkgdir}/${PKG_PREFIX}/${bin_name}"
  fi

  cp -r --preserve=mode "${_zrecomp_dirname}/assets" "${pkgdir}/${PKG_PREFIX}/"
  install -Dm755 launch.sh "${pkgdir}/usr/bin/${bin_name}"
  install -Dm644 zelda64recomp.desktop -t "${pkgdir}/usr/share/applications"
  install -Dm644 "${_zrecomp_dirname}/icons/512.png" "${pkgdir}/usr/share/icons/hicolor/512x512/apps/zelda64recomp.png"

  install -Dm644 "${_zrecomp_dirname}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
