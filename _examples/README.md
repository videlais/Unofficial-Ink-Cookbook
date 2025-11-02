# Interactive Ink Examples

This directory contains interactive Ink examples that can be embedded in chapters using the `ink-player` include component.

## Directory Structure

Examples are organized by chapter:

```
_examples/
├── chapter04/          # Understanding Choices
├── chapter05/          # Managing Project Files (Knots & Stitches)
├── chapter08/          # It's All Variable
├── chapter09/          # Knot and Function Parameters
└── ...                 # Add more as needed
```

## Adding a New Example

### 1. Create the Ink File

Create a new `.ink` file in the appropriate chapter folder:

```bash
_examples/chapter04/my-example.ink
```

### 2. Write Your Ink Story

Keep examples focused and concise. Add comments to explain concepts:

```ink
// This example demonstrates sticky choices
// Sticky choices (+) remain available after being selected

VAR times_greeted = 0

Hello! I've greeted you {times_greeted} time(s).

+ [Say hello]
    ~ times_greeted = times_greeted + 1
    You say hello!
    -> DONE
```

### 3. Compile to JSON

You need to compile your `.ink` file to JSON format. You have several options:

#### Option A: Using Inky Editor
1. Open your `.ink` file in Inky
2. File → Export → "Export story.js only..."
3. Save as `.json` instead of `.js`
4. Place the JSON file in the same folder as your `.ink` file

#### Option B: Using inklecate (Command Line)
```bash
inklecate -o _examples/chapter04/my-example.json _examples/chapter04/my-example.ink
```

#### Option C: Using inkjs CLI
```bash
npx inkjs -o _examples/chapter04/my-example.json _examples/chapter04/my-example.ink
```

### 4. Embed in a Chapter

In your chapter markdown file, use the `ink-player` include:

```liquid
{% include ink-player.html 
   story="chapter04/my-example" 
   title="My Example Title"
   height="400px"
%}
```

**Parameters:**
- `story`: Path to your example (without `.ink` or `.json` extension) relative to `_examples/`
- `title`: (Optional) Display title for the example
- `height`: (Optional) Height of the player container (default: 400px)

## Example Files Naming Convention

Use descriptive, kebab-case names:
- ✅ `sticky-choices.ink`
- ✅ `variable-tracking.ink`
- ✅ `basic-knots.ink`
- ❌ `example1.ink`
- ❌ `test.ink`

## Testing Your Example

1. Make sure both `.ink` and `.json` files are in the same directory
2. Run Jekyll locally:
   ```bash
   bundle exec jekyll serve
   ```
3. Navigate to the chapter page with your embedded example
4. The example should load and be interactive

## Troubleshooting

### "Error loading story"
- Check that the `.json` file exists and is valid JSON
- Verify the `story` parameter path is correct
- Check browser console for specific error messages

### Source code not showing
- Make sure the `.ink` file is in the same location as the `.json` file
- Check that the filename matches exactly (case-sensitive)

### Styling issues
- The ink-player styles are in `assets/css/ink-player.scss`
- Customize the styles there if needed

## Best Practices

1. **Keep examples short**: Focus on demonstrating one concept clearly
2. **Add comments**: Explain what the Ink code does
3. **Test thoroughly**: Make sure all paths through your example work
4. **Consider edge cases**: What happens if the player makes unexpected choices?
5. **Use meaningful variable names**: Help readers understand the code
6. **Include variety**: Show different aspects of the feature being taught

## Current Examples

- `chapter04/sticky-choices.ink` - Demonstrates sticky (+) choices
- `chapter04/fallback-choices.ink` - Shows how fallback choices work
- `chapter05/knots-and-stitches.ink` - Basic navigation between knots
- `chapter08/basic-variables.ink` - Simple variable tracking

## Contributing

When adding examples:
1. Ensure they align with chapter content
2. Test that they compile and run correctly
3. Add clear comments explaining the concepts
4. Keep file sizes reasonable
5. Follow the naming conventions
