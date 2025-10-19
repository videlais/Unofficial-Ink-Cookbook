# OpenTextbook Theme

A modern, accessible Jekyll theme designed for open textbooks and educational content. This theme provides a clean, distraction-free reading experience while meeting WCAG 2.1 AAA accessibility standards.

## Features

- **Accessibility First**: Meets WCAG 2.1 AAA standards with keyboard navigation, screen reader support, and high contrast design
- **Chapter Management**: Built-in support for organizing content into chapters with automatic navigation
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Dark Mode**: Automatic dark mode support based on system preferences
- **Modern Styling**: Clean, professional design focused on readability
- **SEO Optimized**: Built-in SEO tags and sitemap generation
- **Print-Friendly**: Optimized print styles for offline reading

## Installation

### Option 1: Use as a Remote Theme (Recommended for GitHub Pages)

Add this to your `_config.yml`:

```yaml
remote_theme: videlais/opentextbook-theme
```

### Option 2: Clone This Repository

1. Clone this repository to create your textbook project:

   ```bash
   git clone https://github.com/videlais/opentextbook-theme.git my-textbook
   cd my-textbook
   ```

2. Install dependencies:

   ```bash
   bundle install
   ```

3. Customize `_config.yml` with your textbook information

## Configuration

Update `_config.yml` with your textbook information:

```yaml
title: Your Textbook Title
description: >-
  A description of your textbook
baseurl: "/your-repo-name"
url: "https://yourusername.github.io"

author:
  name: Your Name

license:
  text: "Creative Commons Attribution-ShareAlike 4.0 International License"
  url: "https://creativecommons.org/licenses/by-sa/4.0/"
  code: "Public Domain (CC0 1.0 Universal)"
  code_url: "https://creativecommons.org/publicdomain/zero/1.0/"
```

## Creating Chapters

1. Create a `_chapters` directory in your project
2. Add chapter files with front matter:

```markdown
---
title: "Chapter Title"
order: 1
chapter_number: 1
layout: chapter
---

## Chapter Content

Your chapter content goes here...
```

### Front Matter Options

- `title`: The chapter title (required)
- `order`: Numerical order for sorting chapters (required)
- `chapter_number`: The chapter number displayed to readers (required)
- `layout`: Should be "chapter" for chapter pages (required)

## Project Structure

```tree
your-textbook/
├── _chapters/           # Your chapter content
│   ├── chapter1.md
│   ├── chapter2.md
│   └── ...
├── _config.yml          # Site configuration
├── _layouts/            # Theme layouts (from this theme)
├── _includes/           # Theme partials (from this theme)
├── assets/             # Theme styles (from this theme)
├── index.md            # Home page
├── chapters.md         # All chapters listing
└── accessibility.md    # Accessibility statement
```

## Customization

### Override Layouts

Create files in your project's `_layouts/` directory with the same name to override theme layouts:

- `default.html` - Base layout
- `chapter.html` - Chapter layout
- `page.html` - Page layout

### Override Includes

Create files in your project's `_includes/` directory to override:

- `header.html` - Site header
- `footer.html` - Site footer
- `chapter-listing.html` - Chapter list component

### Custom Styles

Create `assets/custom.scss` to add custom styles:

```scss
---
---

@import "main";

// Your custom styles here
.custom-element {
  color: #your-color;
}
```

## Development

To run the site locally:

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` to see your site.

## Deployment

### GitHub Pages

1. Push your repository to GitHub
2. Enable GitHub Pages in repository settings
3. Select the branch containing your content
4. Your site will be available at `https://yourusername.github.io/your-repo-name`

### Other Hosting

Build the site:

```bash
bundle exec jekyll build
```

The generated site will be in the `_site` directory.

## Accessibility Features

This theme includes:

- Skip to main content link
- Keyboard navigation support
- ARIA labels and landmarks
- High contrast mode support
- Reduced motion support
- Minimum 44x44px touch targets
- Semantic HTML structure
- Screen reader optimizations

## Examples

See the theme in action:

- [Learning React](https://videlais.github.io/learning-react/) - The original implementation

## Contributing

Contributions are welcome! Please:

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This theme is released under the MIT License. See LICENSE for details.

## Credits

Created by Dan Cox for use in open educational resources.

Based on the theme developed for [Learning React](https://github.com/videlais/learning-react). A GitHub Pages theme using WCAG AAA guidelines for open access learning resources.
