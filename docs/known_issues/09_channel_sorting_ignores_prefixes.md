# Channel Sorting Ignores Prefixes

A-Z sort doesn't group channels as expected when they have prefixes.

### Status

By design, but confusing to users.

### Problem

Channel sorting uses first character in name, causing channels with prefixes to sort separately from similar channels without prefixes.

### Symptoms

- A-Z sort doesn't group channels as expected
- Channels with prefixes (US, CA, numbers) sort by prefix
- "ESPN" and "US ESPN" don't sort together

### Root Cause

Sort uses first character/number in channel name.

### Workaround

Remove or standardize prefixes in channel names.
- You can revert your changes or to provider name after if prefered
- Ignore Channel Name CHanges will ensure prefix dont get added back on next sync

### Related Topics

- [Channel Sorting Incorrect](../faq/26_channel_sorting_incorrect.md)
