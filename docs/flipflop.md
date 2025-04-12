# FlipFlop Script

Script that allows you to:

1. Set multiple counters with custom names
2. Specify whether each counter starts with 0 or 1 on its start date
3. View all counters' current status (0 or 1) based on their intervals
4. All data persists between runs via JSON config file

### Features:

1. **Custom Initial Value**:

   - Now you can specify whether each counter starts with 0 or 1 on its start date
   - The alternation continues from this initial value

2. **Flexible Start Date**:

   - Can enter "today" to use current date as start date
   - Or specify any date in YYYY-MM-DD format

3. **Display**:

   - Clear formatting with separators
   - Shows pending status for future-dated counters
   - Displays all counter details when viewing

4. **Counter Management**:

   - Added ability to delete counters
   - Better error handling for all inputs

5. **Status Calculation**:

   - Now properly respects the initial value you set
   - Uses formula: `(initial_value + period) % 2` to maintain alternation

6. **Custom Labels**:

   - Now prompts for labels when creating a counter
   - Stores them in the counter's configuration
   - Uses them when displaying status

   **Enhanced Display**:

   - Shows both the numeric value and its label
   - Displays the label mapping in the counter info
   - Improved formatting with wider separators

   **Backward Compatible**:

   - If no labels exist in old configs, defaults to "1" and "0"
   - Maintains all existing functionality

   **User Experience**:

   - More intuitive prompts showing the actual labels
   - Clearer status display with meaningful words

7. **Toogle Counter On/Off**:

   - Set counters as active/inactive when creating them
   - Toggle their status later
   - Inactive counters will simply show "Off" in the status display
   - All other counter information is preserved when inactive

### Example Usage:

1. Add a counter:

   - Name: "WaterPlants"
   - Start date: today
   - Interval: 3 days
   - Initial value: 1

2. Add another counter:

   - Name: "FeedFish"
   - Start date: 2023-01-05
   - Interval: 2 days
   - Initial value: 0

3. View status will show:
   ```
   WaterPlants: 1
     Start: 2023-06-15 (initial: 1)
     Interval: every 3 days
   ----------------------------------------
   FeedFish: 0
     Start: 2023-01-05 (initial: 0)
     Interval: every 2 days
   ```

The script maintains all your counters and their logic between runs through the JSON file.
