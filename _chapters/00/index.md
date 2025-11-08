---
title: "Introduction"
order: 0
chapter_number: 0
layout: chapter
---

## Chapter Summary

This introduction explains who this book is for, the style conventions used throughout, and how to read and interpret the various formatting elements you'll encounter in the chapters.

## Learning Objectives

By the end of this introduction, you will be able to:

- Identify the target audience and prerequisites for this book.
- Recognize the style conventions used throughout the chapters.
- Distinguish between different types of emphasis and code formatting.

## Table of Contents

- [Chapter Summary](#chapter-summary)
- [Learning Objectives](#learning-objectives)
- [Table of Contents](#table-of-contents)
- [Who This Book is For](#who-this-book-is-for)
- [What You'll Learn](#what-youll-learn)
- [Style Conventions](#style-conventions)
  - [Code Example](#code-example)
  - [Interactive Example](#interactive-example)
  - [Emphasis](#emphasis)
    - [Italics for Emphasis](#italics-for-emphasis)
    - [Bold for Key Terms](#bold-for-key-terms)
    - [Inline Code for Syntax](#inline-code-for-syntax)
- [Notes and Reminders](#notes-and-reminders)

## Who This Book is For

This is an open educational resource designed for a hobbyist or student audience. Some things such as the ability to navigate the book and copy and paste text are assumed.

Wherever possible, terms are explained and examples given. However, as this is an open educational resource, additional clarification or more examples can be requested!

Found something confusing? Have a suggestion? Submit an [Issue on GitHub](https://github.com/videlais/Unofficial-Ink-Cookbook/issues) to help improve this book for future audiences!

## What You'll Learn

Throughout this book, you'll explore:

- **Basic ink syntax**: Writing stories, creating flow, and understanding structure.
- **Choices and branching**: Building interactive narratives with player decisions.
- **Variables and state**: Tracking information and creating dynamic content.
- **Advanced techniques**: Organizing complex projects and implementing game logic.

---

## Style Conventions

This book uses some style conventions to visually explain concepts.

### Code Example

All ink code is marked in code blocks. It may appear `in-line`, but most code will appear as the following:

```ink
This is some code.
This is a second line of code.
```

### Interactive Example

In many chapters, ink code examples will be followed by an interactive version of the same code. This interactive player demonstrates how your code will run. You can interact with it using either the mouse (clicking on choices) or via keyboard (using Tab and Enter keys).

{% include ink-player.html
   story="chapter00/example"
   title="Example ink"
   height="350px"
%}

You'll see examples like this throughout the book to test and explore concepts interactively.

### Emphasis

#### Italics for Emphasis

In different places, *emphasis may be repeated to stress importance or connection to other, previous concepts.* For example, when we introduce the concept of *flow* in Chapter 1, it appears in italics to draw your attention.

#### Bold for Key Terms

Strong emphasis is used for important terms. For example, when formally defining a concept in a chapter, it may appear with **stronger emphasis** like **flow**. This indicates a term you should remember.

#### Inline Code for Syntax

Inline code like `VAR` is used for ink keywords, syntax elements, and short code snippets. This helps distinguish code from regular text. For example: "Use the `*` symbol to create a choice."

Choices are written using *emphasis*. However, their output is enclosed in quotation marks.

In Chapter 1, you'll begin writing your first ink stories using these formatting conventions.

---

## Notes and Reminders

Throughout this book, you'll encounter different types of callout boxes to highlight important information.

For notes, the following blockquote style will be used.

> **Note** Notes clarify or explain certain concepts. They provide additional context without interrupting the main flow.

For important information, the following blockquote style will be used.

> **Important** Important callouts highlight critical information you should pay special attention to.

For helpful suggestions and best practices, the following style will appear.

> **Tip** Tips offer helpful suggestions and best practices to improve your ink writing.

Common mistakes and potential issues will appear as the following:

> **Warning** Warnings alert you to common mistakes or potential issues to avoid.

These enhanced callouts use the formatting from the OpenTextbook theme to make important information easy to spot.
