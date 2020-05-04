# Chapter 12: Ink for the Web

- [Chapter 12: Ink for the Web](#chapter-12-ink-for-the-web)
  - [Ink for Web](#ink-for-web)
  - [Folder Organization](#folder-organization)
    - [Editing Files](#editing-files)
    - [Using Images](#using-images)
    - [Images Do Not Appear in Inky Preview](#images-do-not-appear-in-inky-preview)
  - [Meta Instructions](#meta-instructions)
    - [Author](#author)
    - [Theme](#theme)
    - [Clear](#clear)
    - [Restart](#restart)
  - [Adding CLASS](#adding-class)
    - [Changing CSS](#changing-css)
  - [Working with HTML](#working-with-html)
  - [Inline CSS and Choices](#inline-css-and-choices)
  - [Try It](#try-it)

**Summary:** In this chapter, you will learn more about the Ink for Web option, how it works, and special tags that can be used as part of Ink for Web.

---

## Ink for Web

So far in this book, Ink was shown running as part of Inky Editor. There is also another option for running Ink, Ink for the Web! As part of the Ink Editor, a website version of the Ink code can be created using the File → "Export for web..." option.

When using the Inky Editor, code written in Ink can be exported for the web. When used in this way, a compiled Ink project can be played in a web browser and shared on sites for others to see.

When used for the first time with a project, Inky will save the project based on the file name, creating a folder based on what is inputted in the Save As field.

## Folder Organization

Inside the exported project folder will be five files: `index.html`, `ink.js`, `main.js`, `style.css`, and `nameOfProject.js`.

[TODO: Add screenshot of folder structure in Windows and MacOS X]

To play the project locally, open the `index.html` file in a web browser. It should appear as it did in the editor view, but with the name of the project included at the top.

[TODO: Add screenshot of Ink for Web in browser]

### Editing Files

To prepare a project for others to play, two files are more important than the others: `index.html` and `style.css`. Unfortunately, these two files will be replaced each time the Export to Web process is completed!

When editing the `style.css file` (to change CSS rules), use the "Export story.js only..." option from the File menu and select the `nameOfProject.js` file to replace only that file each time.

### Using Images

Starting with release version 0.10, the Inky editor has the ability to build versions of Ink for the web with images using a new tag: `# IMAGE`.

**Reminder:** When used in Inky, tags are created using the hash symbol, `#`, and then additional instructions.

The image tag is used with the capitalized word `IMAGE` and a colon. Images are then referenced either in the current directory or with a relative path in relation to the `index.html` file.

**Note:** A *relative path* is a term meaning a location of a file that is not *absolute*. A relative path includes symbols like the period, `.` and slash, `/`. These define the location of a file *in relation* to another.

```ink
The vast dunes stretch off into the horizon. # IMAGE: dunes.png
```

In the above example, the file `dunes.png` has a relative path of the same folder as the `index.html` file. It would be loaded by the Ink for Web option.

### Images Do Not Appear in Inky Preview

When used in the Inky editor, tags will appear as-is within the preview area. *Images will not be loaded nor shown*.

To see the images, use either File –> Export to Web (for first time exporting) or File –> "Export story.js only..." (for additional exporting).

The reason for this is simple: the `# IMAGE` tag is just that, a *tag*. Ink, and Inky by extension, simply records tags and saves their values. *It does not process them.* It is the Ink for Web functionality that is processing the image tag and adding the image to the final, HTML output.

The following code would show only that a tag was being used, not load the image:

**Code:**

```ink
The vast dunes stretch off into the horizon. # IMAGE: dunes.png
```

**Output:**

```ink
The vast dunes stretch off into the horizon.
```

## Meta Instructions

Along with understanding code commands, the tagging system in Inky also allows for more meta instructions like author, theme, clear, and restart.

### Author

The author tag allows for adding an author to the project. Once added, the "author" area will appear under the title in the web version.

```ink
# AUTHOR: Jane Doe

My life really began after I died.
```

### Theme

By default, the "theme" (CSS style rules) is set to "white". As with other tags, including the keyword "theme:" and a new choice will change it. Version 0.10 introduced a new theme option: dark.

```ink
# THEME: dark

The rain pounded on the windows. Its staccato pace matched my own heart as its unsteady beat echoed each other. I had seen a ghost -- or, at least, I thought I did. Could this house really be haunted?
```

### Clear

While other instructions change code properties, CLEAR works only in the web-export version. It "clears" all other instructions and starts at the top of the screen with the next set of instructions.

Note that CLEAR should usually only be used after the player has made a choice - if you use it in the middle of a flow, it will clear all the text in that current flow before the player will have a chance to read it!

### Restart

Like CLEAR, RESTART also only works in the web-exported version of Ink. Instead of removing things, however, RESTART does as its name implies: it restarts the project.

Much like CLEAR, it is best to use RESTART after the player has made a choice, since it clears all the text on the screen as well.

## Adding CLASS

Like with working with the IMAGE tag, Ink/Inky also supports a tag for defining new CSS rules: CLASS.

When used at the end of a line, the Inky web-exported version will apply any CSS classes matching that name.

To add new CSS rules, edit the style.css file generated by the initial web-exporting process.

Adding or changing rules in this file will be reflected when the `index.html` file is refreshed in the web browser.

**Note:** When adding a new CLASS tag in a project, it will need to be exported again before those changes will appear. Be sure to use File –> "Export story.js only..." and replace the story before refreshing the `index.html` file!

### Changing CSS

The default CSS can also be updated through changing units or writing new rules in the style.css file.

Changing the rules for the `<p>` tag, for example, can make the text bigger.

The same with adding "underline" to the text-decoration rule for hyperlinks. This can better help with showing what text is a link or not.

Any additional rules or changes can be made to the style.css file. However, two things need to be remembered:

- Making changes in Inky means doing a File –> "Export story.js only..." before refreshing the index.html file to see those changes.
- Tags work on sections of text. When used after a selection of text on the same line, it will wrap that text in those styles. Otherwise, tags will work on the next section of text.

## Working with HTML

Along with using text in Inky, it is also possible to use HTML directly. Style elements such as `<strong>` and `<em>` can be used within the editor and their effects will show up in the preview pane.

While the styling of elements must happen through CSS rules, any HTML that has a structural or styling factor can be used in Inky and "passed through" to the Ink for Web usage as well.

This means that text can be arranged within the Inky Editor through using HTML directly, seeing its effect, and having the same structure show up in the output itself.

```html
<table>
  <tr>
    <td>Yes.</td>
    <td>It</td>
    <td> is possible to do things like this.</td>
  </tr>
</table>
<h1>And this?</h1>
```

## Inline CSS and Choices

By default, all of the choice text in the story will appear the same way. it is possible to change the styling of all of the choice text in a story by editing the rules of `p.choices` in the CSS stylesheet generated by Ink’s "Export for Web" option. Every individual choice will be styled in the same way, which can be somewhat limiting.

Luckily, there is a workaround within Ink to style individual choices! This workaround involves using inline CSS within the text of a choice to change the styling of that individual choice. While this workaround is not fully implemented at this time, it will things like change the color of individual choices. Consider the following example:

```ink
===FavoriteColor===

What is your favorite color?

+<p style = "color:blue;">Blue!</p>  ->Blue

+<p style = "color:red;">Red!</p>  ->Red

+<p style = "color:green;">Green!</p> ->Green
```

## Try It

The examples in this chapter demonstrate how you can use Ink’s web features to create stories that you can easily share on a website.

Many of these features rely on knowledge of HTML or CSS that is not fully covered in this book, but this chapter provides some basic examples that should get you started, even if you have never worked with those languages before. While there are plenty of resources online to help you learn HTML and CSS, it is also worth learning how such code works inside the Inky editor, as well as learning about Ink’s specialized web features.

We suggest completing the following practices exercises. Before beginning on them, we recommend that you choose a story you have created from one of the exercises in a previous chapter, though you can create a new story if you wish.

Add author information to your story and apply the dark theme to it using Ink’s specialized web features. Remember that you won’t be able to see these things in the Ink editor: you will only see them once your story has been exported for the web.

Find an appropriate visual for your story and use the image feature to add it. Again, keep in mind that you will not be able to see the image until the story is exported.

Add at least two HTML elements to your story. If you have never used HTML, try the `<strong>` and `<em>` examples shown earlier in the chapter. You should be able to see them in the Inky editor, so you can quickly determine if you have done it correctly or not!

(Optional) If you have used CSS before, add at least two of Ink’s CLASS tags to your story. If you have not used CSS before, you can skip this step.

Export your story for the web and view the resulting story in a web browser. Make sure the image from #2 above is in the same folder as your exporter story, and if you completed the optional #4 step, edit the stylesheet with the relevant CSS changes.
