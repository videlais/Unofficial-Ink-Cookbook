---
title: "Understanding Choices"
order: 2
chapter_number: 2
layout: chapter
---

## Learning Objectives

By the end of this chapter, you will be able to:

- Define ink as a narrative scripting language and describe its purpose.
- Install the Inky Editor on your operating system.
- Demonstrate basic file operations including opening, saving, and creating projects.
- Utilize the Preview pane to test and review your ink stories.

## Summary

In this chapter, you will learn about ink, where to find the Inky Editor, and generally how to install and use it through basics like opening, editing, and saving an ink file.

---

- [Learning Objectives](#learning-objectives)
- [Summary](#summary)
- [Inky Editor](#inky-editor)
- [Installing Inky](#installing-inky)
  - [Windows](#windows)
  - [macOS](#macos)
- [Using the Inky Editor](#using-the-inky-editor)
  - [Opening an Ink File](#opening-an-ink-file)
  - [Saving an Ink File](#saving-an-ink-file)
  - [Creating a New Project](#creating-a-new-project)
  - [Adding a New Included Ink File](#adding-a-new-included-ink-file)
  - [Working with an Inky Project](#working-with-an-inky-project)
    - [Rewind a Single Choice](#rewind-a-single-choice)
    - [Restart a Story](#restart-a-story)
- [Reviewing File Exports](#reviewing-file-exports)
  - [JSON Export](#json-export)
  - [Web Export](#web-export)
  - [Export Process](#export-process)
- [Try It](#try-it)

---

## Inky Editor

ink can be written in anything that can handle text. Some authors prefer to work in their favorite text editor and only move to another tool when it is time to create a compiled, final product. The choice, as always, is up to individual authors. However, the Inky Editor has something most other text editing programs do not: the Preview pane.

When writing ink using the Inky Editor, the code will be previewed on the right-hand side. Every time there is a stop in writing, the code preview will be updated and the compiled product shown to the user. This helps in not only seeing how the code will look when run, but the previewing area allows for rewinding through choices and restarting the story, providing a quick way to see how taking other paths through the story might also look to a player.

## Installing Inky

{% include figure.html src="chapters/02/chapter2-ink-website.png" alt="Screenshot of the ink website homepage showing the download section with a blue Download Inky button" caption="Figure 2.1: The ink website with download options for the Inky Editor" id="fig-2-1" %}

The [ink webpage](https://www.inklestudios.com/ink/) has a link to the Inky editor. Scroll down the page and click on the "Download" button under the name Inky. Builds exist for Windows, Mac, and Linux systems and can be found on the [Releases page](https://github.com/inkle/inky/releases/) for the product on GitHub. (Always download the most-current build to get the newest features and bug fixes!)

### Windows

When downloaded in Windows, Ink will be in a ZIP file. Uncompress the ZIP file and look for the Ink.exe executable file. Running this will open the Inky Editor.

### macOS

For macOS users, Inky will be in a DMG file. These can be opened and the Inky application moved into the Applications directory. Run Inky from inside the Application directory or directly from the Launchpad.

---

## Using the Inky Editor

{% include figure.html src="chapters/02/chapter2-ink-editor.png" alt="Screenshot of Inky Editor interface with code editor pane on the left containing ink script and preview pane on the right showing the compiled output" caption="Figure 2.2: The Inky Editor showing the dual-pane interface with code on the left and live preview on the right." id="fig-2-2" %}

When opened, the Inky Editor will show two main panes. The first, on the left, is where the code is written. As it is run in the editor, the results will be previewed on the right pane.

### Opening an Ink File

Existing Ink files can be opened through the File menu and going to File → Open. Any Ink files can be opened this way and will be loaded in the Editor with their code on the left and the previewed results of the code on the right.

### Saving an Ink File

A collection of Ink files is called a project. Even if a project only contains one file, it can still be saved through the File → Save Project menu option.

### Creating a New Project

A new project can be created through going to File → New Project. This will open a new window of the Inky Editor.

By default, Inky will list all current Ink files in the same directory of a newly created and saved Ink project.

### Adding a New Included Ink File

To more directly add a new Ink file to an existing project, the File → New Included Ink File option can be used. It will prompt what to name the file and then add it to the project.

### Working with an Inky Project

{% include figure.html src="chapters/02/chapter2-rewind.png" alt="Close-up of Inky Editor preview pane header showing two buttons: a left-pointing arrow labeled Rewind and a circular arrow labeled Restart" caption="Figure 2.3: Rewind and Restart buttons in the Inky Editor preview pane." id="fig-2-3" %}

Above the Preview pane where the Ink story is being run are two buttons: Rewind a Single Choice and Restart a Story.

The Preview pane will always show the End of Story as well. This is the true ending and is added when an author does not explicitly add it.

#### Rewind a Single Choice

While a story is being run, the Inky editor remembers each choice. At any point, these choices can be rewound by a single group of choices to the last previous position in the story.

#### Restart a Story

Similar to the Rewind a Single Choice button, the Restart Story button rewinds a story back to the first set of choices.

## Reviewing File Exports

The Inky Editor provides several export options to convert your Ink stories into formats that can be used by other applications and platforms. Understanding these export formats is crucial for integrating your Ink stories into games, web applications, or other interactive media.

### JSON Export

The most common export format is JSON (JavaScript Object Notation). When you compile your Ink story, Inky generates a `.json` file that contains the compiled story data. This JSON file can be read by:

- The Ink JavaScript runtime for web applications.
- Unity projects using the Ink Unity plugin.
- Custom applications using Ink runtime libraries.

To export to JSON, simply save your project in Inky, and the editor will automatically generate a corresponding `.json` file with the same name as your `.ink` file.

### Web Export

Inky also provides a "Export for web..." option under the File menu. This creates a standalone HTML file that includes:

- Your compiled story in JSON format.
- The Ink JavaScript runtime.
- A basic web interface for playing the story.
- CSS styling for a clean, readable presentation.

This web export is perfect for:

- Sharing your story online.
- Testing your story in a web browser.
- Creating prototypes for web-based narrative games.

### Export Process

1. Complete writing your ink story.
2. Save your project (File → Save Project).
3. For web export: go to File → Export for web...
4. Choose a location and filename for your exported file.
5. The exported file(s) will be ready to use in your target application.

---

## Try It

Let's practice working with ink files!

First, make sure you have downloaded the Inky Editor for your operating system.

Open the Inky Editor.

Copy or type the following in the left-hand code pane:

```ink
Greetings, Universe!
```

Over in the Preview pane, the results of the code will be shown.

{% include figure.html src="chapters/02/chapter2-preview.png" alt="Screenshot of Inky Editor preview pane displaying the text 'Greetings, Universe!' as output" caption="Figure 2.4: Preview pane showing the output of a simple ink script" id="fig-2-4" %}

By default, the name of a new ink project is "Untitled.ink".

Choose "Save Project" from the File menu. File → Save Project.

In the Save As field, name this file `Chapter2.ink`, select a location to save the file, and then click the "Save" button.

The Inky Editor will update its name to the new file. The project is now called "Chapter2.ink".

Congratulations on creating a new file, adding code, and then saving it!
