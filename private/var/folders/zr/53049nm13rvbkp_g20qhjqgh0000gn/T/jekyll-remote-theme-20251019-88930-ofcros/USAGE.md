# OpenTextbook Theme Usage Guide

This guide will help you get started using the OpenTextbook theme for your Jekyll-based textbook.

## Quick Start

### 1. Create Your Project

Clone this repository or use it as a template:

```bash
git clone https://github.com/videlais/opentextbook-theme.git my-textbook
cd my-textbook
rm -rf .git  # Remove the theme's git history
git init     # Start fresh with your own repository
```

### 2. Install Dependencies

Install Ruby gems:

```bash
bundle install
```

### 3. Configure Your Textbook

Edit `_config.yml` to customize for your textbook:

```yaml
title: My Textbook Title
description: A comprehensive guide to...
baseurl: "/my-textbook"
url: "https://yourusername.github.io"

author:
  name: Your Name
```

### 4. Test Locally

Run the Jekyll development server:

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` to preview your site.

## Creating Content

### Adding a New Chapter

1. Create a new file in `_chapters/`:

    ```bash
    touch _chapters/chapter3.md
    ```

2. Add front matter and content:

    ```markdown
    ---
    title: "Your Chapter Title"
    order: 3
    chapter_number: 3
    layout: chapter
    ---

    ## Introduction

    Your chapter content here...
    ```

### Chapter Front Matter Fields

- **title** (required): The chapter title displayed to readers
- **order** (required): Numerical order for sorting (can be non-sequential)
- **chapter_number** (required): The chapter number shown to readers
- **layout** (required): Should always be "chapter"

### Adding Regular Pages

Create a new markdown file in the root directory:

```markdown
---
layout: page
title: About
permalink: /about/
---

## About This Textbook

Content here...
```

## Customizing the Theme

### Adding Custom CSS

Create `assets/custom.scss`:

```scss
---
---

@import "main";

// Your custom styles
.my-custom-class {
  color: blue;
}
```

Update `_config.yml` to use custom CSS:

```yaml
sass:
  style: compressed
  sass_dir: _sass
```

### Modifying Layouts

To customize a layout:

1. Copy the layout from `_layouts/` to your project's `_layouts/`
2. Make your changes
3. The custom version will override the theme version

### Modifying Includes

Same process for includes:

1. Copy from `_includes/` to your project's `_includes/`
2. Customize as needed

## Publishing

### GitHub Pages

1. Push to GitHub:

    ```bash
    git add .
    git commit -m "Initial textbook setup"
    git remote add origin https://github.com/yourusername/your-repo.git
    git push -u origin main
    ```

2. Enable GitHub Pages:

   - Go to repository Settings
   - Navigate to Pages
   - Select source branch (usually `main`)
   - Save

3. Your site will be available at:
   `https://yourusername.github.io/your-repo-name`

### Custom Domain

To use a custom domain with GitHub Pages:

1. Add a `CNAME` file in your repository root:

   ```text
   yourdomain.com
   ```

2. Configure DNS settings at your domain registrar

3. Enable HTTPS in GitHub Pages settings

## Best Practices

### Chapter Organization

- Use sequential order numbers (1, 2, 3...) for simplicity
- Keep chapter files named consistently: `chapter1.md`, `chapter2.md`
- Use descriptive titles that clearly indicate chapter content

### Content Structure

- Start each chapter with learning objectives
- End with a summary
- Use headings (##, ###) to organize content hierarchically
- Include examples and exercises where appropriate

### Accessibility

- Always provide alt text for images
- Use semantic heading structure (don't skip levels)
- Ensure sufficient color contrast
- Test with keyboard navigation

### Version Control

- Commit frequently with descriptive messages
- Use branches for major revisions
- Tag releases for different editions

## Troubleshooting

### Jekyll Won't Build

Check for:

- Syntax errors in YAML front matter
- Missing required front matter fields
- Incompatible plugin versions

Run with verbose output:

```bash
bundle exec jekyll serve --verbose
```

### Chapters Not Appearing

Verify:

- Files are in `_chapters/` directory
- Front matter includes all required fields
- `order` field is a number, not a string
- Files have `.md` extension

### Styles Not Loading

Check:

- `assets/main.scss` exists
- Front matter dashes (---) are at the top of the file
- No syntax errors in SCSS

## Advanced Topics

### Multiple Chapter Collections

You can create additional collections for different content types:

```yaml
# _config.yml
collections:
  chapters:
    output: true
  appendices:
    output: true
    permalink: /:collection/:name/
```

### Custom Permalinks

Customize chapter URLs:

```yaml
collections:
  chapters:
    output: true
    permalink: /ch/:chapter_number/
```

### Adding Search

Consider adding a search plugin like `jekyll-search` or `lunr.js` for larger textbooks.

## Getting Help

- Check the [README](README.md) for general information
- Review sample chapters in `_chapters/`
- Consult [Jekyll documentation](https://jekyllrb.com/docs/)
- Open an issue on GitHub for theme-specific questions

## Contributing Back

If you make improvements to the theme:

1. Fork the theme repository
2. Make your changes
3. Submit a pull request

Your contributions help improve the theme for everyone!
