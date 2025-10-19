# Quick Reference

## File Structure

```tree
opentextbook-theme/
├── _chapters/          # Chapter content (create your chapters here)
├── _includes/          # Reusable HTML partials
│   ├── header.html
│   ├── footer.html
│   └── chapter-listing.html
├── _layouts/           # Page layouts
│   ├── default.html
│   ├── chapter.html
│   └── page.html
├── assets/            # Styles and static files
│   └── main.scss
├── _config.yml        # Site configuration
├── Gemfile            # Ruby dependencies
├── .gitignore         # Git ignore rules
├── index.md           # Home page
├── chapters.md        # All chapters listing
├── accessibility.md   # Accessibility statement
├── README.md          # Project documentation
├── USAGE.md          # Usage guide
└── CHANGELOG.md      # Version history
```

## Common Commands

```bash
# Install dependencies
bundle install

# Run local development server
bundle exec jekyll serve

# Build site for production
bundle exec jekyll build

# Build and watch for changes
bundle exec jekyll serve --livereload

# Check for errors
bundle exec jekyll doctor
```

## Chapter Template

```markdown
---
title: "Chapter Title"
order: 1
chapter_number: 1
layout: chapter
---

## Introduction

Your content here...

## Summary

Chapter summary...
```

## Page Template

```markdown
---
layout: page
title: Page Title
permalink: /page-url/
---

# Page Heading

Your content here...
```

## Configuration Checklist

- [ ] Update `title` in _config.yml
- [ ] Update `description` in _config.yml
- [ ] Update `baseurl` in _config.yml
- [ ] Update `url` in _config.yml
- [ ] Update `author.name` in _config.yml
- [ ] Customize license information
- [ ] Update index.md with your introduction
- [ ] Update accessibility.md with contact info
- [ ] Remove or customize sample chapters

## Front Matter Fields

### Chapter Front Matter

- `title`: Chapter title (required)
- `order`: Sorting order (required, number)
- `chapter_number`: Display number (required, number)
- `layout`: Always "chapter" (required)

### Page Front Matter

- `layout`: Usually "page" (required)
- `title`: Page title (required)
- `permalink`: Custom URL (optional)

## Deployment

### GitHub Pages

1. Push to GitHub
2. Settings → Pages
3. Select branch
4. Save

### Custom Domain

1. Add CNAME file with domain name
2. Configure DNS at registrar
3. Enable HTTPS in settings

## Customization Quick Tips

### Change Colors

Edit CSS variables in `assets/main.scss`:

```scss
:root {
  --text-color: #your-color;
  --link-color: #your-color;
}
```

### Add Custom Navigation

Edit `_includes/header.html`

### Modify Footer

Edit `_includes/footer.html`

### Add Custom Styles

Create `assets/custom.scss`:

```scss
---
---
@import "main";
// Your styles here
```

## Accessibility Quick Check

- [ ] All images have alt text
- [ ] Headings are in logical order
- [ ] Links have descriptive text
- [ ] Color contrast is sufficient
- [ ] Site works with keyboard only
- [ ] Site works with screen reader

## Common Issues

**Chapters not showing?**

- Check front matter has all required fields
- Verify files are in `_chapters/` directory
- Ensure `order` is a number, not string

**Styles not loading?**

- Check `assets/main.scss` has front matter dashes
- Clear Jekyll cache: `rm -rf .jekyll-cache`
- Rebuild: `bundle exec jekyll build --force`

**Build errors?**

- Run `bundle exec jekyll build --verbose`
- Check YAML syntax in front matter
- Verify all plugins are installed

## Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/pages)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Markdown Guide](https://www.markdownguide.org/)
