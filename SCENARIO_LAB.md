# Predict the program, then explain why

Use only scenarios whose prerequisites have already been taught. Before running, predict output/error and final state, explain the mechanism, then change one condition. Exact exception wording can vary; identify the error class and cause. Use your own practice folder. Production work stays in its owned path.

Scope cases 1–7 fit Day 012. Imports fit Day 019; object mutation case 13 fits Day 025; enclosing scope/defaults/closures fit Day 032. Spread cases through existing lesson, recall, and repair time. A correct implementation and a still-pending concept answer have separate status.

## 1. Reading a module value

Is `global` needed here? What is printed?

```python
total = 10
def read_total():
    return total
print(read_total())
```

## 2. Same name, different binding

```python
total = 10
def change_local():
    total = 20
    return total
print(change_local(), total)
```

## 3. Read and assign

```python
total = 10
def bump():
    total += 1
    return total
print(bump())
```

## 4. Explicit module rebinding

```python
total = 10
def bump():
    global total
    total += 1
bump()
print(total)
```

## 5. Mutating an existing object

```python
topics = []
def remember(topic):
    topics.append(topic)
remember("python")
print(topics)
```

Now replace the append line with `topics += [topic]`. Does the result change? Explain the binding operation, not just the list operation.

## 6. Rebinding a local list

```python
topics = ["python"]
def replace_topics():
    topics = ["ml"]
    return topics
print(replace_topics(), topics)
```

## 7. Assignment in a branch that does not run

```python
limit = 10
def choose(flag):
    if flag:
        limit = 20
    return limit
print(choose(False))
```

Try `choose(True)` separately. Why can the error depend on the call while the local-name rule is determined earlier?

## 8. Enclosing scope

```python
def make_counter():
    total = 0
    def next_value():
        nonlocal total
        total += 1
        return total
    return next_value
counter = make_counter()
print(counter(), counter())
```

What changes if `nonlocal` is removed? Would `global` target the same binding?

## 9. Default object lifetime

```python
def add_topic(topic, seen=[]):
    seen.append(topic)
    return seen
first = add_topic("python")
second = add_topic("ml")
print(first, second, first is second)
```

## 10. Shadowing a built-in name

```python
list = [1, 2]
print(list("ab"))
```

## 11. When a closure reads a value

```python
functions = [lambda: index for index in range(3)]
print([function() for function in functions])
```

Compare with `lambda index=index: index` only after predicting the original.

## 12. Import binding versus module attribute

Put this in `settings.py` in your own practice folder:

```python
value = 10
```

Put this in `read_setting.py` in the same folder and run it:

```python
from settings import value
import settings
settings.value = 20
print(value, settings.value)
```

What would change if the imported value were a shared list that was mutated instead of rebound?

## 13. A mutation followed by an error

```python
record = ([1],)
try:
    record[0] += [2]
except TypeError:
    print(record)
```

Did the error undo all earlier changes? Connect the answer to the rule that an exception is not automatically a transaction rollback.

## 14. Declaration order

```python
print("start")
total = 10
def show():
    print(total)
    global total
```

Does `start` print? Is the problem found before or during a call to `show`?

Use the [coach key](coach/scenario-key.md) after an independent attempt. The reviewer records correct, partial, incorrect, and missing parts and asks a targeted variation.
