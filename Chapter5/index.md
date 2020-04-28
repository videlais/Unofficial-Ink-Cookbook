# Chapter 5: Managing Project Files

- [Chapter 5: Managing Project Files](#chapter-5-managing-project-files)
  - [Projects](#projects)
  - [Adding New Files](#adding-new-files)
    - [Including Files](#including-files)
  - [Stitches](#stitches)

**Summary:** In this chapter, you will learn about managing a project through adding new files, working with stitches, and including other files in a project.

## Projects

In Inky, each new file is a new project. Managing project, then, becomes an important part of working with Inky and programming in Ink.

In the Inky Editor, creating a new file is creating a New Project. It is assumed that any new file will be part of a different project (unless added through the New Included File option).

It is always good to save a project to a new directory when working with the Inky Editor, too. The reason for this is that additional Ink files can be added. Inky will detect these files and then add them to the project. This allows for quickly working between files and knowing which files are part of which project.

## Adding New Files

Once a project has been created, new files can be added to it. When editing a project, using the File → New Included File option to create a new file and have it automatically included in the project.

### Including Files

For better organization in more complex projects, Ink stories can be broken up into files. These can then be "included" through using the `INCLUDE` keyword. This is automatically generated when the New Included File option is used. The file will be added, and the `INCLUDE` keyword will be added to the project file.

```ink
INCLUDE Dinner
INCLUDE GettingReady
```

Once broken up, knots in other files can be called by their names like they would if they were in the same file.

**GettingReady.ink:**

```ink
=== Getting_Ready ===

= Pick_Out_Something_Good
  I took some time and picked out something good.
  -> Chapter_3
  
= Just_Grab_Something
  I just grabbed some clothes off the floor and ran out.
  -> Chapter_3
```

This allows for using diverts and knots across files, branching off into other parts and returning to others through having files be those locations, people, or other logical sections of a much longer flow.

## Stitches

Like breaking a project into different files, knots can also be broken into parts called Stitches. As reviewed in the Common Terms section, Stitches are subsections of Knots. As a project can be broken up into files, so too can a Knot be broken up into its own Stitches.

```ink
* Pick out something good
    -> Getting_Ready.Pick_Out_Something_Good
* Don't bother
    -> Getting_Ready.Just_Grab_Something
```

Within a knot, a stitch is defined with a single equal sign `=`. Just like knots, they can also be a section to be diverted to. However, as stitches are within knots, they must be referenced as such. A stitch takes its location as the knotName.stitchName with a dot between the two.

**GettingReady.ink:**

```ink
=== Getting_Ready ===

= Pick_Out_Something_Good
  I took some time and picked out something good.
  -> Chapter_3
  
= Just_Grab_Something
  I just grabbed some clothes off the floor and ran out.
  -> Chapter_3
```

Combined with the `INCLUDE` keyword, stitches in other files can be reached through including the file and then using their knot name followed by their stitch name.

**Example:**

**Example.ink:**

```ink
INCLUDE Dinner
INCLUDE GettingReady

CHAPTER 1: ASKING HIM OUT

I was unsure about asking him out on a date. What would we do? Where would we go?

I let it go for weeks.

Finally, I asked him out.

-> Chapter_2

=== Chapter_2 ===
CHAPTER 2: GETTING READY

Why hadn't I thought about what I was going to wear? Here I am, 30 minutes before the date and I haven't picked out my clothes!

* Pick out something good
    -> Getting_Ready.Pick_Out_Something_Good
* Don't bother
    -> Getting_Ready.Just_Grab_Something

-> Chapter_3

=== Chapter_3 ===
CHAPTER 3: EATING DINNER

-> Dinner
```

**Dinner.Ink:**

```ink
=== Dinner ===

But I hadn't made dinner plans! And they we were, standing outside his apartment.

He turned to me. "What should we eat?"

-> Pizza_Choices

=== Pizza_Choices ===
+ {Pizza < 1} [Pizza?]
    -> Pizza
+ {Pizza} {Salad < 1} [Salad?]
    -> Salad
+ {Pizza} {Salad} {Nothing < 2} [Nothing?]
    -> Nothing
+ {Pizza} {Salad} {Nothing} [Sushi?]
    -> Sushi

=== Pizza ===
He shook his head. "I don't like pizza."
-> Pizza_Choices

=== Sushi ===
"Sushi sounds good!"
-> DONE

=== Salad ===
"Not a salad."
-> Pizza_Choices

=== Nothing ===
{"We have to eat something!"|"Stop being silly!"}
-> Pizza_Choices
```

**GettingReady.ink:**

```ink
=== Getting_Ready ===

= Pick_Out_Something_Good
  I took some time and picked out something good.
  -> Chapter_3
  
= Just_Grab_Something
  I just grabbed some clothes off the floor and ran out.
  -> Chapter_3
```
