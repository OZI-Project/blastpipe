# OZI 0.1 meson.build:root_files,root_children
# Part of blastpipe.
# See LICENSE.txt in the project root for details.
# DO NOT EDIT BY HAND - This file was generated for use with OZI tools.
# ozi-fix -> meson rewrite is the standard editing pipeline.
project(
    'blastpipe',
    default_options: ['warning_level=3'],
    license: 'Apache-2.0 WITH LLVM-exception',
    license_files: ['LICENSE.txt'],
    meson_version: '>=1.1.0',
    version: run_command(
        'python3',
        [
            '-c',
            'from setuptools_scm import get_version;print(get_version(normalize=False, fallback_version="%OZIBUILDVERSION%"))',
        ],
        check: true,
    ).stdout().strip(),
)
env = environment()
fs = import('fs')
pymod = import('python')
project_name = meson.project_name()
docs_source = 'subprojects/docs'
pip_compile = find_program(get_option('compile-requirements-command')[0], required: true)
root_files = [
    'README.rst',
    'CHANGELOG.md',
    'LICENSE.txt',
    'pyproject.toml',
    '.gitignore',
    '.pre-commit-config.yaml',
    'NOTICE.md',
]
python = pymod.find_installation()
pyproject_config = configuration_data()
pyproject_config.set(
    'PYTHON_VERSION_DIST',
    'py'+''.join(python.language_version().split('.'))
)
pyproject_config.set('SCM_VERSION', meson.project_version())
pyproject_config.set('VCS_TAG', '@VCS_TAG@')
pyproject_config.set('PROJECT_NAME', project_name)
pyproject_config.set('README_TEXT', fs.read('README.rst'))
pyproject_config.set('LICENSE', meson.project_license()[0])
configure_file(
    input: 'pyproject.toml',
    output: 'pyproject.toml',
    configuration: pyproject_config
)
vcs_tag(input: 'pyproject.toml', output: 'pyproject.orig.toml')
foreach source : root_files
    if source not in ['pyproject.toml', '.gitignore', 'CHANGELOG.md']
        fs.copyfile(source)
    endif
endforeach
root_children = [
    'blastpipe',
    'tests',
]
foreach child: root_children
    subdir(child)
endforeach
if false
    executable('root_files', root_files)
    executable('root_children', root_children)
    executable('source_files', source_files)
    executable('source_children', source_children)
    executable('test_files', test_files)
endif
if not meson.is_subproject()
    dev = subproject('ozi')
    foreach var : get_option('variables')
        name = var.replace('-', '_')
        set_variable(name, dev.get_variable(name))
    endforeach
    deps = run_command(python, '-c', dev.get_variable('install_dependencies'), check: true).stdout().strip().split('$$')
    if deps[0] != ''
        if find_program('uv', disabler: true).found()
            meson.add_postconf_script('uv', 'venv', 'venv')
        else
            meson.add_postconf_script(dev.get_variable('pip'), 'install', 'virtualenv')
            meson.add_postconf_script('virtualenv', 'venv')
        endif
        meson.add_postconf_script(dev.get_variable('pip'), 'install', deps)
    endif
endif
subproject('msgspec', default_options: ['install-subprojects=enabled'])