# Python Loops - June 11 2026

## While Loop
- Runs as long as condition is true
- Needs an exit condition or runs forever
- x = x + 1 increments the counter each loop

## Key Concepts
- Define variable before the loop
- Use separate variables for original value vs counter
- start = stores original input, never changes
- x = the counter that changes during the loop

## Real World Example
- BioResponse: log starting temp (start)
- Track current temp as it changes (x)
- Stop heating when target reached (exit condition)

## Bug I Fixed Today
- Checking x after loop always equals 6
- Solution: check start instead of x
- start never changes, x does

## Break and continue
- break = exit loop immediately
- continue = skip current iteration, keep looping
