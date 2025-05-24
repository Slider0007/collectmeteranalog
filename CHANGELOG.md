# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unlreased] - 2025-05-xx

### Added
- Implement appilcation version handling
  - Source of version: `collectmeteranalog/__version__.py`
  - New parameter `--version`
  - Automatically inject version to all build processes
  - Use version in github actions for artifacts
- Implement adjustable image collection root path
  - New `parameter: --collectpath`
- Add posibilty to define the labeled images root folder using `--labelfile`
  - Define `--labeling` and `--labelfile` at the same time using different paths

### Changed
- Updated github actions
- Fix image download counter
- Refacored prediction functionality
- Refactored readme

### Removed
- Removed internal model handling -> default: No model is used
- Repo cleanup



## [1.0.8]

- fix failure in labeling with csv-file if multiple images are not available

## [1.0.1] - 2022-09-18

### Added

### Changed

- changed release action
- fixed requirements

### Removed
