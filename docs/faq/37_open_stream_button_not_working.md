# Open Stream Button Not Working

VLC64 must be installed for stream preview to work.

### Problem

The "Open Stream" button in Layout Editor doesn't work, does nothing when clicked, or crashes Boss

### Solution

**The Open Stream button requires VLC to be installed:**

1. Download and install VLC Media Player (64-bit version)
   - Get it from: https://www.videolan.org/vlc/
   - **Important**: Install the 64-bit (x64) version, not 32-bit

2. Restart IPTVBoss after installing VLC

**How to use the Open Stream button:**

1. Open a layout in Layout Editor
2. Select a channel
3. Click **Open Stream** button in Channel Options panel
4. VLC will launch and start playing the stream

**Use this to**:
- Test if a stream works before outputting
- Verify stream quality & channel accuracy
- Troubleshoot playback issues
- Preview channels

### Common Issues

**Button does nothing**:
- VLC is not installed
- Wrong VLC architecture (32-bit vs 64-bit)
- VLC installation path not detected by Java

**Stream doesn't play in VLC**:
- Stream URL is invalid or broken
- Provider issue (check with provider)
- Network/firewall blocking stream
- Expired credentials

### Related Topics

- [Layout Editor Channel Options](../user_guide/11_layout_editor_channel_options.md)
- [No Streams Found After Output](09_no_streams_found_after_output.md)
