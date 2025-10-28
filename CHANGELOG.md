# Changelog

## Version 3.0.0 - 2025-10-28

### Major Improvements

#### Error Handling & Reliability
- Added comprehensive try-catch blocks throughout the code
- Proper timeout handling with `WebDriverWait` for page loads
- Graceful error recovery when individual viewers fail to load
- Better exception messages with specific error types
- Critical error handling prevents crashes

#### Modern Selenium Usage
- Updated to modern `--headless=new` mode
- Added `WebDriverWait` and `ExpectedConditions` for reliable element detection
- Proper exception imports: `TimeoutException`, `NoSuchElementException`
- Added stability flags: `--no-sandbox`, `--disable-gpu`
- Set default window size for better compatibility

#### Cross-Platform Support
- Platform detection using `sys.platform`
- Windows-specific commands (cls, title) now conditional
- Added support for Linux/Mac with `clear` command alternative

#### User Experience
- Input validation for proxy selection (1-5) with retry loop
- Input validation for viewer count (1-100) with retry loop
- Real-time progress tracking during viewer creation
- Success/failure statistics displayed at completion
- Better formatted output messages with emojis
- Improved error messages with actionable guidance

#### Code Quality
- Added docstrings to main functions
- Better variable naming and code organization
- Proper file handling with context managers (`with` statement)
- Added `timeout` parameter to HTTP requests
- Used `r.raise_for_status()` for HTTP error checking
- Colorama auto-reset initialization

#### Proxy Selection
- Now displays full proxy URLs when selecting
- Shows all 5 servers (was showing only 4 before)
- Better input validation

#### Viewer Creation
- Progress indicator for each viewer
- Individual error handling per viewer (doesn't stop on single failure)
- Tracks successful vs failed viewers
- Small delays between viewer creation for stability
- Explicit `text_box.clear()` before entering URL

#### Completion & Cleanup
- Displays statistics: successful viewers, failed viewers, target channel
- Better shutdown handling with try-finally
- Keyboard interrupt (Ctrl+C) handling
- Graceful browser cleanup on exit
- Confirmation messages

### Bug Fixes
- Fixed proxy server loop showing only 4 of 5 servers
- Added proper exception handling in update check
- Fixed file handling (using context manager)
- Better handling of missing version.txt file
- Fixed potential race conditions with WebDriverWait

### Technical Changes
- Version bumped to 3.0.0
- Added imports: `sys`, `WebDriverWait`, `EC`, exception types
- Removed hardcoded Chrome path (now uses system default)
- Removed hardcoded driver_path reference
- Better HTTP request handling with timeout

### Recommendations for Users
- Recommended viewer count: 5-20 (now displayed in UI)
- Maximum viewer count limited to 100 (validation)
- Better guidance on troubleshooting proxy servers
