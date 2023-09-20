## Function Design Recipe 1

## 1. Describe the Problem

_User story 1:_

> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_The name of the function, its parameters, return value, and side effects:_

```python
def estimate_reading_time(words):
    """Calculate reading time, given text length and reading speed.
    
    Parameters:
        words: int -- number of words in the text
    
    Returns:
        int -- estimated reading time in minutes
    
    Side effects:
        None
    """

    pass
```

## 3. Create Examples as Tests

_A list of examples of what the function will take and return._

```python
"""
Given a text length of 200 words
It returns a reading time of 1 minute
"""
estimate_reading_time(200) => (1)

"""
Given a text length of 450 words
It returns a reading time of 2.25 minutes
"""
estimate_reading_time(450) => (2.25)
```