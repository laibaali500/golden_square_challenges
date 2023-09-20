## Function Design Recipe 2

## 1. Describe the Problem

_User story 2:_

> As a user
> So that I can improve my grammar
> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_The name of the function, its parameters, return value, and side effects:_

```python
def grammar_check(sentence: str):
    """Check if a sentence is grammatically correct.
    
    Parameters:
        sentence: str -- a sentence to be checked
    
    Returns:
        bool -- is the sentence correct or not?
    
    Side effects:
        None
    
    """

    pass
```

## 3. Create Examples as Tests

_A list of examples of what the function will take and return._

```python
"""
Given a correct sentence "Hello everynyan!"
It returns True
"""
grammar_check("Hello everynyan!") => (True)

"""
Given a partially correct sentence "hello guys!"
It returns False
"""
grammar_check("hello guys!") => (False)

"""
Given a partially correct sentence "Hello guys"
It returns False
"""
grammar_check("Hello guys") => (False)

"""
Given an incorrect sentence "hey guys"
It returns False
"""
grammar_check("hey guys") => (False)
```