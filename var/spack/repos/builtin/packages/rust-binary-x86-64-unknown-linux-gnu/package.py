# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RustBinaryX8664UnknownLinuxGnu(RustBinaryPackage):
    """Install Rust binary distributions for x86_64-unknown-linux-gnu"""

    homepage = "https://www.rust-lang.org/"

    maintainers = ['AndrewGaspar']

    # provides('rust-binary', when='platform=linux os=rhel7 target=x86_64')

    rust_target_arch = 'x86_64-unknown-linux-gnu'

    version('1.41.1', sha256='a6d5a3b3f574aafc8f787fea37aad9fb8a7946b383ae5348146927192ff0bef0')
    version('1.41.0', sha256='343ba8ef7397eab7b3bb2382e5e4cb08835a87bff5c8074382c0b6930a41948b')
    version('1.40.0', sha256='fc91f8b4bd18314e83a617f2389189fc7959146b7177b773370d62592d4b07d0')
    version('1.39.0', sha256='b10a73e5ba90034fe51f0f02cb78f297ed3880deb7d3738aa09dc5a4d9704a25')
    version('1.38.0', sha256='adda26b3f0609dbfbdc2019da4a20101879b9db2134fae322a4e863a069ec221')
    version('1.37.0', sha256='cb573229bfd32928177c3835fdeb62d52da64806b844bc1095c6225b0665a1cb')
    version('1.36.0', sha256='15e592ec52f14a0586dcebc87a957e472c4544e07359314f6354e2b8bd284c55')
    version('1.35.0', sha256='cf600e2273644d8629ed57559c70ca8db4023fd0156346facca9ab3ad3e8f86c')
    version('1.34.2', sha256='2bf6622d980a52832bae141304e96f317c8a1ccd2dfd69a134a14033e6e43c0f')
    version('1.34.1', sha256='8e2eead11bd5bf61409e29018d007c6fc874bcda2ff54db3d04d1691e779c14e')
    version('1.34.0', sha256='170647ed41b497dc937a6b2556700210bc4be187b1735029ef9ccf52e2cb5ab8')
    version('1.33.0', sha256='6623168b9ee9de79deb0d9274c577d741ea92003768660aca184e04fe774393f')
    version('1.32.0', sha256='e024698320d76b74daf0e6e71be3681a1e7923122e3ebd03673fcac3ecc23810')
    version('1.31.1', sha256='a64685535d0c457f49a8712a096a5c21564cd66fd2f7da739487f028192ebe3c')
    version('1.30.1', sha256='a01a493ed8946fc1c15f63e74fc53299b26ebf705938b4d04a388a746dfdbf9e')
    version('1.30.0', sha256='f620e3125cc505c842150bd873c0603432b6cee984cdae8b226cf92c8aa1a80f')
    version('1.29.2', sha256='e9809825c546969a9609ff94b2793c9107d7d9bed67d557ed9969e673137e8d8')
    version('1.29.1', sha256='b36998aea6d58525f25d89f1813b6bfd4cad6ff467e27bd11e761a20dde43745')
    version('1.29.0', sha256='09f99986c17b1b6b1bfbc9dd8785e0e4693007c5feb67915395d115c1a3aea9d')
    version('1.28.0', sha256='2a1390340db1d24a9498036884e6b2748e9b4b057fc5219694e298bdaa37b810')
    version('1.27.2', sha256='5028a18e913ef3eb53e8d8119d2cc0594442725e055a9361012f8e26f754f2bf')
    version('1.27.1', sha256='435778a837af764da2a7a7fb4d386b7b78516c7dfc732d892858e9a8a539989b')
    version('1.27.0', sha256='235ad78e220b10a2d0267aea1e2c0f19ef5eaaff53ad6ff8b12c1d4370dec9a3')
    version('1.26.2', sha256='d2b4fb0c544874a73c463993bde122f031c34897bb1eeb653d2ba2b336db83e6')
    version('1.26.1', sha256='b7e964bace1286696d511c287b945f3ece476ba77a231f0c31f1867dfa5080e0')
    version('1.26.0', sha256='13691d7782577fc9f110924b26603ade1990de0b691a3ce2dc324b4a72a64a68')
    version('1.25.0', sha256='06fb45fb871330a2d1b32a27badfe9085847fe824c189ddc5204acbe27664f5e')
    version('1.24.1', sha256='4567e7f6e5e0be96e9a5a7f5149b5452828ab6a386099caca7931544f45d5327')
    version('1.24.0', sha256='336cf7af6c857cdaa110e1425719fa3a1652351098dc73f156e5bf02ed86443c')
    version('1.23.0', sha256='9a34b23a82d7f3c91637e10ceefb424539dcfa327c2dcd292ff10c047b1fdc7e')
    version('1.22.1', sha256='8cf4e840041fb05721673836997c5aac5673f733660927dfb64b8d653a3a94fa')
    version('1.22.0', sha256='11118f670343f3ebdd4790f845fd68f38db65b19261b81b3ab580d8425d0a7c6')
    version('1.21.0', sha256='b41e70e018402bc04d02fde82f91bea24428e6be432f0df12ac400cfb03108e8')
    version('1.20.0', sha256='ca1cf3aed73ff03d065a7d3e57ecca92228d35dc36d9274a6597441319f18eb8')
    version('1.19.0', sha256='30ff67884464d32f6bbbde4387e7557db98868e87fb2afbb77c9b7716e3bff09')
    version('1.18.0', sha256='abdc9f37870c979dd241ba8c7c06d8bb99696292c462ed852c0af7f988bb5887')
    version('1.17.0', sha256='bbb0e249a7a3e8143b569706c7d2e7e5f51932c753b7fd26c58ccd2015b02c6b')
    version('1.16.0', sha256='48621912c242753ba37cad5145df375eeba41c81079df46f93ffb4896542e8fd')
    version('1.15.1', sha256='b1e7c818a3cc8b010932f0efc1cf0ede7471958310f808d543b6e32d2ec748e7')
    version('1.15.0', sha256='576fcced49744af5ea438afc4411395530426b0a3d4839c5205f646f15850663')
    version('1.14.0', sha256='c71325cfea1b6f0bdc5189fa4c50ff96f828096ff3f7b5056367f9685d6a4d04')
    version('1.13.0', sha256='95f4c372b1b81ac1038161e87e932dd7ab875d25c167a861c3949b0f6a65516d')
    version('1.12.1', sha256='9e546aec13e389429ba2d86c8f4e67eba5af146c979e4faa16ffb40ddaf9984c')
    version('1.12.0', sha256='3a9647123f1f056571d6603e40f21a96162702e1ae4725ee8c2bc9452a87cf5d')
    version('1.11.0', sha256='f4ebbd6d9494cb8fa6c410cb58954e1913546c2bca8963faebc424591547d83f')
    version('1.10.0', sha256='f189303d52b37c8bb694b9d9739ae73ffa926cbdeffde1d5d6a5c6e811940293')
    version('1.9.0',  sha256='288ff13efa2577e81c77fc2cb6e2b49b1ed0ceab51b4fa12f7efb87039ac49b7')
    version('1.8.0',  sha256='d5a7c10070f8053defe07d1704762c91e94fc30a1020d16b111d63e9af365d48')
    version('1.7.0',  sha256='d36634bd8df3d7565487b70af03dfda1c43c635cd6f2993f47cd61fda00d890a')
    version('1.6.0',  sha256='8630cc02432b4423d64eeae4ef071ec58e5dd1f3d555a3a3cc34b759202813f6')
    version('1.5.0',  sha256='60b83f74d882ce2ba5bc979b5b0589dca56659f215b3259e7188fed8c50aac9d')
    version('1.4.0',  sha256='2de2424b50ca2ab3a67c495b6af03c720801a2928ad30884438ad0f5436ac51d')
    version('1.3.0',  sha256='fa755b6331ff7554e6e8545ee20af7897b0adc65f471dd24ae8a467a944755b4')
    version('1.2.0',  sha256='2311420052e06b3e698ce892924ec40890a8ff0499902e7fc5350733187a1531')
    version('1.1.0',  sha256='5a8b1c4bb254a698a69cd05734909a3933567be6996422ff53f947fd115372e6')
    version('1.0.0',  sha256='aab0d853314675d5e80e427c613a0e646ae75fbbc856b886dab682280f825d53')
