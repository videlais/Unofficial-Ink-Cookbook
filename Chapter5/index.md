# Chapter 5: Managing Project Files

- [Chapter 5: Managing Project Files](#chapter-5-managing-project-files)
  - [Projects](#projects)
  - [Adding New Files](#adding-new-files)
  - [Knots Across Files](#knots-across-files)
  - [Stitches](#stitches)
  - [Try It](#try-it)

**Summary:** In this chapter, you will learn about managing a project through adding new files, working with stitches, and including other files in a project.

---

## Projects

In Inky, each new story is a new project. Understanding projects, then, becomes an important part of working with Inky and programming in Ink.

Projects are created through the File menu using File -> New Project.

## Adding New Files

Once a project has been created, new files can be added to it. When editing a project, use the File → New Included File option to create a new file and have it automatically included in the project.

**Note:** It is always good to save a project to a new directory when working with the Inky Editor. Inky will detect files with the `.ink` filetype and add them to the project.

For better organization in more complex projects, Ink stories can be broken up into different files. These can then be "included" through using the `INCLUDE` keyword. (This is automatically generated when the New Included File option is used. The file will be added, and the `INCLUDE` keyword will be added to the project file.)

```ink
INCLUDE Example.ink
```

## Knots Across Files

Once broken up, knots in other files can also be called by their names like they would if they were in the same file. As far as Ink is concerned, they are when using `INCLUDE`!

**KnotsAcrossFiles.ink:**

```ink
INCLUDE Example.ink

This story begins here, in this file. However, it quickly moves to another file, Example.ink.

-> Example_Knot
```

**Example.ink:**

```ink
=== Example_Knot ===
I'm in another file!
-> DONE
```

In the above code, the story begins in the file `KnotsAcrossFiles.ink`. When the divert is encountered, the story moves across files to `Example.ink`. However, as far as Ink was concerned, it was all one story!

## Stitches

Like breaking a project into different files, knots can also be broken into parts called *stitches*.

Stitches are *subsections of knots*. As a project can be broken up into files, so too can a knot be broken up into its own stitches!

```ink
* Pick out something good
    -> Getting_Ready.Pick_Out_Something_Good
* Don't bother
    -> Getting_Ready.Just_Grab_Something
```

Within a knot, a stitch is defined with a single equal sign `=`. Just like knots, they can also be a section to be diverted to.

As stitches are within knots, they must be referenced as such. A stitch takes its location as the `knotName.stitchName` with a dot between the two.

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

**StitchExample.ink:**

```ink
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
-> DONE

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

## Try It

Knots are sections of a story. They can be places, people, or useful logical separations of a large narrative. Stitches are like sub-sections of a knot. They are referenced using the knot's name.

As practice, try doing the following:

Using a previous project created from reading the **Try It** parts of another chapter or a brand new project, adopt or create a new story. This time, divide up the story into different locations the protagonist would visit.

For each location, create a new, included file in the project. Using the `INCLUDE` keyword, make sure all of the files can be accessed.

Within the story, have the protagonist visit these different locations, moving between the files of the project. Now, create stitches. In each location, each file, add something the protagonist would interact with there. This could be a person, animal, or even something like a statue!

Now, allow the player to divert to the stitches. (Remember, a stitch is referenced through its knot!) When playing, the story should present possible interaction choices in different places -- all of which are now in included files and are broken up into stitches!
