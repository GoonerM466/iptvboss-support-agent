# Channels Sorted Incorrectly - A-Z Not Working

Channel sorting uses the first character in the channel name including prefixes.

### Problem

Channels are sorted incorrectly (A-Z sorting not working).

### Explanation

Channel sorting uses the first character/number in the channel name. If channels start with prefixes like "CA", "US", numbers, or symbols, these determine sort order.

**Example**: "CA: ESPN" and "ESPN" will sort under "C" and "E" respectively, not together.

### Solution

Remove prefixes that interfere with sorting:

1. Edit channel names to remove country codes or numbering prefixes
2. Or use a consistent prefix format for all channels
3. Re-output your playlist after making changes

### Related Topics

- [Channel Sorting Ignores Prefixes](../known_issues/09_channel_sorting_ignores_prefixes.md)
