# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions
### Source of truth
- Treat `bytebites_spec.md` as the source of truth. If a request conflicts with the
  spec or isn't covered by it, point that out and ask before writing code.
- Stay within the four classes in the spec: `Customer`, `FoodItem`, `Menu`, and
  `Order`. Do not add new classes, base classes, or inheritance unless I ask for them.
- Only add attributes and methods that a requirement in the spec needs. If you think
  one is missing, suggest it and explain which requirement it serves rather than
  adding it silently.

### Complexity
- Use plain Python 3 with the standard library only. No third-party packages,
  frameworks, or ORMs.
- Keep all data in memory, using lists and simple object references. No files,
  databases, APIs, or networking.
- Prefer simple, readable algorithms (loops, list comprehensions, `sum()`) over
  clever or optimized ones. No design patterns, abstract classes, decorators, or
  async code unless I request them.
- Keep methods short and single-purpose.

### Code style
- Follow PEP 8 naming: `PascalCase` for classes, `snake_case` for attributes and
  methods.
- Add type hints to method parameters and return values.
- Give each class and public method a one-line docstring.
- Represent prices as `float` and round totals to two decimal places.
- Handle invalid input simply, such as negative prices or empty orders, by raising
  `ValueError` with a clear message. Don't build custom exception hierarchies.

### How to structure suggestions
- Work on one class or feature at a time, and keep each change small.
- Before writing code, briefly state which requirement in the spec the change
  covers.
- Show the full updated class, or a clearly marked snippet, plus a short example of
  how to use it.
- Keep explanations brief and beginner-friendly, explaining any Python feature
  that may be unfamiliar.
- When asked for tests, use the built-in `unittest` module or plain `assert`
  statements, and cover normal cases as well as at least one edge case.
- Keep the class diagram consistent with the code. If a change affects
  attributes, methods, or relationships, say so.
