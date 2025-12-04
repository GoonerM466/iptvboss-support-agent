# Adding Numbered Logos

Boss Pro includes support for custom numbered logos, allowing you to bulk-assign sequential logo files to multiple channels.

### Getting Custom Numbered Logos

- Boss Pro supports bulk updating for numbered logo sets (e.g., ESPN+ event channels).
- Replace the number in the logo filename with the placeholder format:  
`{num#}` — where # represents the starting number of the sequence.

### Example

- IPTVBoss hosts a set of event-based channels with filenames like:
`https://cdn.iptvboss.pro/logos/USA/ESPN+001.v.png`
![https://cdn.iptvboss.pro/logos/USA/ESPN+001.v.png](https://cdn.iptvboss.pro/logos/USA/ESPN+001.v.png)
- To bulk-apply these logos:
1. Select the group of channels you want to update.
2. Paste a logo link using the numbered placeholder, such as: `https://cdn.iptvboss.pro/logos/USA/ESPN+{num1}.v.png`
- Boss Pro will automatically increment the numbers across the channel list.

### Notes
- The `{num#}` syntax currently only supports numbering with two leading zeros.
- Example format:  
  - ESPN+001
  - ESPN+010
  - ESPN+100
- **Not**:
  - ESPN+1
  *or*
  - ESPN+01

### Available Logos
You can browse existing numbered logos [here](https://cdn.iptvboss.pro/logos/).

### Related Topics
~To Be Added~