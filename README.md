# sellthetrend_cj

## Using the drop shipping parser for Sell The Trend

#### Step 1: Create HTML file

1. Open Google Chrome and navigate to Sell the Trend website.
1. Scroll down as much as needed. 
1. Open developer tools.
1. Select html tag, copy it.
1. Paste it in a file within `data` folder.

#### Step 2: Parse HTML file

In the command line:

```bash
squeezer drop-shipping --html THE_HTML_FILE --date THE_DATE
```

For example:

```bash
squeezer drop-sheeping --html input.html --date 2023-09-25
```

